import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime
import re

from .Core.Controller      import *
from .Core.SetStatusItems  import *

from .Commands.gitCommit   import *
from .Commands.gitPush     import *
from .Commands.gitDiff     import *
from .Commands.gitLog      import *
from .Commands.gitSetScope import *
from .Commands.gitRemoteBranch import *
from .Commands.gitRepoStatus import *
from .Commands.gitAdd import *


def plugin_loaded():
	print("loaded")

class gitEventListener(sublime_plugin.EventListener, gitController):
	def on_activated_async(self, view):
		git_set_status_items(self, view)

	def on_post_save_async(self, view):
		git_set_status_items(self, view)


class gitTestCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit):
		self.debug_print(message = "test command",first = True, last = True)
		# self.dir = self.get_scoped_path('repo')
		# grepString = 'test'
		# cmd = self.run_git_command(["git", "log", "--no-commit-id", "--grep", grepString, "--oneline", "--name-status"], self.dir)
		# # cmd = self.run_git_command(["git", "diff", "--no-color"], self.dir)
		# cmd = self.run_git_command(["git", "diff-files", "--name-status", "--ignore-submodules=all"], self.dir)
		# show_output_panel(cmd)


		window = sublime.active_window()
		view = window.active_view()
		settings = view.settings()

		is_composer_enabled = view.settings().get('message_placeholders')
		self.debug_print(message = is_composer_enabled,first = True, last = True)

