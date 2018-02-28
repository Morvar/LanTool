# coding: utf-8
import constants
import utils
from collections import OrderedDict
from scene import Scene, command
from editmode import EditMode
import os

class MainMenu(Scene):
	def __init__(self):
		#construct a scene
		super().__init__("Main Menu")

	#specify the functions
	@command("list", "List projects")
	def list_projects(self, args):
		#if there were additional arguments, don't execute
		if args:
			utils.print_invalid_arg(args[0])
			return
		entries = utils.project_entries()
		if not entries:
			print("No projects were found")
			return
		print("Here's a list of your projects: ")
		print("---------")
		for entry in entries:
			print("▪ " + entry.stem)
		print("---------")

	@command("new", "Create new project")
	def create_project(self, args):
		#if there were more than one additional argument, don't execute
		if len(args) > 1:
			utils.print_invalid_arg(args[1])
			return
		#if no arguments were given, set the project name to empty
		if not args:
			file_name = ""
		else:
			file_name = args[0]
		new_file = utils.new_projectfile(file_name)
		if not new_file:
			return
		print(f"Project '{new_file.stem}' was created")

	#the way to edit mode
	@command("open", "Open project")
	def open_project(self, args):
		#if no arguments were given, don't execute
		if not args:
			utils.print_missing_arg("project name")
			return
		#if there were more than one additional argument, don't execute
		if len(args) > 1:
			utils.print_invalid_arg(args[1])
			return
		project_name = args[0]
		project_path = utils.get_project_path(project_name)
		if not project_path.exists():
			print(f"Could not find project {project_name}")
			return
		editmode = EditMode(project_path)
		print("Opening project " + project_name + "... ")
		editmode.enter()
		# is drawing scene a sane thing to do here?
		self.draw()
		return

	@command("delete", "Delete project")
	def delete_project(self, args):
		#if no arguments were given, don't execute
		if not args:
			utils.print_missing_arg("project name")
			return
		#if there were more than one additional argument, don't execute
		if len(args) > 1:
			utils.print_invalid_arg(args[1])
			return
		for file_name in args:
			if utils.remove_projectfile(file_name):
				print(f"{file_name} was deleted")
			else:
				print(f"{file_name} was not deleted")

	@command("exit", "Exit " + constants.app_name)
	def exit_mainmenu(self, args):
		return False
