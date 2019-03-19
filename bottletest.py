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
    recupdata = m.GameServers.config(machine)
    templateroute = './configuration.html'
    return template('./my_page', item=recupdata, machine=machine, tempdata=templateroute)


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
    templateroute = './statpergame.tpl'
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
    config = m.GameServers.get(m.GameServers.nom == machine)
    templateroute = './modifconfig.html'
    return template('./my_page', tempdata=templateroute, config=config)


@post('/modifconfig/<machine>')
def modifconfig(machine):
    print(dict(request.forms))
    config = m.GameServers.get(m.GameServers.nom == machine)
    config.adresse_ip = request.forms.get("adresse_ip")
    config.jeu = request.forms.get("jeu")
    config.max_player_delay = request.forms.get('max_player_delay')
    config.max_coin_blink_delay = request.forms.get('max_coin_blink_delay')
    config.victory_blink_delay = request.forms.get('victory_blink_delay')
    config.level = request.forms.get('level')
    config.player_1_color = request.forms.get('player_1_color')
    config.player_2_color = request.forms.get('player_2_color')
    print(type(config.player_1_color))
    print(type(config.player_2_color))
    config.save()

    return "Nouvelle configuration pour " + machine


if __name__ == '__main__':
    run(debug=True, reloader=True)
