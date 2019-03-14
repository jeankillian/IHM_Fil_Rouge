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


@route('/statperday/<machine>')
def last_game_result(machine):
    return '<h1>statperday page<h1>'


@route('/log/<machine>')
def last_game_result(machine):
    templateroute = './log.tpl'
    recupdata = m.ReceivedMessage.liste_msg_per_marchine(machine)
    liste = []
    for obj in recupdata:
        liste.append(obj)
    return template('./my_page', liste=liste, tempdata=templateroute, machine=machine)


@route('/statpergame/<machine>')
def last_game_result(machine):
    return '<h1>statpergame page<h1>'


@route('/')
def index():
    return '<h1>nothing_here<h1>'


if __name__ == '__main__':
    run(debug=True, reloader=True)
