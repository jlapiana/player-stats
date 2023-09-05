import scrape, transform
from db import db_loader

scrape.scrape_skater_data()
scrape.scrape_goalie_data()

transform.transform_skaters()
transform.transform_goalies()

db_loader.load_to_db()