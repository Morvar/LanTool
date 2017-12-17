# coding: utf-8
from collections import OrderedDict
from copy import deepcopy
import utils
import constants
class Scene:
	def __init__(self, title, commands = None):
		self.title = title

		if commands is None:
			self.commands = OrderedDict()
			self.commands["exit"] = ("Exit", lambda: False)
		else:
			self.commands = deepcopy(commands)

		self.elements = []

	def add_element(self, new_element):
		self.elements.append(new_element)

	#draw the scene by drawing all the elements
	def draw(self):
		#draw the title of the scene
		print("")
		print(self.title)

		#draw each element
		for element in self.elements:
			element.draw()

		#draw the list of available commands
		self.draw_commands()

	def draw_commands(self):
		print("")
		list_of_names = []
		list_of_commands = []
		number_of_middle_spaces = 3
		space_character = '·'
		keys = self.commands.keys()
		for key in keys:
			list_of_names.append(self.commands[key][0])
			list_of_commands.append(key)
		#set max to the longest of the command names
		max_left = max(map(len, list_of_names))
		max_right = max(map(len, list_of_commands))
		#calculate number of spaces to put after the name
		keys = self.commands.keys()
		for key in keys:
			number_of_left_spaces = max_left - len(self.commands[key][0])
			number_of_right_spaces = max_right - len(key)
			print(self.commands[key][0] + space_character * number_of_left_spaces \
			+ space_character * number_of_middle_spaces \
			+ space_character * number_of_right_spaces + "(" + key + ")")
		print("")

	def request_input(self):
		while True:
			i = input(constants.input_prompt)
			#keep going doing on_input stuff, in case the user didn't say exit which will cause on_input to return False
			if self.on_input(i) is False:
				break

	def on_input(self, i):
		#if used only pressed enter, draw the commands
		if not i:
			self.draw_commands()
		# string -> list
		input_args = i.split()
		if not input_args: return True
		#define the command as the first of the received arguments
		input_command = input_args[0]
		#put the rest of the arguments in a list to send along
		tail_args = input_args[1:]
		try:
			#call the corresponding function
			command_function = self.commands[input_command][1]
		except KeyError:
			#if there was no matching key:
			utils.print_unrecognized_command(input_command)
		else:
			if constants.debug:
				print("(debug from scene) Input: ", input_args[0], tail_args)
			return command_function(self, tail_args)

	#"launch" the scene. when this function ends, the user has chosen to exit the scene
	def enter(self):
		self.draw()
		self.request_input()
		#gets here when the user has said "exit" so that on_input returned a False to request_input()
