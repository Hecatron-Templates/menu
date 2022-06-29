import yaml
from os import path

class MenuConfig():
    def __init__(self):
        self.cfg_file="../menu_items.yaml"
        self.yaml_cfg = None
        self.menu_groups = []

    def get_cfg_filepath(self):
        cur_dir = path.dirname(path.realpath(__file__))
        cfg_file_path = path.join(cur_dir, self.cfg_file)
        return cfg_file_path

    def read_cfg(self):
        cfg_file_path = self.get_cfg_filepath()
        with open(cfg_file_path, 'r') as f:
            self.yaml_cfg = yaml.load(f, Loader=yaml.FullLoader)
        return self.yaml_cfg

    def get_groups(self):
        tmpset = set()
        for site in self.yaml_cfg['sites']:
            tmpset.add(site)
        self.menu_groups = sorted(tmpset)

    def get_templates(self, group_name):
        return self.yaml_cfg['sites'][group_name]

    def get_templates_indexed(self, group_name):
        tmpls = self.get_templates(group_name)
        ret = []
        for x in range(0, len(tmpls)):
            ret.append((tmpls[x]['name'], x))
        return ret

    def get_template(self, group_name, tmpl_name):
        tmpls = self.get_templates(group_name)
        tmpl = []
        for x in range(0, len(tmpls)):
            if tmpls[x]['name'] == tmpl_name:
                tmpl = tmpls[x]
        return tmpl

    def read(self):
        self.read_cfg()
        self.get_groups()
