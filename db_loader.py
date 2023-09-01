import pandas as pd
from sqlalchemy import create_engine

def load_to_db():
    skaters = pd.read_csv('transformed_skaters.csv')
    goalies = pd.read_csv('transformed_goalies.csv')

    database_url = "postgresql://your_user:your_password@localhost:5432/player_data"

    engine = create_engine(database_url)

    skaters.to_sql('skaters', engine, if_exists='replace', index=False)
    goalies.to_sql('goalies', engine, if_exists='replace', index=False)