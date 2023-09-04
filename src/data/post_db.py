import pandas as pd

def add_cols_to_df(df: pd.DataFrame) -> pd.DataFrame:
    df['full_name'] = df['first_name'].map(str)+' '+df['last_name'].map(str)
    df['identifier'] = df['first_name'].map(str)+'-'+df['last_name'].map(str)+'-'+df['team'].map(str) 
    return df

def list_of_unique_player_teams(df: pd.DataFrame) -> list:
    unique_player_teams: list = df['identifier'].unique()
    return unique_player_teams

def create_cleaned_player_df(df: pd.DataFrame, unique_player_teams: list) -> pd.DataFrame:
    cleaned_df = pd.DataFrame(columns=['name', 'team', 'first_season', 'last_season'])

    for player_team in unique_player_teams:
        split_player = player_team.split('-')
        team = split_player[-1]
        name = f'{split_player[0]} {split_player[1]}'
        temp_df = df[df['identifier'] == player_team]
        first_season = temp_df['season'].min()
        last_season = temp_df['season'].max()
        new_row = [name, team, first_season, last_season]
        cleaned_df.loc[len(cleaned_df)] = new_row

    sorted_df = cleaned_df.sort_values(['name'])
    return sorted_df

def main():
    players = [{'first_name': 'Patson', 'last_name': 'Daka', 'team': 'Leicester', 'season': 2021}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team': 'Arsenal', 'season': 2021}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team': 'Wolves', 'season': 2021}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team': 'Everton', 'season': 1999},
           {'first_name': 'Patson', 'last_name': 'Daka', 'team': 'Leicester', 'season': 2020}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team': 'Arsenal', 'season': 2015}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team': 'Everton', 'season': 2004}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team': 'Everton', 'season': 1996},
           {'first_name': 'Patson', 'last_name': 'Daka', 'team': 'Leicester', 'season': 2019}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team': 'Tottenham', 'season': 2010}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team': 'Everton', 'season': 2003}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team': 'Liverpool', 'season': 1995},
           {'first_name': 'Patson', 'last_name': 'Daka', 'team': 'Chelsea', 'season': 1995}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team': 'Tottenham', 'season': 2005}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team': 'Everton', 'season': 2003}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team': 'Liverpool', 'season': 1993}]

    df = pd.DataFrame(players)
    player_df = add_cols_to_df(df)
    unique_player_teams = list_of_unique_player_teams(df)
    cleaned_df = create_cleaned_player_df(player_df, unique_player_teams)
    return cleaned_df

if __name__ == "__main__":
    cleaned_df = main()
    print(cleaned_df)