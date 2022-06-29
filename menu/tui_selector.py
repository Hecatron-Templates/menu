from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, ListBox, Widget
import re

# Initial data for the form
#form_data = {
#    "TA": ["Hello world!", "How are you?"],
#    "TB": "alphabet",
#    "TC": "123",
#    "TD": "a@b.com",
#    "Things": 2,
#    "CA": False,
#    "CB": True,
#    "CC": False,
#}


class SelectorFrame(Frame):
    def __init__(self, screen, cfg):

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
        
        # Setup main layout
        self.set_theme("default")
        layout = Layout([1, 1], fill_frame=True)
        self.add_layout(layout)

        # Setup Groups ListBox
        layout.add_widget(Label("Group", align="^"), 0)
        indexed_groups = []
        for x in range(0, len(cfg.menu_groups)):
            indexed_groups.append((cfg.menu_groups[x], x))
        self.GroupLB = ListBox(
            height=Widget.FILL_FRAME,
            add_scroll_bar=True,
            on_change=self._on_group_change,
            options = indexed_groups)
        layout.add_widget(self.GroupLB, 0)




        opts1 = []
        for x in range(1, 22):
            opts1.append(("item" + str(x), x))

        layout.add_widget(Label("Template", align="^"), 1)
        layout.add_widget(ListBox(
            height=Widget.FILL_FRAME,
            add_scroll_bar=True,
            options = opts1), 1)
        
        #self._reset_button = Button("Reset", self._reset)
        #layout.add_widget(Label("Group 1:"), 1)
        #layout.add_widget(TextBox(5,
        #                          label="My First Box:",
        #                          name="TA",
        #                          on_change=self._on_change), 1)
        #layout.add_widget(
        #    Text(label="Alpha:",
        #         name="TB",
        #         on_change=self._on_change,
        #         validator="^[a-zA-Z]*$"), 1)
        #layout.add_widget(
        #    Text(label="Number:",
        #         name="TC",
        #         on_change=self._on_change,
        #         validator="^[0-9]*$"), 1)
        #layout.add_widget(
        #    Text(label="Email:",
        #         name="TD",
        #         on_change=self._on_change,
        #         validator=self._check_email), 1)
        #layout.add_widget(Divider(height=2), 1)
        #layout.add_widget(Label("Group 2:"), 1)
        #layout.add_widget(RadioButtons([("Option 1", 1),
        #                                ("Option 2", 2),
        #                                ("Option 3", 3)],
        #                               label="A Longer Selection:",
        #                               name="Things",
        #                               on_change=self._on_change), 1)
        #layout.add_widget(CheckBox("Field 1",
        #                           label="A very silly long name for fields:",
        #                           name="CA",
        #                           on_change=self._on_change), 1)
        #layout.add_widget(
        #    CheckBox("Field 2", name="CB", on_change=self._on_change), 1)
        #layout.add_widget(
        #    CheckBox("Field 3", name="CC", on_change=self._on_change), 1)
        #layout.add_widget(Divider(height=3), 1)
        layout2 = Layout([1, 1])
        self.add_layout(layout2)
        #layout2.add_widget(self._reset_button, 0)
        #layout2.add_widget(Button("View Data", self._view), 1)
        layout2.add_widget(Button("Quit", self._quit), 0)
        layout2.add_widget(Button("Select", self._quit), 1)
        self.fix()

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Are you sure?",
                        ["Yes", "No"],
                        on_close=self._quit_on_yes))

    @staticmethod
    def _quit_on_yes(selected):
        # Yes is the first button
        if selected == 0:
            exit()










    def _on_group_change(self):
        group_selected_val = self.GroupLB.value
        group_selected_name = self.GroupLB.options[group_selected_val][0]
        
        changed = False
    #    self.save()
    #    for key, value in self.data.items():
    #        if key not in form_data or form_data[key] != value:
    #            changed = True
    #            break
    #    self._reset_button.disabled = not changed

    #def _reset(self):
    #    self.reset()
    #    raise NextScene()

    #def _view(self):
    #    # Build result of this form and display it.
    #    try:
    #        self.save(validate=True)
    #        message = "Values entered are:\n\n"
    #        for key, value in self.data.items():
    #            message += "- {}: {}\n".format(key, value)
    #    except InvalidFields as exc:
    #        message = "The following fields are invalid:\n\n"
    #        for field in exc.fields:
    #            message += "- {}\n".format(field)
    #    self._scene.add_effect(
    #        PopUpDialog(self._screen, message, ["OK"]))



    #@staticmethod
    #def _check_email(value):
    #    m = re.match(r"^[a-zA-Z0-9_\-.]+@[a-zA-Z0-9_\-.]+\.[a-zA-Z0-9_\-.]+$",
    #                 value)
    #    return len(value) == 0 or m is not None

