[![Install Dependencies and Run Unit Tests](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/run-unittests.yml/badge.svg)](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/run-unittests.yml)
[![Check Systems Compatability](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/check-systems-compat.yml/badge.svg)](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/check-systems-compat.yml)
[![Lint with flake8](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/run-flake8.yml/badge.svg)](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/run-flake8.yml)
[![codecov](https://codecov.io/gh/Software-Engineering-BBSRC-Group-6/PK_modelling/branch/main/graph/badge.svg?token=gdzMuuonBd)](https://codecov.io/gh/Software-Engineering-BBSRC-Group-6/PK_modelling)
[![Documentation Status](https://readthedocs.org/projects/pk-proj/badge/?version=latest)](https://pk-proj.readthedocs.io/en/latest/?badge=latest)
# Pharmacokinetic Modelling Group Project

A PharmacoKinetic (PK) modelling function for analysis of injected solute dynamics over time, developed by Group 6 of the 2021 Software Engineering course. This model has been developed with the end-user in mind, and includes an easy-to-use interface to guide refinement of tissue models.

https://software-engineering-bbsrc-group-6.github.io/PK_modelling/

# Authors

Amit Halkhoree - amit.halkhoree@dtc.ox.ac.uk \
Cameron Anderson - cameron.anderson@dtc.ox.ac.uk \
Dan Hudson - alexander.hudson@dtc.ox.ac.uk \
Ishaan Kapoor - ishaan.kapoor@dtc.ox.ac.uk \
Joseph Pollacco - joseph.pollacco@dtc.ox.ac.uk \
Samuel Johnson - samuel.johnson@dtc.ox.ac.uk

# Background
Ref: https://sabs-r3.github.io/software-engineering-projects/01-introduction/index.html.

The field of Pharmacokinetics (PK) provides a quantitative basis for describing the delivery of a drug to a patient, the diffusion of that drug through the plasma/body tissue, and the subsequent clearance of the drug from the patient’s system. PK is used to ensure that there is sufficient concentration of the drug to maintain the required efficacy of the drug, while ensuring that the concentration levels remain below the toxic threshold. Pharmacokinetic (PK) models are often combined with Pharmacodynamic (PD) models, which model the positive effects of the drug, such as the binding of a drug to the biological target, and/or undesirable side effects, to form a full PKPD model of the drug-body interaction. This project will only focus on PK, neglecting the interaction with a PD model.

![alt text](https://sabs-r3.github.io/software-engineering-projects/fig/pk1.jpg)
# Model overview

Our model consists of three principal modules:
- A solver (solver.py) that computes the distribution of solute in different tissue compartments over time, given input parameters including the number of compartments to model, dose,  mode of administration  (intravenous or subcutaneous), compartment volume and transition rate constants.
- A user interface (ux.py) that prompts the user to configure the model
- A visualisation module (visualiser.py) that generates and saves comparative plots to facilitate evaluation of PK using different administration methods.

# Folder structure

This repository includes the following key files/folders:

- .github/workflows: directory of github actions ensuring continuous integration (CI) of repository updates 
- data: directory for saving outputs
- docs: files required for automated document production
- jsons: directory for saving user input and passing to the solver
- pk_model: directory for main executables
    - definitons.py: Key helper functions for the solver
    - dosing.py: computes dose changes for different administration models
    - solver.py: Solver model for PK modelling
    - ux.py: User interface executable
    - visualiser.py Graph plotting function
- README.md: text file populating this guide
- tests: unit tests fed to pytest for continuous integration
- venv: virtual environment including dependencies for this package
- .gitignore: file controlling which files are/are not updated by git during development
- requirements.txt: Dependencies required for proper package functioning

# Installation

The project can be installed via pip: `pip install pkproject-8` CHECK
To execute the file, navigate to the root directory of the pk_modelling folder in terminal and enter the following:
`python -m pk_model_main_pipeline.py`

# Runtime

The model will then pose a series of questions, to be answered using the command line. An example runscript is provided below:

How many models would you like to test? 1 /
What kind of models do you want to build? (intravenous bolous (ib) / subcutaneous (sc)): ib
What compound or drug are you using? paracetamol
How is the dose delivered? Constantly over time (c), Instantaneously (i) or Repeated instantaneous doses (r): c
What is the dose of paracetamol that you want to test? (units in ng per hour): 500
What time period would you like to simluate the model? (units in hours): 48
What interval time would you like in the simulation? (units in hours): 1
What is the clearance rate? (units in ng/hour): 50
Enter volume (L), transition rate (ng/hour) for the main compartment (all seperated by spaces - eg: 5 25 ): 7 50
How many peripheral compartments do you want to test?: 1
Enter volume (L), transition rate (ng/hour) of the compartment (all seperated by spaces - eg: 5 25): 2 10
Please enter the name of the compartment (please ensure correct spelling): heart
Would you like to generate a graph? (Y/N): y

This should produce a plot of the distribution of paracetamol between the main compartment and the heart, and save the resulting figure in data/xxx.



