# import functions from functions.py file
from functions import careerstats, careerleaders, leaguestanding, currentseason, lastgame, teamroster

# welcome statement
print('\n\nWelcome to Danny\'s MLB Stat Exchange! Learn more about baseball through career stats, career leaders, league standings, current player stats, last game, and team rosters!\n')

while True:
    # ask for user input
    user = input('\nWhat statistic do you want to find today? ').lower()

    # call functions to display stats
    if user == 'career stats':
        careerstats()
        break

    if user == 'career leaders':
        print('\nFor hitting, we are able to find the career leaders for home runs, batting average, runs, hits, RBIs, doubles, and stolen bases.')
        print('For pitching, we are able to find the career leaders for wins, losses, saves, era, innings pitched, strikeouts, and walks.')
        careerleaders()
        break

    if user == 'league standings':
        leaguestanding()
        break

    if user == 'current player stats':
        currentseason()
        break

    if user == 'last game':
        lastgame()
        break
    
    if user == 'team rosters':
        teamroster()
        break

    # continue to ask for what they want until valid input
    else:
        print('\nPlease choose one of the available stats from the introduction message (i.e. career stats)')
        
    