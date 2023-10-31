# main_app.py

import streamlit as st
from menu_beranda import beranda_menu
from menu_tentang import tentang_menu
from menu_kontak import kontak_menu
from menu_kalkulator import kalkulator_menu

# Judul aplikasi
st.markdown("<h3 style='text-align: center;'> 💻 Mari Belajar Ruang Vektor!</h3>", unsafe_allow_html=True)

# Pilihan menu dalam sidebar
menu = st.selectbox.sidebar("Menu", ["Beranda", "Tentang", "Belajar", "Kontak"])

# Tampilkan konten sesuai dengan pilihan menu
if menu == "Beranda":
    beranda_menu()

elif menu == "Tentang":
    tentang_menu()

elif menu == "Belajar":
    kalkulator_menu()

elif menu == "Kontak":
    kontak_menu()
