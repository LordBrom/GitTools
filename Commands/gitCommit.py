import sublime
import sublime_plugin

from ..Core.Controller import *
from ..Core.History import *

class gitCommitCommand(sublime_plugin.TextCommand, gitController):
	def run(self, edit, showHistory = False, doPush = True):

		self.argDoPush = doPush

		if showHistory:
			self.messageList = gitHistory.get_history(includeNewLogOption = True)
			sublime.active_window().show_quick_panel(self.messageList, self.sel_message)
		else:
			message = gitHistory.get_history(getLast = True)
			if len(message) == 0:
				self.new_message()
			else:
				self.do_commit(message)


		self.path = self.get_git_dir()
		if len(self.path) == 0:
			return;

		self.path = self.get_scoped_path(git_settings().get('commit_scope', 'file'))
		self.dir = self.get_scoped_path('repo')

		print(self.path)
		print(self.dir)


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
		self.run_git_command(["git", "commit", "-m", message, self.dir], self.dir)
		gitHistory.add_history(message)

		if self.argDoPush:
			sublime.active_window().run_command("git_push")

