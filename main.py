#!/usr/bin/env python
# coding: utf-8
import sys
from mainmenu import initialized_main_menu
import constants
import utils
from scene import Scene

def exit_application():
	print("Exiting " + constants.app_name + " now. Cya!")
	sys.exit(0)

def init_app():
	utils.init_project_dir()

# this is the ENTRY POINT
if __name__ == "__main__":
	#if main was run with argument 'd', enable debug mode
	if len(sys.argv) > 1 and sys.argv[1] == 'd':
		constants.debug = True
	#do necessary setup
	init_app()
	print("Welcome to " + constants.app_name + "!")
	if constants.debug: print("DEBUG MODE")
	#create a main menu and enter it
	main_menu = initialized_main_menu()
	while True:
		main_menu.enter()
		# when main menu returns, the user has chosen to exit the application
		exit_application()
