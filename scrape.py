import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import TopDownHockey_Scraper.TopDownHockey_EliteProspects_Scraper as tdhepscrape
from utils import save_data

# Set paremeters for scrape
leagues = ["nhl"]
seasons = ["2021-2022", "2022-2023"]

def scrape_skater_data():

    # Scrape data from eliteprospects.com
    nhl_skaters_2123 = tdhepscrape.get_skaters(leagues, seasons)

    # Return dataframe
    save_data(nhl_skaters_2123, 'skaters_data.pkl')

def scrape_goalie_data():

    nhl_goalies_2123 = tdhepscrape.get_goalies(leagues, seasons)

    save_data(nhl_goalies_2123, 'goalies_data.pkl')