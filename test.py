import models as m

ratatouille = m.GameServers.liste_serveur()
liste = []
for s in ratatouille:
    liste.append(s)

print(liste[0].nom)

recupdata = m.StatsPerDay.liste_stat_per_marchine()
print(recupdata)
liste = []
for obj in recupdata:
    liste.append(obj)
    print(obj.moyenne_partie)
