import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

from ..Core.Controller import *

class gitHistory():
	def get_history(includeNewLogOption = False, getLast = False):
		messageHistory = list(git_settings().get('history', []))
		if includeNewLogOption:
			messageHistory.insert(min(len(messageHistory), 1), 'New Log')
		if getLast:
			messageHistory = messageHistory[1]
		return messageHistory

	def add_history(log):
		history = git_settings().get('history', [])

		for item in list(history):
			if item == log:
				history.remove(item)

		history.reverse()
		history.append(log)
		history.reverse()
		git_settings().set('history', history)
		sublime.save_settings('GitTools.sublime-settings')



