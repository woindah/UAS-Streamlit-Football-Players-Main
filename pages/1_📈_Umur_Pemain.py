import numpy as np
import pandas as pd
import streamlit as st
from datetime import date 

# MEMANGGIL DATA CSV
df = pd.read_csv("./data/players.csv") 

# MEMBUAT FUNGSI MENGHITUNG UMUR DARI TANGGAL LAHIR
def age(born): 
    today = date.today() 
    return today.year - born.year - ((today.month,today.day) < (born.month,born.day)) 


st.title("Umur Pemain Berdasarkan Posisi")  # MENAMBAH TITLE HALAMAN

# MEMBUAT DROPDOWN PILIHAN POSISI PEMAIN
option = st.selectbox(
    'Pilih Posisi Pemain?',
    df['position'].drop_duplicates())

st.subheader('Menampilkan histogram posisi umur pemain :blue['+option+'] :sunglasses:')

# MENGSELEKSI DATA BERDASARKAN PILIHAN POSISI PEMAIN
posisi = df[df['position'] == option]
# MEMBUAT KOLOM BARU UMUR
posisi['date_of_birth'] = pd.to_datetime(posisi['date_of_birth'], format='%Y-%m-%d')
posisi['Umur'] = posisi['date_of_birth'].apply(age) 

# MELAKUKAN GROUPING UMUR UNTUK MENDAPATKAN JUMLAH PEMAIN YG BERUMUR SAMA
umur = posisi.groupby('Umur', sort=False).count()
umur['Jumlah'] = umur['player_id']

# MENAMPILKAN CHART
st.bar_chart(umur,y='Jumlah')
#MENAMPILKAN TABEL DATA
st.write(posisi)