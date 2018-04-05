import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

def git_settings():
	return sublime.load_settings( 'GitTools.sublime-settings' )

def show_output_panel(outputStr):
    window = sublime.active_window()
    output = window.get_output_panel("Git")

    output.run_command("insert", {"characters": outputStr})
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
		print("Running command")
		startupinfo = None
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

		print(params)

		try:
			proc = subprocess.Popen(
						params,
						cwd=dir,
						stdin=subprocess.PIPE,
						stdout=subprocess.PIPE,
						stderr=subprocess.STDOUT,
						startupinfo=startupinfo)

		except ValueError:
			print(ValueError)
			sublime.status_message( "Git command failed." )
			return ""

		print(proc.communicate())
		print("Running Done")
		return proc.communicate()[0].decode()