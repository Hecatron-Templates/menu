import json
from os import path

class MenuConfig():
    def __init__(self):
        self.cfg_file="../menu_items.json"
        self.json_cfg = None
        self.menu_groups = []

    def get_cfg_filepath(self):
        cur_dir = path.dirname(path.realpath(__file__))
        cfg_file_path = path.join(cur_dir, self.cfg_file)
        return cfg_file_path

    def read_cfg(self):
        cfg_file_path = self.get_cfg_filepath()
        with open(cfg_file_path, 'r') as f:
            file_str = f.read()
        self.json_cfg = json.loads(file_str)
        return self.json_cfg

    def get_groups(self):
        tmpset = set()
        for site in self.json_cfg['sites']:
            group_name = site['group']
            tmpset.add(group_name)
        self.menu_groups = sorted(tmpset)

    def read(self):
        self.read_cfg()
        self.get_groups()
