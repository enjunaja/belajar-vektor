# main_app.py

import streamlit as st
from menu_beranda import beranda_menu
from menu_tentang import tentang_menu
from menu_kontak import kontak_menu
from menu_kalkulator import kalkulator_menu

# Judul aplikasi
st.title("Belajar Ruang Vektor")

# Pilihan menu dalam sidebar
menu = st.sidebar.selectbox("Menu", ["Beranda", "Tentang", "Kalkulator", "Kontak"])

# Tampilkan konten sesuai dengan pilihan menu
if menu == "Beranda":
    beranda_menu()

elif menu == "Tentang":
    tentang_menu()

elif menu == "Kalkulator":
    kalkulator_menu()

elif menu == "Kontak":
    kontak_menu()
