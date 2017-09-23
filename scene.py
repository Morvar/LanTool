from collections import OrderedDict
class Scene:
	def __init__(self, title, commands = None):
		self.title = title

		if commands is None:
			self.commands = OrderedDict()
			self.commands["exit"] = ("Exit", lambda: False)
		else:
			self.commands = copy.deepcopy(commands)

		self.elements = []
		
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
		print("---------")

		l = []
		number_of_spaces = 3
		space_character = '·'
		keys = self.commands.keys()
		for key in keys:
			l.append(self.commands[key][0])
		#set m to the longest of the command names
		m = max(map(len, l))
		#calculate number of spaces to put after the name
		keys = self.commands.keys()
		for key in keys:
			s = m - len(self.commands[key][0]) + number_of_spaces
			print(self.commands[key][0] + space_character * s + "(" + key + ")")
			
		print("---------")
		print("")

	def request_input(self):
		while True:
			i = input(" > ")
			#keep going doing on_input stuff, in case the user didn't say exit which will cause on_input to return False
			if self.on_input(i) is False:
				break

	def on_input(self, i):
		keys = self.commands.keys()
		for key in keys:
			if key == i:
				#call the corresponding function
				return self.commands[key][1]()
		#if there was no matching key:
		print("Error: Unrecognized command")

	#"launch" the scene. when this function ends, the user has chosen to exit the scene
	def enter(self):
		self.draw()
		self.request_input()
		#gets here when the user has said "exit" so that on_input returned a False to request_input()
