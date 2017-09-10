from .constants import app_name

class MenuOption:
	def __init__(self, name, command):
		self.name = name
		self.command = command
		
	def draw(self, s):
		print(self.name + " " * s + "(" + self.command + ")")

class MainMenu:
	def __init__(self):
		self.menuoptions = []

	def add_menu_option(self, name, command):
		new_opt = MenuOption(name, command)
		self.menuoptions.append(new_opt)

	def draw(self):
		print("Welcome to " + app_name + "!")
		print("")
		print("---------")
		
		l = []
		for opt in self.menuoptions:
			l.append(opt.name)
		m = max(map(len, l))
		#number of spaces to put after the name
		for opt in self.menuoptions:
			s = m - len(opt.name) + 1
			opt.draw(s)
		print("---------")
		print("")

def init():
	main_menu = MainMenu()
	main_menu.add_menu_option("List projects", "list")
	main_menu.add_menu_option("Open project", "open")
	main_menu.add_menu_option("Create new project", "new")
	main_menu.add_menu_option("Delete project", "delete")
	main_menu.add_menu_option("Exit " + app_name, "exit")
	return main_menu
