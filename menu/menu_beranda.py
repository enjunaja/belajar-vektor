# menu_beranda.py

import streamlit as st

def beranda_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor</h3>", unsafe_allow_html=True)
    st.image("https://github.com/enjunaja/belajar-vektor/blob/main/gambar/Webinar-pana.png?raw=true",width=600)

    st.markdown(
        """
        👈 Pilih Menu Belajar dari Sidebar untuk memulai kegiatan pembelajaran.

        """
    )
