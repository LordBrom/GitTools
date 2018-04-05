import sublime
import sublime_plugin

from ..Core.Controller import *

class gitPushCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit):
		print('push')
		# git.exe push --progress "origin" HomeCheckOut:NateHomeCheckout
		self.dir = self.get_scoped_path('repo')
		branch = git_settings().get('remoteBranch', '')
		if len(branch) == 0:
			self.set_branch()
		else:
			self.do_push(branch)

	def set_branch():
		sublime.active_window().show_input_panel("Remote Brach Name:", "", self.do_push, None, None)

	def do_push(self, remoteBranch):
		git_settings().set('history', history)
		sublime.save_settings('GitTools.sublime-settings')
		self.run_git_command(["git", "push", "origin", remoteBranch], self.dir)