# menu_beranda.py

import streamlit as st

def beranda_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> Ruang Vektor </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor Berbasis DNR!</h3>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='text-align: left;'>Selamat datang di Beranda 👋</h4>", unsafe_allow_html=True)

    st.markdown(
        """
        
        👈 Pilih Menu Belajar dari Sidebar untuk memulai kegiatan pembelajaran.

        """
    )
