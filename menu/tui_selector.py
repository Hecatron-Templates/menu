from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, ListBox, Widget
from asciimatics.exceptions import StopApplication
from copier import run_auto
import re

class SelectorFrame(Frame):
    def __init__(self, screen, cfg, args):
        self.cfg = cfg
        self.args = args

        frame_y = 8
        frame_height = screen.height - frame_y
        frame_width = int(screen.width - 2)

        frame_minheight = 15
        if (frame_height < frame_minheight):
            frame_height = frame_minheight
            frame_y = screen.height - frame_minheight

        # Setup the Frame
        super(SelectorFrame, self).__init__(
            screen,
            frame_height,
            frame_width,
            y=frame_y,
            has_shadow=True,
            name="Tempaltes",
            title="Templates",
            hover_focus=True,
            can_scroll=False)
        #self.set_theme("default")
        self.set_theme("green")

        self._add_header_layout()
        self._add_main_layout()
        self._add_button_layout()


    def _add_header_layout(self):
        layout = Layout([1, 3])
        self.add_layout(layout)
        layout.add_widget(Label("Name: ", align=">"), 0)
        layout.add_widget(Label("Link: ", align=">"), 0)
        layout.add_widget(Label("Description: ", align=">"), 0)

        self.NameLbl = Label("test", align="<")
        layout.add_widget(self.NameLbl, 1)
        self.LinkLbl = Label("", align="<")
        layout.add_widget(self.LinkLbl, 1)
        self.DescLbl = Label("", align="<")
        layout.add_widget(self.DescLbl, 1)

        layout.add_widget(Divider(height=3), 0)
        layout.add_widget(Divider(height=3), 1)
        return


    def _add_main_layout(self):
        layout = Layout([1, 1], fill_frame=True)
        self.add_layout(layout)

        # Setup Groups ListBox
        layout.add_widget(Label("Group", align="^"), 0)
        indexed_groups = []
        for x in range(0, len(self.cfg.menu_groups)):
            indexed_groups.append((self.cfg.menu_groups[x], x))
        self.GroupLB = ListBox(
            height=Widget.FILL_FRAME,
            add_scroll_bar=True,
            on_change=self._on_group_change,
            options = indexed_groups)
        layout.add_widget(self.GroupLB, 0)

        # Setup Templates Listbox
        layout.add_widget(Label("Template", align="^"), 1)
        self.TemplateLB = ListBox(
            height=Widget.FILL_FRAME,
            add_scroll_bar=True,
            on_change=self._on_tmpl_change,
            options = [])
        layout.add_widget(self.TemplateLB, 1)


    def _add_button_layout(self):
        layout = Layout([1, 1])
        self.add_layout(layout)
        layout.add_widget(Button("Quit", self._quit_butt), 0)
        layout.add_widget(Button("Select", self._select_butt), 1)
        self.fix()


    def _on_group_change(self):
        group_selected_name = self._get_selected_group()
        tmpls = self.cfg.get_templates_indexed(group_selected_name)
        self.TemplateLB.options = tmpls
        self._on_tmpl_change()


    def _on_tmpl_change(self):
        group_name = self._get_selected_group()
        tmpl_name = self._get_selected_tmpl()
        tmpl = self.cfg.get_template(group_name, tmpl_name)
        self.NameLbl.text = tmpl['name']
        self.LinkLbl.text = tmpl['link']
        self.DescLbl.text = tmpl['description']


    def _get_selected_group(self):
        group_selected_name = self.GroupLB.options[self.GroupLB.value][0]
        return group_selected_name

    def _get_selected_tmpl(self):
        tmpl_selected_name = self.TemplateLB.options[self.TemplateLB.value][0]
        return tmpl_selected_name


    def _select_butt(self):
        group_name = self._get_selected_group()
        tmpl_name = self._get_selected_tmpl()
        tmpl = self.cfg.get_template(group_name, tmpl_name)
        link = tmpl['link']
        run_auto(link, self.args[1])
        raise StopApplication("Complete")


    def _quit_butt(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Are you sure?",
                        ["Yes", "No"],
                        on_close=self._quit_on_yes))


    def _quit_on_yes(self, selected):
        if selected == 0:
            raise StopApplication("Quit")
