import pandas as pd
import TopDownHockey_Scraper.TopDownHockey_EliteProspects_Scraper as tdhepscrape
from utils import load_data

def transform_skaters(data=None):
    if data is None:
        data = load_data('skaters_data.pkl')

    # Drop redundant columns
    data = data.drop(columns = ['player', 'league'])

    # Remove whitespace, rename column
    data.playername = data.playername.str.strip()
    data = data.rename(columns = {'playername' : 'player'})

    # Rearrange columns
    data = data.loc[:, ['player', 'team', 'season', 'position', 'gp', 'g', 'a', 'tp', 'ppg', 'pim', '+/-', 'link']]

    data.to_csv('transformed_skaters.csv', index=False)

def transform_goalies(data=None):
    if data is None:
        data = load_data('goalies_data.pkl')

    # Drop redundant columns
    data = data.drop(columns = 'league')

    # Remove whitespace, rename column
    data.player = data.player.str.strip()
    data = data.rename(columns = {'sv%' : 'pct'})

    # Rearrange columns
    data = data.loc[:, ['player', 'team', 'season', 'gp', 'gaa', 'pct', 'w', 'l', 'so', 'toi', 'svs', 'ga', 'link']]

    data.to_csv('transformed_goalies.csv', index=False)