import sys, os
from copier_templates_extensions import ContextHook
# Insert this directory onto the python path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from main import menu

class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        #context["subdir"] = "web/svelte-storybook-vite"
        menu()
        # TODO leaves temp directory behind
        exit()
