import sqlite3
import pandas as pd

conn = sqlite3.connect('data/spotify_analysis.db')

queries = {
    '01_decade_averages': '''
        SELECT
            decade,
            COUNT(*) AS total_songs,
            ROUND(AVG(popularity), 2) AS avg_popularity,
            ROUND(AVG(danceability), 2) AS avg_danceability,
            ROUND(AVG(energy), 2) AS avg_energy,
            ROUND(AVG(valence), 2) AS avg_valence,
            ROUND(AVG(tempo), 2) AS avg_tempo,
            ROUND(AVG(loudness_norm), 2) AS avg_loudness,
            ROUND(AVG(acousticness), 2) AS avg_acousticness,
            ROUND(AVG(speechiness), 2) AS avg_speechiness
        FROM top_hits
        GROUP BY decade
        ORDER BY decade
    ''',
    '02_top5_per_decade': '''
        SELECT decade, artist, song, popularity,
            RANK() OVER (PARTITION BY decade ORDER BY popularity DESC) AS rank_in_decade
        FROM top_hits
        ORDER BY decade, rank_in_decade
    ''',
    '03_genre_by_year': '''
        SELECT year, genre, COUNT(*) AS song_count,
            ROUND(AVG(popularity), 2) AS avg_popularity
        FROM top_hits
        GROUP BY year, genre
        ORDER BY year, song_count DESC
    ''',
    '04_popularity_correlation': '''
        SELECT
            ROUND(danceability, 1) AS danceability_bucket,
            ROUND(energy, 1) AS energy_bucket,
            ROUND(valence, 1) AS valence_bucket,
            COUNT(*) AS song_count,
            ROUND(AVG(popularity), 2) AS avg_popularity
        FROM top_hits
        GROUP BY danceability_bucket, energy_bucket, valence_bucket
        ORDER BY avg_popularity DESC
    ''',
    '05_hit_formula_score': '''
        SELECT
            artist, song, year, decade, genre, popularity,
            danceability, energy, valence, tempo, loudness_norm,
            ROUND(
                (danceability * 0.3) +
                (energy * 0.25) +
                (valence * 0.2) +
                (loudness_norm * 0.15) +
                ((tempo / 200.0) * 0.1), 4
            ) AS hit_formula_score
        FROM top_hits
        ORDER BY hit_formula_score DESC
    ''',
    '06_tempo_energy_by_decade': '''
        SELECT
            decade,
            ROUND(AVG(tempo), 2) AS avg_tempo,
            ROUND(AVG(energy), 2) AS avg_energy,
            ROUND(AVG(danceability), 2) AS avg_danceability,
            ROUND(AVG(valence), 2) AS avg_valence
        FROM top_hits
        GROUP BY decade
        ORDER BY decade
    '''
}

for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    df.to_csv(f'data/cleaned/{name}.csv', index=False)
    print(f'✅ {name} saved. Rows: {len(df)}')

conn.close()
print('\n✅ All queries done.')
