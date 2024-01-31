import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="laplateforme"
)

curseur = connexion.cursor()

requete_sql = "SELECT nom, capacite FROM salle"
curseur.execute(requete_sql)

resultats = curseur.fetchall()

for resultat in resultats:
    nom, capacite = resultat
    print(f"Nom: {nom}, Capacité: {capacite}")

curseur.close()
connexion.close()
