# menu_kontak.py

import streamlit as st
from PIL import Image, ImageOps

def kontak_menu():
    st.markdown("<h3 style='text-align: center;'> Lembar Kerja Mahasiswa </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Vektor sebagai Representasi Data</h3>", unsafe_allow_html=True)
    st.write("")
    
    st.markdown("<h5 style='text-align: left;'>Tujuan Pembelajaran</h4>", unsafe_allow_html=True)
    st.write("a. Mengidentifikasi titik awal vektor dan titik ujung vektor;")
    st.write("b. Mengidentifikasi besar/panjang dan arah vektor;")
    st.write("c. Memformulasikan penjumlahan dan perkalian pada vektor;")
    st.write("d. Menentukan vektor nol (identitas penjumlahan);")
    st.write("e. Menentukan skalar satuan (identitas perkalian);")
    st.write("f. Mengevaluasi kesamaan dua vektor.")
    st.write(" ")
    
    st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Merepresentasikan Posisi dan Perpindahan sebagai Vektor</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: left;'>Tahapan Pembelajaran</h4>", unsafe_allow_html=True)
    st.write("Perhatikan gambar berikut!")
    url_github = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar1.png?raw=true"
    st.image(url_github, caption='Gambar dari Buku', use_column_width=True)

   # Fungsi untuk memberikan kotak dengan warna background yang berbeda
    def add_background_color(image_path, color):
        img = Image.open(image_path)
        img_with_background = ImageOps.expand(img, border=20, fill=color)
        return img_with_background

    # Path gambar dari sistem lokal
    image_path = 'https://github.com/enjunaja/belajar-vektor/blob/main/gambar1.png'

    # Memberikan kotak dengan warna background yang berbeda
    image_with_bg = add_background_color(image_path, 'yellow')

    # Menampilkan gambar dengan kotak berwarna background
    st.image(image_with_bg, caption='Gambar dengan Background Berwarna', use_column_width=True)

    st.write("Seorang atlet golf akan memukul bola yang berada pada posisi (0,0) seperti gambar diatas dengan tujuan adalah posisi lubang bola golf yang ditandai bendera. Bagaimana kita dapat menyatakan posisi lubang bola golf terhadap titik awal bola?")
