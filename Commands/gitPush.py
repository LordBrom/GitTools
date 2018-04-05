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

	def set_branch(self):
		sublime.active_window().show_input_panel("Remote Brach Name:", "", self.do_push, None, None)

	def new_branch(self, remoteBranch):
		cmd = self.run_git_command(["git", "branch", "--set-upstream-to", "origin/"+remoteBranch], self.dir)
		show_output_panel(cmd)
		return
		self.do_push(remoteBranch)


	def do_push(self, remoteBranch):
		print(remoteBranch)
		git_settings().set('remoteBranch', remoteBranch)
		sublime.save_settings('GitTools.sublime-settings')
		cmd = self.run_git_command(["git", "push", "origin"], self.dir)
		show_output_panel(cmd)
		print('done pushing')