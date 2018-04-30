import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

from ..Core.Controller import *


def git_history():
	return sublime.load_settings( 'GitMessageHistory.sublime-settings' )

class gitHistory():
	def get_history(includeNewLogOption = False, newLogText = 'New Log', getLast = False):
		messageHistory = list(git_history().get('history', []))
		if includeNewLogOption:
			messageHistory.insert(min(len(messageHistory), 1), newLogText)
		if getLast:
			if len(messageHistory) == 0:
				messageHistory = ''
			else:
				messageHistory = messageHistory[0]
		return messageHistory

	def add_history(log):
		history = git_history().get('history', [])

		for item in list(history):
			if item == log:
				history.remove(item)

		history.reverse()
		history.append(log)
		history.reverse()
		git_history().set('history', history)
		sublime.save_settings('GitMessageHistory.sublime-settings')



