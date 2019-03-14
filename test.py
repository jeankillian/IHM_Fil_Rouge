import models as m

ratatouille = m.GameServers.liste_serveur()
liste = []
for s in ratatouille:
    liste.append(s)

print(liste[0].nom)