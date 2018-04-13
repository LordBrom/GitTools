import sublime
import sublime_plugin

from ..Core.Controller import *

def git_set_status_items(self, view):
    controller = gitController()

    if git_settings().get('show_status_bar_info', 1) == 1:
        controller.gitDir = controller.get_git_dir()
        if len(controller.gitDir) == 0:
            view.set_status('AAAgitTool', 'Git:' + u'\u2718')
        else:
            view.set_status('AAAgitTool', 'Git:' + u'\u2714')
    else:
        view.erase_status('AAAgitTool')
