# coding: utf-8
import constants
import utils
from collections import OrderedDict
from scene import Scene
from editmode import initialized_edit_mode
import os

def initialized_main_menu():
	#specify the title
	title = "Main Menu"

	#specify the functions
	def list_projects(scene, args):
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

	def create_project(scene, args):
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
	def open_project(scene, args):
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
		if not project_path:
			print(f"Could not find project {project_name}")
			return
		edit_mode = initialized_edit_mode(project_path)
		print("Opening project " + project_name + "... ")
		edit_mode.enter()
		# is drawing scene a sane thing to do here?
		scene.draw()
		return

	def delete_project(scene, args):
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

	def exit_mainmenu(scene, args):
		return False

	#specify the commands and which functions they will use
	commands = OrderedDict()
	commands["list"] = ("List projects", list_projects)
	commands["new"] = ("Create new project", create_project)
	commands["open"] = ("Open project", open_project)
	commands["delete"] = ("Delete project", delete_project)
	commands["exit"] = ("Exit " + constants.app_name, exit_mainmenu)

	#create a main menu from the Scene class
	main_menu = Scene(title, commands)
	return main_menu
