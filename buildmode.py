from collections import OrderedDict
from scene import Scene
def initialized_build_mode():
	#specify the title
	title = "Build Mode"

	#specify the functions
	def add_piece(scene):
		pass

	def remove_piece(scene):
		pass

	def move_piece(scene):
		pass

	def edit_piece(scene):
		pass

	def duplicate_piece(scene):
		pass

	def save_workspace(scene):
		pass

	def exit_buildmode(scene):
		while True:
			print("Do you want to exit " + title + "? (yes/no)")
			i = input(" > ")
			if i == "yes":
				return False
			if i == "no":
				break
			else:
				print("Error: Unrecognized command")

	#specify the commands and which functions they will use
	commands = OrderedDict()
	commands["add"] = ("Add", add_piece)
	commands["search"] = ("remove", remove_piece)
	commands["edit"] = ("move", move_piece)
	commands["edit"] = ("edit", edit_piece)
	commands["add"] = ("duplicate", duplicate_piece)
	commands["save"] = ("Save workspace", save_workspace)
	commands["exit"] = ("Exit", exit_buildmode)

	#create an edit mode from the Scene class
	build_mode = Scene(title, commands)
	return build_mode
