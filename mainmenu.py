from constants import app_name
from utils import list_project_entries
import sys
class MenuOption:
	def __init__(self, name, command):
		self.name = name
		self.command = command
		
	def draw(self, s):
		print(self.name + " " * s + "(" + self.command + ")")

class Menu:
	def __init__(self, options):
		self.menuoptions = []
		print(options)

		for name, command in options:
			self.add_menu_option(name, command)

	def add_menu_option(self, name, command):
		new_opt = MenuOption(name, command)
		self.menuoptions.append(new_opt)

	def draw(self):
		l = []
		for opt in self.menuoptions:
			l.append(opt.name)
		m = max(map(len, l))
		#number of spaces to put after the name
		for opt in self.menuoptions:
			s = m - len(opt.name) + 1
			opt.draw(s)

class MainMenu(Menu):
	def __init__(self):
		options = [("List projects", "list"),("Open project", "open"),("Create new project", "new"),("Delete project", "delete"),("Exit " + app_name, "exit")]
		super().__init__(options)

	def draw(self):
		print("Welcome to " + app_name + "!")
		print("")
		print("---------")
		super().draw()
		print("---------")
		print("")

	def show(self):
		self.draw()
		while True:
			i = input(" > ")
			on_input(i)
#______________
def list_projects():
	print("Here's a list of your projects: ")
	print("---------")
	list_project_entries()
	print("---------")

def open_project():
	print("Project <projectname> was opened")

def create_project():
	print("Project <projectname> was created")

def delete_project():
	print("Project <projectname> was deleted")

def exit_application():
	print("Exiting " + app_name + " now. Cya!")
	print("this exit is done from mainmenu and that should probably be changed")
	sys.exit(0)
#______________
def on_input(input):
	if input == "list":
		list_projects()
		
	elif input == "open":
		open_project()
		
	elif input == "new":
		create_project()
		
	elif input == "delete":
		delete_project()
		
	elif input == "exit":
		exit_application()
		
	else:
		print("Error: Unrecognized command")
