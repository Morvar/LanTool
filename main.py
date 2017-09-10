import sys
import os
import modules.mainmenu
from modules.constants import app_name
from modules.constants import projects_path
#______________
def list_projects():
	print("Here's a list of your projects: ")
	print("---------")
	entries = os.listdir(projects_path)
	for file in entries:
		print("▪ " + file)
	print("---------")

def open_project():
	print("Project <projectname> was opened")

def create_project():
	print("Project <projectname> was created")

def delete_project():
	print("Project <projectname> was deleted")

def exit_application():
	print("Exiting " + app_name + " now. Cya!")
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
#______________
if __name__ == "__main__":
	main_menu = modules.mainmenu.init()
	main_menu.draw()

	while True:
		i = input(" > ")
		on_input(i)

	sys.exit(0)
