import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

def git_settings():
	window = sublime.active_window()
	view = window.active_view()
	settings = view.settings()

	return view.settings()
	# return sublime.load_settings( 'GitTools.sublime-settings' )

def show_output_panel(outputStr, reset = False):
	window = sublime.active_window()
	output = window.get_output_panel("Git")

	output.run_command("append", {"characters": outputStr })

	window.run_command("show_panel", {"panel": "output.Git"})


class gitController():

	def get_git_root_path(self):
		path = sublime.active_window().active_view().file_name( ).split( "\\" )

		gitFound = 0
		while 0 == gitFound and 0 != len( path ):
			path = path[:-1]
			currentDir = "\\".join( path )

			if os.path.isdir( currentDir + "\\.git" ):
				return currentDir

		return ""

	def get_scoped_path(self, scope):
		filePath = sublime.active_window().active_view().file_name()
		repoPath = self.get_git_root_path()

		if scope == 'repo':
			return repoPath
		elif scope == 'file':
			return filePath
		elif scope == 'dir':
			return os.path.dirname(filePath)
		else:
			return repoPath

	def get_git_dir(self):
		try:
			self.gitDir = sublime.active_window().active_view().file_name( ).split( "\\" )

			gitFound = 0
			while 0 == gitFound and 0 != len( self.gitDir ):
				self.gitDir = self.gitDir[:-1]
				currentDir = "\\".join( self.gitDir )

				if os.path.isdir( currentDir + "\\.git" ):
					gitFound = 1

			if 0 == gitFound:
				return ""
		except:
			return ""

		return self.gitDir

	def run_git_command(self, params = [], dir = '', stripResult = True):

		# self.debug_print(message = "Running command", first = True, last = False)
		startupinfo = None
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

		# self.debug_print(message = params, first = False, last = False)

		try:
			proc = subprocess.Popen(
						params,
						cwd=dir,
						stdin=subprocess.PIPE,
						stdout=subprocess.PIPE,
						stderr=subprocess.STDOUT,
						startupinfo=startupinfo)

			cmd = proc.communicate()

		except ValueError:
			self.debug_print(message = ValueError, first = False, last = False)
			sublime.status_message( "Git command failed." )
			return ""


		# self.debug_print(message = cmd, first = False, last = False)
		# self.debug_print(message = "Running Done", first = False, last = True)
		return cmd[0].decode()

	def debug_print(self, message = "", first = False, last = False):
		if first:
			print("==========================")

		print(message)

		if last:
			print("==========================")
