import os
import re
from functions import int_input, rreplace



#verif exo
if os.path.isdir(f"{os.curdir}/kwyk-solver/solvers/"):
    solvers_directory_path = f"{os.curdir}/kwyk-solver/solvers/"
else:
    solvers_directory_path = f"{os.curdir}/solvers/"

#affichage exo
supported_ex = []
solver_filename_pattern = "solver_([0123456789]+)\.py"
for file in os.listdir(solvers_directory_path):
    solver_filename_match = re.match(solver_filename_pattern, file)
    if solver_filename_match:
        #recuperation fichier
        supported_ex.append(int(solver_filename_match.group(1)))
# On trie la liste dans l'ordre croissant et on l'affiche à l'utilisateur.
supported_ex.sort()
supported_ex_string = rreplace(str(supported_ex), ',', ' et', 1)[1:-1]
print(f"\nExercices supportés : {supported_ex_string}.")


prompt = "Entrez le numéro de l'exercice : "
separator = f"\n{'-' * (len(prompt) - 1)}\n"

while True:
    print(separator)
    ex = int_input(prompt)
    print()
    if ex in supported_ex:
        try:
            exec(f"from solvers import solver_{ex}")
            exec(f"solver_{ex}.solve()")
        except Exception as e:
            print(f"(!) Une erreur est survenue : {str(e)}.")
    else:
        print("(!) Exercice non supporté par le solveur.")
