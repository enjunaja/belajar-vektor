# main_app.py

import streamlit as st
from menu_beranda import beranda_menu
from menu_tentang import tentang_menu
from menu_konsep import konsep_menu
from menu_lkm import lkm_menu

# Pilihan menu dalam sidebar
menu = st.sidebar.selectbox("Menu", ["Beranda", "Tentang", "Konsep Materi", "Lembar Kerja"])

# Tampilkan konten sesuai dengan pilihan menu
if menu == "Beranda":
    beranda_menu()

elif menu == "Tentang":
    tentang_menu()

elif menu == "Konsep Materi":
    konsep_menu()

elif menu == "Lembar Kerja":
    lkm_menu()
