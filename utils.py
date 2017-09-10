import os
from constants import projects_path
def list_project_entries():
	entries = os.listdir(projects_path)
	for file in entries:
		print("▪ " + file)
