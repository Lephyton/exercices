# exercices
Tous les exercices ci-dessous vont utiliser le fichier en pièce-jointe "MOCK_DATA.csv".
Essaye de faire en sorte de créer des fonctions que tu puisses réutiliser au fil des exercices (une fonction qui te permet de lire un fichier par exemple etc...)?

Si jamais tu as un problème avec un exercice n'hésite pas à me le dire. Si c'est trop compliqué ou trop simple aussi. J'espère que les énoncés sont assez clairs. Si tu as une incompréhension, n'hésite pas à me le remonter !

Le fichier se présente de la manière suivante : 
Format CSV
Une liste de personnes : prénom, nom, email, genre, adresse ip
Un entête qui décrit les différentes colonnes
Les colonnes sont séparées par des virgules
Exercice 1

Écrire un script qui lit le fichier CSV et affiche les 30 premières personnes en respectant le format suivant :

Taylor Fahrenbacher est le contact n°1. Il s'agit d'un Homme.
Rochella Jerke est le contact n°2. Il s'agit d'une Femme.
          etc... jusqu'à la 30ème personne


Exercice 2

Écrire un script qui lit le fichier CSV et qui écrit dans un deuxième fichier uniquement les contacts masculins. Tu peux écrire le deuxième fichier en suivant le même format CSV utilisé dans le fichier MOCK_DATA.csv

Exercice 3

Écrire un script qui lit le fichier CSV et qui écrit dans un deuxième fichier uniquement les contacts féminins en les classant par ordre alphabétique des emails.Tu peux écrire le deuxième fichier en suivant le même format CSV utilisé dans le fichier MOCK_DATA.csv

Exercice 4

Reprend le code de l'exercice 1 mais cette fois utilise le module CSV de Python pour traiter les données : https://docs.python.org/3/library/csv.html 
Bon exercice pour te faire manipuler la doc python et commencer à utiliser les modules de la librairie standard.

Exercice 5

Toujours en utilisant le module CSV de Python, écrire un script qui permet de filtrer la liste des personnes en passant des paramètres. Pour cela tu devras utiliser le module argparse de Python (https://docs.python.org/3/library/argparse.html)

Par exemple, pour n'afficher que les hommes de la liste :
python ton_script.py --genre=male

Ou encore pour limiter le nombre de résultats
python ton_script.py --gender=male --max-results=50

Ou bien pour chercher par le nom ou le prenom
python ton_script.py --name=Forest


Cordialement,

-- 
Dimitri SÉGARD
