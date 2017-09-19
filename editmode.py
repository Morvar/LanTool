def enter_editmode(filepath):
	wordlist = []

def on_input(input):
	if input == "list":
		list_projects()

	elif input == "open":
		open_project()

	elif input == "add":
		add_word()

	elif input == "save":
		save_changes()

	elif input == "exit":
		exit_editmode()

	else:
		print("Error: Unrecognized command")

def show(self):
		self.draw()
		while True:
			i = input(" > ")
			on_input(i)
def draw():
		print("Welcome to " + app_name + "!")
		print("")
		print("---------")
		super().draw()
		print("---------")
		print("")
