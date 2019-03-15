import models as m

recupdata = m.ReceivedMessage.last_game_result()
liste = []
templateroute = './lastgameresult.tpl'
for objects in recupdata:
    liste.append(objects)
last_game = m.Data(liste[-1].message)

print(truc.msg_id)