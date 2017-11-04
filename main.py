#!/usr/bin/env python
# coding: utf-8
import sys
from mainmenu import initialized_main_menu
from constants import app_name
from scene import Scene

def exit_application():
	while True:
		print("Do you want to exit " + app_name + "? (yes/no)")
		i = input(" > ")
		if i == "yes":
			print("Exiting " + app_name + " now. Cya!")
			sys.exit(0)
		if i == "no":
			break
		else:
			print("Error: Unrecognized command")

# this is the ENTRY POINT
if __name__ == "__main__":
	print("Welcome to " + app_name + "!")
	
	main_menu = initialized_main_menu()
	while True:
		main_menu.enter()
		# when main menu returns, the user has chosen to exit the application
		exit_application()


