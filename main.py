import sys
from mainmenu import enter_mainmenu
from constants import app_name

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

if __name__ == "__main__":
	while True:
		enter_mainmenu()
		# when main menu returns, the user has chosen to exit the application
		exit_application()


