CREATE DATABASE player_data;

\c player_data;

-- Create the skaters table
CREATE TABLE skaters (
    player VARCHAR(255),
    team VARCHAR(100),
    season VARCHAR(50),
    position VARCHAR(50),
    gp INTEGER,
    g INTEGER,
    a INTEGER,
    tp INTEGER,
    ppg REAL,
    pim INTEGER,
    plus_minus INTEGER,
    link TEXT
);

-- Create the goalies table
CREATE TABLE goalies (
    player VARCHAR(255),
    team VARCHAR(100),
    season VARCHAR(50),
    gp INTEGER,
    gaa REAL,
    pct REAL,
    w INTEGER,
    l INTEGER,
    so INTEGER,
    toi INTEGER,
    svs INTEGER,
    ga INTEGER,
    link TEXT
);