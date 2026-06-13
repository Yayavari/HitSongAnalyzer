import pandas as pd
import sqlite3
import os

df = pd.read_csv('data/raw/songs_normalize.csv')
df.columns = df.columns.str.lower().str.strip()
df['decade'] = (df['year'] // 10 * 10).astype(str) + 's'
df = df.dropna(subset=['danceability','energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','popularity'])
df['loudness_norm'] = (df['loudness'] - df['loudness'].min()) / (df['loudness'].max() - df['loudness'].min())
os.makedirs('data/cleaned', exist_ok=True)
df.to_csv('data/cleaned/hits_cleaned.csv', index=False)
print('Cleaned shape:', df.shape)
conn = sqlite3.connect('data/spotify_analysis.db')
df.to_sql('top_hits', conn, if_exists='replace', index=False)
conn.close()
print('SQLite DB created.')
