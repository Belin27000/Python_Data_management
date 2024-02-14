"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""

from pathlib import Path
from pprint import pprint

prenom = Path("/Users/yannlecerf/OneDriveLocal/Documents/Formation DEV/Python/la-formation-complete-python-master/prj-009_organiser-des-donnees/01-sources/prenoms.txt")

New_list = Path("/Users/yannlecerf/OneDriveLocal/Documents/Formation DEV/Python/la-formation-complete-python-master/prj-009_organiser-des-donnees/01-sources")

with open(prenom,"r") as f:
    lines=f.read().splitlines()

pprint(lines)

prenoms =[]
for line in lines:
    prenoms.extend(line.split())
prenoms_final = [prenom.strip(",. ") for prenom in prenoms]
pprint(prenoms_final)


final_name = Path(New_list) / "prenom_final.txt"
with open( final_name,"w") as f:
    f.write("\n".join(sorted(prenoms_final)))

