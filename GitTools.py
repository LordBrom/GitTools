import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime
import re

from .Core.Controller          import *
from .Core.SetStatusItems      import *

from .Commands.gitAdd          import *
from .Commands.gitCommit       import *
from .Commands.gitDiff         import *
from .Commands.gitFetch        import *
from .Commands.gitLog          import *
from .Commands.gitPull         import *
from .Commands.gitPush         import *
from .Commands.gitRemoteBranch import *
from .Commands.gitRepoStatus   import *
from .Commands.gitSetScope     import *


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


		self.rootDir = self.get_scoped_path('repo')
		branches = self.run_git_command(["git", "branch"], self.rootDir)

		currentBranch = ''
		branches = branches.split( '\n' )
		for branch in branches:
			if len(branch) and branch[0] == '*':
				currentBranch = branch[1:].strip( )
				break


		# view.set_status('AAcgitTool', 'Repo: ' + currentBranch)


		# sublime.active_window().active_view().show_popup_menu(['item1','item2'], self.done)
		# print(sublime.active_window().active_view().style())
		# sublime.ok_cancel_dialog('test', sublime.platform())
		# self.dir = self.get_scoped_path('repo')
		# grepString = 'test'
		# cmd = self.run_git_command(["git", "log", "--no-commit-id", "--grep", grepString, "--oneline", "--name-status"], self.dir)
		# # cmd = self.run_git_command(["git", "diff", "--no-color"], self.dir)
		# cmd = self.run_git_command(["git", "diff-files", "--name-status", "--ignore-submodules=all"], self.dir)
		# show_output_panel(cmd)

	def done(self, index):
		print(index)

