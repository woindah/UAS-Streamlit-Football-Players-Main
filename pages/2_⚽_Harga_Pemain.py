import numpy as np
import pandas as pd
import streamlit as st
from datetime import date 

# MEMANGGIL DATA CSV
player = pd.read_csv("./data/players.csv") 
appearances = pd.read_csv("./data/appearances.csv") 

st.title("Harga Pemain Berdasarkan Jumlah GOAL ⚽")  # MENAMBAH TITLE HALAMAN

# MEMFILTER DATA UNTUK GOAL LEBIH DARI 1 SAJA
appearances = appearances[appearances['goals'] > 0]
# MELAKUKAN MERGING DATA GOAL DENGAN PLAYER
df = player.merge(appearances, how='left',on='player_id')
# MEMFILTER LAGI DATA UNTUK GOAL LEBIH DARI 1 SAJA
goal = df[df['goals'] > 0]

option_goals = st.selectbox(
    'MAKSIMAL BANYAK GOAL',
    df['goals'].drop_duplicates())

# MEMFILTER DATA BERDASARKKAN PILIHAN GOAL DI DROPDOWN
goal = goal[goal['goals'] <= option_goals]

# MENAMPILKAN DATA
st.scatter_chart(
    goal,
    x='goals',
    y='market_value_in_eur',
    color='market_value_in_eur',
    height=600
)
# st.write(df)