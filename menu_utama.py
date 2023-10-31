# main_app.py

import streamlit as st
from menu_beranda import beranda_menu
from menu_tentang import tentang_menu
from menu_kontak import kontak_menu
from menu_kalkulator import kalkulator_menu

# Judul aplikasi
st.markdown("<h1 style='text-align: center;'>Judul Aplikasi Tengah</h1>", unsafe_allow_html=True)
st.subtitle(" 💻 Mari Belajar Ruang Vektor!")

# Pilihan menu dalam sidebar
menu = st.sidebar.selectbox("Menu", ["Beranda", "Tentang", "Belajar", "Kontak"])

# Tampilkan konten sesuai dengan pilihan menu
if menu == "Beranda":
    beranda_menu()

elif menu == "Tentang":
    tentang_menu()

elif menu == "Belajar":
    kalkulator_menu()

elif menu == "Kontak":
    kontak_menu()
