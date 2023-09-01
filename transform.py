import pandas as pd
import TopDownHockey_Scraper.TopDownHockey_EliteProspects_Scraper as tdhepscrape
from utils import load_data

def transform_skaters(data=None):
    if data is None:
        data = load_data('skaters_data.pkl')  # Changed variable name to 'data'

    #drop redundant columns
    data = data.drop(columns = ['player', 'league'])

    #remove whitespace, rename column
    data.playername = data.playername.str.strip()
    data = data.rename(columns = {'playername' : 'player'})

    #rearrange columns to be more readable
    data = data.loc[:, ['player', 'team', 'season', 'position', 'gp', 'g', 'a', 'tp', 'ppg', 'pim', '+/-', 'link']]

    data.to_csv('transformed_skaters.csv', index=False)

def transform_goalies(data=None):
    if data is None:
        data = load_data('goalies_data.pkl')  # Corrected file name to 'goalies_data.pkl'

    #drop redundant columns
    data = data.drop(columns = 'league')

    #remove whitespace, rename column
    data.player = data.player.str.strip()
    data = data.rename(columns = {'sv%' : 'pct'})

    #rearrange columns to be more readable
    data = data.loc[:, ['player', 'team', 'season', 'gp', 'gaa', 'pct', 'w', 'l', 'so', 'toi', 'svs', 'ga', 'link']]

    data.to_csv('transformed_goalies.csv', index=False)

#cleaned_skaters = transform_skaters()
#cleaned_skaters.to_csv('skaters.csv', index=True)

#cleaned_goalies = transform_goalies()
#cleaned_goalies.to_csv('goalies.csv', index=True)