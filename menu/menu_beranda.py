# menu_beranda.py

import streamlit as st

def beranda_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor</h3>", unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/Webinar-pana.png",width=600)

    st.markdown("<h4 style='text-align: center;'>👈 Pilih Menu Belajar dari Sidebar untuk memulai kegiatan pembelajaran.</h4>", unsafe_allow_html=True)
