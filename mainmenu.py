from constants import app_name
from utils import project_entries, new_projectfile
from collections import OrderedDict
from scene import Scene
from editmode import initialized_edit_mode

def initialized_main_menu():
	#specify the title
	title = "Main Menu"

	#specify the functions
	def list_projects():
		print("Here's a list of your projects: ")
		print("---------")
		entries = project_entries()
		for file in entries:
			print("▪ " + file)
		print("---------")

	def create_project():
		file = new_projectfile()
		print("Project " + file.name + " was created")

	# the way to edit mode
	def open_project():
		print("Project <projectname> was opened")
		edit_mode = initialized_edit_mode()
		while True:
			edit_mode.enter()
			print("draw the main menu here again? because now the edit_mode.enter() has returned, so we're in main menu again")
			break

	def delete_project():
		print("Project <projectname> was deleted")

	def exit_mainmenu():
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
