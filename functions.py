from msilib.schema import Error
import statsapi as mlb

def careerstats():
    # find playerid 
    while True:
        try:
            player = input('\nWhat is the full name of the player? ')
            stat = input('\nHitting/Pitching/Fielding? ').lower()
            playerid = mlb.lookup_player(player)[0]['id']
            break
        except IndexError:
            print('\nPlayer does not exist. Please input another name.')
    # api call
    print('\n\n' + mlb.player_stats(playerid, stat, 'career'))

def careerleaders():
    # ask for what type of stats and top #
    while True:
        want = input('\nWhich stat do you want to find the all-time leaders of? ').lower()
        top = input('\nTop how many players? ')
        stats = ['home runs', 'batting average', 'runs', 'hits', 'rbis', 'doubles', 'stolen bases', 'wins', 'losses', 
        'saves', 'era', 'innings pitched', 'strikeouts', 'walks']
        if want in stats:
            break
        else:
            print('\nPlease input a valid stat from the list')

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

    # pitching stats
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
    
    # display ranking
    print('\n\n' + mlb.league_leaders(stat ,statGroup=group,statType='career',limit=top))

def leaguestanding():
    # specify which league and date
    while True:
        league = input('\nAmerican League or National League? ').lower()
        date = input('\nFrom which date (MM/DD/YYYY)? ')
        if league == 'american league':
            leagueId = 103
            break
        if league == 'national league':
            leagueId = 104
            break
        else:
            print('\nLeague has to be either American League or National League')

    # display standings
    print('\n\n' + mlb.standings(leagueId=leagueId,date=date))


def currentseason():
    # ask for player
    while True:
        try:
            player = input('\nWhat is the full name of the player? ')
            stat = input('\nHitting/Pitching/Fielding? ').lower()
            playerid = mlb.lookup_player(player)[0]['id']
            break
        except IndexError:
            print('\nPlayer does not exist. Please input another name.')
    
    # display that player's current season stats
    print('\n\n' + mlb.player_stats(playerid, stat, 'season'))

def lastgame():
    # ask for team and whether you want highlights or box score
    while True:
        try:
            team = input('\nWhich team would you like the last game information of? ')
            choice = input('\nWould you like the highlights or the box score from the last game? ')
            teamid = mlb.lookup_team(team)[0]['id']
            break
        except IndexError:
            print('\nPlayer does not exist. Please input another name.')
    gameid = mlb.last_game(teamid)

    # display what the user asked for
    if choice == 'box score':
        print('\n\n' + mlb.boxscore(gameid))
    if choice == 'highlights':
        print('\n\n' + mlb.game_highlights(gameid))

def teamroster():
    # ask for team
    while True:
        try:
            team = input('\nWhich team would you like the roster for? ')
            teamid = mlb.lookup_team(team)[0]['id']
            break
        except IndexError:
            print('\nTeam does not exist. Please input another name.')

    # display team roster
    print('\n\n' + mlb.roster(teamid)) 