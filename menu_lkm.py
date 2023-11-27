# menu_lkm.py

import streamlit as st
from PIL import Image

def lkm_menu():
    st.markdown("<h3 style='text-align: center;'> Lembar Kerja Mahasiswa </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Vektor sebagai Representasi Data</h3>", unsafe_allow_html=True)
    st.write("")

    tab1, tab2, tab3 = st.tabs(["Tujuan", "Kegiatan 1", "Kegiatan 2"])
    with tab1: 
        st.markdown("<h5 style='text-align: left;'>Tujuan Pembelajaran</h4>", unsafe_allow_html=True)
        st.write("Setelah melakukan Kegiatan Belajar 1 dan Kegiatan Belajar 2 diharapakan mahasiswa mampu:")
        st.write("a. Merepresentasikan data dengan menggunakan vektor;")
        st.write("b. Memformulasikan penjumlahan dan perkalian pada vektor;")
        st.write("c. Menentukan vektor nol (identitas penjumlahan);")
        st.write("d. Menentukan skalar satuan (identitas perkalian);")
        st.write("e. Mengevaluasi kesamaan dua vektor.")
        st.write(" ")

    with tab2:
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Merepresentasikan Posisi dan Perpindahan sebagai Vektor</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        
        st.markdown("<h5 style='text-align: left;'>Kegiatan Pembelajaran</h4>", unsafe_allow_html=True)
        st.write("Perhatikan gambar berikut!")
        url_github1 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar1.png?raw=true"
        st.image(url_github1, caption='Posisi bola pada Koordinat Cartesius (Takahashi, S. & Inoue, I.,  2008)')
        st.write("Seorang atlet golf akan memukul bola yang berada pada posisi (0,0) seperti gambar diatas dengan tujuan adalah posisi lubang bola golf yang ditandai bendera. Bagaimana kita dapat menyatakan posisi lubang bola golf relatif terhadap titik awal bola?")
        
        jawab1 = st.text_input('Jawab:')
        if jawab1 != '':
            if jawab1 == "(7,4)" or jawab1 == "(7, 4)" or jawab1 == "[7,4]" or jawab1 == "[7, 4]":
                st.write("Kamu benar!")
            else:
                st.write("Jawaban kamu masih salah, seharusnya posisi lubang bola terhadap titik (0, 0) adalah (7,4).")
        else: 
            st.write("Tuliskan jawabanmu pada kotak")
        
        show_next_paragraph = st.button("Berikutnya")
        if show_next_paragraph:
            st.write("Terdapat tiga orang pemain, yang memukul bola sehingga menghasilkan perpindahan posisi bola sebagaimana terlihat pada gambar-gambar berikut.")
             
            pemain1, pemain2, pemain3 = st.tabs(["Pemain 1", "Pemain 2", "Pemain 3"])
            with pemain1:
               st.header("Pemain 1")
               url_github2 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar2.png?raw=true"
               st.image(url_github2, caption='Perpindahan bola berdasarkan pukulan Pemain 1 (Takahashi, S. & Inoue, I.,  2008)')
            
            with pemain2:
               st.header("Pemain 2")
               url_github3 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar3.png?raw=true"
               st.image(url_github3, caption='Perpindahan bola berdasarkan pukulan Pemain 2 (Takahashi, S. & Inoue, I.,  2008)')
            
            with pemain3:
                st.header("Pemain 3")
                url_github4 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar4.png?raw=true"
                st.image(url_github4, caption='Perpindahan bola berdasarkan pukulan Pemain 3 (Takahashi, S. & Inoue, I.,  2008)')
                
            
    with tab3:
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Merepresentasikan Warna sebagai Vektor</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)

        st.markdown("<h5 style='text-align: left;'>Kegiatan Pembelajaran</h4>", unsafe_allow_html=True)
        
