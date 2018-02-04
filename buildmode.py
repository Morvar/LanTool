# coding: utf-8
from collections import OrderedDict
from scene import Scene, command

class BuildMode(Scene):
	def __init__(self):
		#construct a scene
		super().__init__("Build Mode")

	#specify the functions
	@command("add", "Add piece")
	def add_piece(self, args):
		pass

	@command("rem", "Remove piece")
	def remove_piece(self, args):
		pass

	@command("move", "Move piece")
	def move_piece(self, args):
		pass

	@command("edit", "Edit piece")
	def edit_piece(self, args):
		pass

	@command("dup", "Duplicate piece")
	def duplicate_piece(self, args):
		pass

	@command("save", "Save workspace")
	def save_workspace(self, args):
		pass

	@command("exit", "Exit")
	def exit_buildmode(self, args):
		while True:
			print("Do you want to exit " + self.title + "? (yes/no)")
			i = input(" > ")
			if i == "yes":
				return False
			if i == "no":
				break
			else:
				print("Error: Unrecognized command")
