# menu_beranda.py

import streamlit as st

def beranda_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor</h3>", unsafe_allow_html=True)
    st.write("")
    st.image("https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/Webinar-pana.png?token=GHSAT0AAAAAACMH4J3I2I7FHOS3YRFN4DAGZMTRNDA",width=2000)

    st.markdown(
        """
        
        👈 Pilih Menu Belajar dari Sidebar untuk memulai kegiatan pembelajaran.

        """
    )
