from bottle import run , route, template


@route('/gameserver')
def gameserver():
    return '<h1>gameserver page<h1>'


@route('/lastgameresult')
def last_game_result():
    return '<h1>lastgameresult page<h1>'


@route('/configuration/<machine>')
def configuration(machine):
    return '<h1>configuration page<h1>'


@route('/statperday/<machine>')
def last_game_result(machine):
    return '<h1>statperday page<h1>'


@route('/statpergame/<machine>')
def last_game_result(machine):
    return '<h1>statpergame page<h1>'
