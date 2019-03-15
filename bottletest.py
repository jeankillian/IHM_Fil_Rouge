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
    return '<h1>lastgameresult page<h1>'


@route('/configuration/<machine>')
def configuration(machine):

    return '<h1>configuration page of ' + machine + '<h1>'


@route('/statperday')
def stat_per_day():
    templateroute = './stat_per_day.tpl'
    recupdata = m.StatsPerDay.liste_stat_per_marchine()
    liste = []
    for obj in recupdata:
        liste.append(obj)
    return template('./test_stat_per_day', liste=liste, tempdata=templateroute)


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
