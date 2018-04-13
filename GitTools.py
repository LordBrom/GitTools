import sublime
import sublime_plugin
import os.path
import subprocess
import functools
import datetime

from .Core.Controller import *
# from .Core.SetStatusItems import *

from .Commands.gitCommit import *
from .Commands.gitPush import *
from .Commands.gitDiff import *
from .Commands.gitLog import *


def plugin_loaded():
	print("this is a test")