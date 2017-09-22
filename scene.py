from collections import OrderedDict
from mainmenu import Menu
class Scene:
	
	def __init__(self, name):
		self.name = name
		self.commands = OrderedDict()
		self.commands["exit"] = ("Exit", lambda: False)
		#self.menu = Menu() #use this or not? double storing the commands is not a great idea. both in the commands dict, and the menu element
		self.elements = []
		
	#draw the scene by drawing all the elements
	def draw(self):
		for element in self.elements:
			element.draw()
		self.draw_commands()

	def draw_commands(self):
		l = []
		keys = self.commands.keys()
		for key in keys:
			l.append(self.commands[key][0])
		#set m to the longest of the command names
		m = max(map(len, l))
		#calculate number of spaces to put after the name
		keys = self.commands.keys()
		for key in keys:
			s = m - len(self.commands[key][0]) + 1
			print(self.commands[key][0] + " " * s + "(" + key + ")")

	#"launch" the scene. when this function ends, the user has chosen to exit the scene
	def enter(self):
		self.draw()
		self.request_input()
		#gets here when the user has said "exit" so that on_input returned a False to request_input()

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
		print("Error: Unrecognized command")
