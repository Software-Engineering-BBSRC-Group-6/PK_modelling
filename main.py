# Helper script which runs the entire pipeline and handles user input,
# solving models, visualising models

from ux import num_models, param_to_file
from solver import build_and_solve_model
from visualiser import multiplot

# Get number of models that the user wants to compare
N = num_models()
filenames = []

for i in range(N):
    current_json = param_to_file()
    current_csv = build_and_solve_model(current_json)
    filenames.append([current_json, current_csv])

# Visualising stuff will go here

