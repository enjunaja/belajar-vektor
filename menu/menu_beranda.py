# menu_beranda.py

import streamlit as st

def beranda_menu():
    # Judul aplikasi
    st.markdown("<h2 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor</h2>", unsafe_allow_html=True)

   # URL gambar dari "story set" atau sumber daya penyimpanan lainnya
    image_url_story_set = "https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/Webinar-pana.png"

    # Mendefinisikan CSS untuk menengahkan gambar
    centered_image_style = (
        "display: flex; justify-content: center; align-items: center; "
        #"width: 50px;"
        "height: 200px;" # Sesuaikan tinggi gambar sesuai kebutuhan Anda
    )

    # Menampilkan gambar dengan menggunakan style
    st.markdown(
        f'<div style="{centered_image_style}"><img src="{image_url_story_set}" alt="Gambar" width="500"></div>',
        unsafe_allow_html=True
    )

    #st.image("https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/Webinar-pana.png",width=600)

    st.markdown("<h4 style='text-align: center;'>👈 Pilih Menu Belajar dari Sidebar untuk memulai kegiatan pembelajaran.</h4>", unsafe_allow_html=True)
