# player-stats

This Python project simulates an ETL workflow for NHL data. We collect detailed statistics on NHL goalies and skaters for the 2021-2022 and 2022-2023 seasons using the TopDownHockey web scraper. After extraction, the data undergoes cleaning with the pandas library to ensure accuracy and consistency. Once cleaned, it's loaded into a PostgreSQL database for structured storage and easy retrieval.

Below is an example of a query that can be made using the skaters table produced from these scripts:

![Alt text]([URL](https://user-images.githubusercontent.com/81118163/264910780-da5a45ed-d0f4-4fe2-b7bb-4147d5fcfc0f.PNG))



