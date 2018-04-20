import sublime
import sublime_plugin

from ..Core.Controller import *
from ..Core.History import *

class gitCommitCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit, showHistory = False):

		self.path = self.get_git_dir()
		if len(self.path) == 0:
			return;

		self.path = self.get_scoped_path(git_settings().get('commit_scope', 'file'))
		self.rootDir = self.get_scoped_path('repo')

		if showHistory:
			self.messageList = gitHistory.get_history(includeNewLogOption = True)
			sublime.active_window().show_quick_panel(self.messageList, self.sel_message)
		else:
			message = gitHistory.get_history(getLast = True)
			if len(message) == 0:
				self.new_message()
			else:
				self.do_commit(message)




	def sel_message(self, index):
		try:
			message = self.messageList[index]

			if index == -1:
				pass
			elif message == 'New Log':
				self.new_message()
			else:
				self.do_commit(message)

		except ValueError:
			pass


	def new_message(self):
		sublime.active_window().show_input_panel("Ticket number:", "", self.on_ticket, None, None)

	def on_ticket(self, text):
		try:
			self.ticketNo = text

			sublime.active_window().show_input_panel("Comment:", "", self.on_comment, None, None)
		except ValueError:
			pass

	def on_comment(self, text):
		message = "#" + self.ticketNo + ": " + text
		self.do_commit(message)

	def do_commit(self, message):
		self.run_git_command(["git", "commit", "-m", message, self.path], self.rootDir)
		gitHistory.add_history(message)

		if git_settings().get('auto_push_after_commit', True):
			sublime.active_window().run_command("git_push")

