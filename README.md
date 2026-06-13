# Anatomy of a Hit - What Makes Songs Chart-Topping Across Decades?

## Project Overview
An end-to-end data analytics project exploring what audio features make a song a hit, how the hit formula has changed across decades, and which genres dominate over time - using Spotify's top 2000 songs dataset (2000-2019).

## Business Question
Why do some songs become massive hits while others with similar production flop? Is it tempo? Energy? Danceability? Does what made a hit in 2000 still work in 2019?

## Tools & Technologies
| Layer | Tool |
|---|---|
| Data Cleaning | Python, Pandas |
| Analysis | SQL (SQLite) |
| Visualization | Power BI Desktop |
| Version Control | Git & GitHub |

## Dataset
- Source: Kaggle - Top Hits Spotify 2000-2019
- Size: 2,000 songs, 18 audio features
- Key Features: danceability, energy, valence, tempo, loudness, speechiness, acousticness, popularity, genre

## Project Structure

    HitSongAnalyzer/
    ├── data/
    │   ├── raw/               <- Original Kaggle CSV
    │   └── cleaned/           <- 6 SQL query outputs + cleaned CSV
    ├── sql/                   <- SQL query files
    ├── powerbi/               <- Power BI .pbix dashboard
    ├── docs/                  <- Dashboard screenshots
    ├── analysis.py            <- Data cleaning pipeline
    ├── run_queries.py         <- SQL analysis runner
    └── README.md

## Key Insights
- Valence is declining - songs have gotten progressively sadder from 2000s to 2010s
- Energy & tempo are rising - music is getting louder and faster
- Pop dominates - but hip hop has surged dramatically post-2010
- Hit Formula Score - top scoring songs combine high danceability (0.3), energy (0.25), valence (0.2), loudness (0.15), tempo (0.1)
- Formula does not equal Popularity - high audio scores do not guarantee chart success

## Dashboard Pages
1. Hit Overview - Genre distribution, audio feature trends, scatter of popularity vs danceability
2. Decade Deep Dive - How energy, valence, danceability, and tempo shifted decade by decade
3. Hit Formula - Hit Formula Score rankings, genre comparison, score vs popularity scatter

## Skills Demonstrated
- Python data cleaning & feature engineering
- SQL window functions (RANK, PARTITION BY)
- SQLite database creation
- Power BI dashboard design (3 pages, 9 visuals)
- Correlation analysis
- Business storytelling with cultural context

## Author
Yaya | Systems Engineer at Infosys | Aspiring Data Analyst
GitHub: https://github.com/Yayavari
