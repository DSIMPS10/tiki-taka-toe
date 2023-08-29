from utils.app_objects import Team

team_names = ['Arsenal',
                'Aston Villa',
                'Bournemouth AFC',
                'Brentford',
                'Brighton & Hove Albion',
                'Burnley',
                'Chelsea',
                'Crystal Palace',
                'Everton',
                'Fulham',
                'Liverpool',
                'Luton Town',
                'Manchester City',
                'Manchester United',
                'Newcastle United',
                'Nottingham Forest',
                'Sheffield United',
                'Tottenham Hotspur',
                'West Ham United',
                'Wolverhampton Wanderers']

CURRENT_PREM_TEAMS =[Team(team_name=team, league='Premiership', country='England') for team in team_names]

print(CURRENT_PREM_TEAMS)