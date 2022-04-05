import statsapi as mlb

def careerstats():
    player = input('What is the full name of the player? ')
    stat = input('Hitting/Pitching/Fielding? ').lower()
    year = input('What is one of the year\s that ' + player + ' played in? ')
    playerid = mlb.lookup_player(player)[0]['id']
    print('\n\n' + mlb.player_stats(playerid, stat, 'career'))

def careerleaders():
    want = input('Which stat do you want to find the all-time leaders of? ').lower()
    top = input('Top how many players? ')

    # batting stats
    if want == 'home runs':
        stat = 'homeRuns'
        group = 'hitting'
    if want == 'hits':
        stat = 'hits'
        group = 'hitting'
    if want == 'doubles':
        stat = 'doubles'
        group = 'hitting'
    if want == 'runs':
        stat = 'runs'
        group = 'hitting'
    if want == 'batting average':
        stat = 'avg'
        group = 'hitting'
    if want == 'stolen bases':
        stat = 'stolenBases'
        group = 'hitting'
    if want == 'rbis':
        stat = 'rbi'
        group = 'hitting'

    if want == 'wins':
        stat = 'wins'
        group = 'pitching'
    if want == 'era':
        stat = 'era'
        group = 'pitching'
    if want == 'innings pitched':
        stat = 'inningsPitched'
        group = 'pitching'
    if want == 'losses':
        stat = 'losses'
        group = 'pitching'
    if want == 'saves':
        stat = 'saves'
        group = 'pitching'
    if want == 'strikeouts':
        stat = 'strikeOuts'
        group = 'pitching'
    if want == 'Walks':
        stat = 'baseOnBalls'
        group = 'pitching'

    print('\n\n' + mlb.league_leaders(stat ,statGroup=group,statType='career',limit=top))