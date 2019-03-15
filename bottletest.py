from bottle import run, route, template
import models as m


@route('/gameserver')
def gameserver():
    templateroute = './gameserver.tpl'
    recupdata = m.GameServers.liste_serveur()
    liste = []
    for obj in recupdata:
        liste.append(obj)
    return template('./my_page', liste=liste, tempdata=templateroute)


@route('/lastgameresult')
def last_game_result():
    recupdata = m.ReceivedMessage.last_game_result()
    liste = []
    templateroute = './lastgameresult.tpl'
    for objects in recupdata:
        liste.append(objects)
    last_game = m.Data(liste[-1].message)
    return template('./my_page', last_game=last_game, tempdata=templateroute)


@route('/configuration/<machine>')
def configuration(machine):

    return '<h1>configuration page of ' + machine + '<h1>'


@route('/statperday/<machine>')
def stat_per_day(machine):
    return '<h1>statperday page<h1>'


@route('/log/<machine>')
def log_machine(machine):
    templateroute = './log.tpl'
    recupdata = m.ReceivedMessage.liste_msg_per_marchine(machine)
    liste = []
    for obj in recupdata:
        liste.append(obj)
    return template('./my_page', liste=liste, tempdata=templateroute, machine=machine)


@route('/statpergame/<machine>')
def stat_per_game(machine):
    templateroute = './StatPerGame.tpl'
    recupdata = m.StatsPerMatch.liste_game(machine)
    liste = []
    for obj in recupdata:
        liste.append(obj)
    return template('./my_page', liste=liste, tempdata=templateroute, machine=machine)


@route('/')
def index():
    return '<h1>nothing_here<h1>'


if __name__ == '__main__':
    run(debug=True, reloader=True)
