from bottle import run, route, template, request, post, get
import models as m


@route('/gameserver')
def gameserver():
    templateroute = './gameserver.html'
    recupdata = m.GameServers.liste_serveur()
    liste = []
    for obj in recupdata:
        liste.append(obj)
    return template('./my_page', liste=liste, tempdata=templateroute)


@route('/lastgameresult')
def last_game_result():
    recupdata = m.ReceivedMessage.last_game_result()
    liste = []
    templateroute = './lastgameresult.html'
    for objects in recupdata:
        liste.append(objects)
    last_game = m.Data(liste[-1].message)
    return template('./my_page', last_game=last_game, tempdata=templateroute)


@route('/configuration/<machine>')
def configuration(machine):
    recupdata = m.GameServers.list_config(machine)
    liste = []
    templateroute = './configuration.html'
    for objects in recupdata:
        liste.append(objects)
    return template('./my_page', liste=liste, machine=machine, tempdata=templateroute)


@route('/statperday')
def stat_per_day():
    templateroute = './stat_per_day.tpl'
    recupdata = m.StatsPerDay.liste_stat_per_marchine()
    liste = []
    for obj in recupdata:
        liste.append(obj)
    return template('./my_page', liste=liste, tempdata=templateroute)


@route('/log/<machine>')
def log_machine(machine):
    templateroute = './log.html'
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


@get('/modifconfig/<machine>')
def config(machine):
    templateroute = './modifconfig.html'
    return template('./my_page', tempdata=templateroute, machine=machine)


@post('/modifconfig/<machine>')
def modifconfig(machine):

    max_player_delay = request.forms.get('max player delay')
    max_coin_blink_delay = request.forms.get('max coin blink delay')
    victory_blink_delay = request.forms.get('victory blink delay')
    level = request.forms.get('level')
    player1_color = request.forms.get('player1_color')
    player2_color = request.forms.get('player2_color')
    print(max_player_delay)
    print(max_coin_blink_delay)
    print(victory_blink_delay)
    print(level)
    print(player1_color)
    print(player2_color)
    # query = m.GameServers.create_config(machine, adresse_ip)

    # m.GameServers.get_or_create(adresse_ip=adresse_ip, name_server=machine,
    #                                   game=game, max_player_delay=max_player_delay,
    #                                   max_coin_blink_delay=max_coin_blink_delay,
    #                                   victory_blink_delay=victory_blink_delay, level=level,
    #                                   player1_color=player1_color, player2_color=player2_color)
    return "OK"


if __name__ == '__main__':
    run(debug=True, reloader=True)
