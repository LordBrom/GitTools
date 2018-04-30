import sublime
import sublime_plugin

from ..Core.Controller import *

def git_set_status_items(self, view):
    controller = gitController()

    if git_settings().get('Git.show_status_bar_info', 1) == 1:
        controller.gitDir = controller.get_git_dir()
        if len(controller.gitDir) == 0:
            view.set_status('AAAgitTool', 'Git:' + u'\u2718')
            view.erase_status('AABgitTool')
        else:
            view.set_status('AAAgitTool', 'Git:' + u'\u2714')
            view.set_status('AABgitTool', 'Scope: ' + str(git_settings().get('Git.commit_scope', 'file')))
    else:
        view.erase_status('AAAgitTool')
        view.erase_status('AABgitTool')
