from constants import app_name
from utils import project_entries, new_projectfile, remove_projectfile
from collections import OrderedDict
from scene import Scene
from editmode import initialized_edit_mode
import os

def initialized_main_menu():
	#specify the title
	title = "Main Menu"

	#specify the functions
	def list_projects(scene, args):
		print("Here's a list of your projects: ")
		print("---------")
		entries = project_entries()
		for file in entries:
			print("▪ " + file)
		print("---------")

	def create_project(scene, args):
		file = new_projectfile()
		print("Project " + file.name + " was created")

	# the way to edit mode
	def open_project(scene, args):
		print("Opening <projectname>")
		edit_mode = initialized_edit_mode()
		while True:
			edit_mode.enter()
			# is this a sane thing to do here?
			scene.draw()
			break

	def delete_project(scene, args):
		#glfödf
		if remove_projectfile(file_name):
			print(file_name + " was deleted")
		else:
			print(file_name + " was not deleted")

	def exit_mainmenu(scene, args):
		return False

	#specify the commands and which functions they will use
	commands = OrderedDict()
	commands["list"] = ("List projects", list_projects)
	commands["new"] = ("Create new project", create_project)
	commands["open"] = ("Open project", open_project)
	commands["delete"] = ("Delete project", delete_project)
	commands["exit"] = ("Exit " + app_name, exit_mainmenu)

	#create a main menu from the Scene class
	main_menu = Scene(title, commands)
	return main_menu
