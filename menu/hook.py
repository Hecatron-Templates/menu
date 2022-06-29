import sys, os
from copier_templates_extensions import ContextHook
# Insert this directory onto the python path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from main import menu

class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        menu(sys.argv)

		# Allow copier to exit cleanly instead of just calling exit()
        context["subdir"] = "menu/dummy"
