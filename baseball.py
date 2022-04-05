from functions import careerstats, careerleaders

print('\n\nWelcome to Danny\'s MLB Stat Exchange! Learn more about baseball through career stats, career leaders, etc !\n')
user = input('\nWhat statistic do you want to find today? ')

if user == 'career stats':
    careerstats()
if user == 'career leaders':
    print('\nFor hitting, we are able to find the career leaders for home runs, batting average, runs, hits, RBIs, doubles, and stolen bases.')
    print('\nFor pitching, we are able to find the career leaders for wins, losses, saves, era, innings pitched, strikeouts, and walks.\n')
    careerleaders()