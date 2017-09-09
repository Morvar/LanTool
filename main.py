import sys

#options = {"List projects":"list", "Open project":"open", "Create new project":"new", "Delete project":"delete", "Exit <appname>":"exit"}

def list_projects():
	print("here's a list of your projects")

def open_project():
	print("project <projectname> was opened")

def create_project():
	print("project <projectname> was created")

def delete_project():
	print("project <projectname> was deleted")

def exit_application():
	print("exiting application now cya")
	sys.exit(0)

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

if __name__ == "__main__":
	print("Welcome to <app>!")
	print("")
	print("List projects		(list)")
	print("Open project 		(open <projectname>)")
	print("Create new project 	(new <projectname>)")
	print("Delete project 		(delete <projectname>)")
	print("Exit <appname> 		(exit)")
	print("")

	while True:
		i = input(" > ")
		on_input(i)

	sys.exit(0)
