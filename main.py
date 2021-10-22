# Helper script which runs the entire pipeline and handles user input,
# solving models, visualising models

from ux import num_models, param_to_file
from solver import build_and_solve_model
from dosing import build_dose
# from visualiser import multiplot

# Get number of models that the user wants to compare.
N = num_models()
filenames = []

for i in range(N):
    # Get user input to build a model.
    #current_json = param_to_file()
    current_json = '1634833362.6048021.json'

    # Transform that user input into a dosing protocol function.
    dosing_function = build_dose(current_json)

    # Use that dosing function and compartment specification to solve model.
    current_csv = build_and_solve_model(current_json, dosing_function)

    # Store which filenames we have solved in order to give them to visualiser.
    filenames.append([current_json, current_csv])

# Visualising stuff will go here

