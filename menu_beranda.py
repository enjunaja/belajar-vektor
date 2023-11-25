# menu_beranda.py

import streamlit as st

def beranda_menu():
    st.write("")
    st.markdown("<h4 style='text-align: left;'>Selamat datang di Beranda 👋</h4>", unsafe_allow_html=True)

    st.markdown(
        """
        Ini adalah halaman beranda aplikasi kami.
        
        👈 Pilih Menu Belajar dari Sidebar untuk memulai kegiatan pembelajaran.

        """
    )
