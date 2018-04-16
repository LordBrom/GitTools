import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

from .Core.Controller      import *
from .Core.SetStatusItems  import *

from .Commands.gitCommit   import *
from .Commands.gitPush     import *
from .Commands.gitDiff     import *
from .Commands.gitLog      import *
from .Commands.gitSetScope import *
from .Commands.gitRemoteBranch import *


def plugin_loaded():
	print("loaded")

class gitEventListener(sublime_plugin.EventListener, gitController):
    def on_activated_async(self, view):
        git_set_status_items(self, view)

    def on_post_save_async(self, view):
        git_set_status_items(self, view)