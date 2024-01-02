# menu_lkm.py

import streamlit as st
from PIL import Image

def lkm_menu():
    
    st.markdown("<h2 style='text-align: center;'> 💻 Vektor sebagai Representasi Data</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'> Lembar Kerja Mahasiswa </h3>", unsafe_allow_html=True)
    st.write("")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Tujuan", "Pengantar", "Kegiatan 1", "Kegiatan 2", "Kegiatan 3", "Kesimpulan"])
    with tab1: 
        st.markdown("<h5 style='text-align: left;'>Tujuan Pembelajaran</h4>", unsafe_allow_html=True)
        st.write("Setelah melakukan Kegiatan Belajar diharapkan mahasiswa mampu:")
        st.write("a. Merepresentasikan data dengan menggunakan vektor;")
        st.write("b. Memformulasikan penjumlahan dan perkalian pada vektor;")
        st.write("c. Menentukan vektor nol (identitas penjumlahan);")
        st.write(" ")
    
    with tab2:
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Merepresentasikan Posisi dan Perpindahan sebagai Vektor</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.write(" ")
    
        st.markdown("<h5 style='text-align: left;'>Perhatikan gambar berikut!</h4>", unsafe_allow_html=True)
        url_github1 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar/gambar1.png?raw=true"
        st.image(url_github1, caption='Posisi bola pada Koordinat Cartesius (Takahashi, S. & Inoue, I.,  2008)')
        st.write("Seorang atlet golf akan memukul bola yang berada pada posisi (0,0) seperti gambar diatas dengan tujuan adalah posisi lubang bola golf yang ditandai bendera. Bagaimana kita dapat menyatakan posisi lubang bola golf relatif terhadap titik awal bola?")
        
        jawab1 = st.text_input('Jawab:')
        if jawab1 != '':
            if jawab1 == "(7,4)" or jawab1 == "(7, 4)" or jawab1 == "[7,4]" or jawab1 == "[7, 4]":
                st.write("Kamu benar! Suatu objek yang terletak pada sumbu-x (garis horizontal) dengan koordinat x = 7 dan pada sumbu-y (garis vertikal) dengan koordinat y = 4, dapat kita notasikan dengan menggunakan tuple sebagai (7, 4).")
            else:
                st.write("Jawaban kamu masih salah, seharusnya posisi lubang bola terhadap titik (0, 0) adalah (7,4). Suatu objek yang terletak pada sumbu-x (garis horizontal) dengan koordinat x = 7 dan pada sumbu-y (garis vertikal) dengan koordinat y = 4, dapat kita notasikan dengan menggunakan tuple sebagai (7, 4).")
        else: 
            st.write("Tuliskan jawabanmu pada kotak")
        
        show_next_paragraph = st.button("Berikutnya")
        if show_next_paragraph:
            st.write("Secara umum, Suatu objek yang terletak pada sumbu-x (garis horizontal) dengan koordinat x = a dan pada sumbu-y (garis vertikal) dengan koordinat y = b, dapat kita notasikan dengan menggunakan tuple sebagai (a, b).")
            next = st.button("Lanjutkan pada Kegiatan 1")
            
           
                  
    with tab3:
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Kegiatan 1</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)

        st.write('Untuk memindahkan bola golf dari titik (0, 0) ke titik (7,4), seorang pemain (Pemain 1) melakukan tiga pukulan seperti pada gambar berikut.')
        
        st.markdown("<h5 style='text-align: left;'>Pemain 1</h4>", unsafe_allow_html=True)
        url_github2 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar/gambar2.png?raw=true"
        st.image(url_github2, caption='Perpindahan bola berdasarkan pukulan Pemain 1 (Takahashi, S. & Inoue, I.,  2008)')
        st.write('')
        st.markdown("<h5 style='text-align: center;'>Data Pukulan Bola Pemain 1</h5>", unsafe_allow_html=True)
        st.write('')
        
        st.markdown("<h5 style='text-align: left;'>Pukulan ke-1</h5>", unsafe_allow_html=True)
        st.markdown("""
        - Posisi bola pukulan ke-1: (3,1)
        - Posisi bola relatif terhadap posisi terakhirnya: 3 ke kanan dan 1 ke atas relatif terhadap posisi (0,0)
        - Perpindahan bola yang dinyatakan dalam bentuk (ke kanan, ke atas): (3, 1)
        """)
        

        st.write('')
        st.markdown("<h5 style='text-align: left;'>Pukulan ke-2</h5>", unsafe_allow_html=True)
        st.markdown("""
        - Posisi bola pukulan ke-2: (4,3)
        - Posisi bola relatif terhadap posisi terakhirnya: 1 ke kanan dan 2 ke atas relatif terhadap posisi (3,1)
        - Perpindahan bola yang dinyatakan dalam bentuk (ke kanan, ke atas): (1, 2)
        """)
        

        st.write('')
        st.markdown("<h5 style='text-align: left;'>Pukulan ke-3</h5>", unsafe_allow_html=True)
        st.markdown("""
        - Posisi bola pukulan ke-3: (7,4)
        - Posisi bola relatif terhadap posisi terakhirnya: 3 ke kanan dan 1 ke atas relatif terhadap posisi (4,3)
        - Perpindahan bola yang dinyatakan dalam bentuk (ke kanan, ke atas): (3, 1)
        """)
        
    
    with tab4:
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Kegiatan 2</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        
        st.write('Untuk memindahkan bola golf dari titik (0, 0) ke titik (7,4), seorang pemain (Pemain 2) melakukan dua pukulan seperti pada gambar berikut.')
        
        st.markdown("<h5 style='text-align: left;'>Pemain 2</h4>", unsafe_allow_html=True)
        url_github3 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar/gambar3.png?raw=true"
        st.image(url_github3, caption='Perpindahan bola berdasarkan pukulan Pemain 2 (Takahashi, S. & Inoue, I.,  2008)')
        st.write('')
        st.markdown("<h5 style='text-align: center;'>Data Pukulan Bola Pemain 2</h5>", unsafe_allow_html=True)

        st.write('')
        st.markdown("<h5 style='text-align: left;'>Pukulan ke-1</h5>", unsafe_allow_html=True)
        st.markdown("""
        - Posisi bola pukulan ke-1: (10,10)
        - Posisi bola relatif terhadap posisi terakhirnya: 10 ke kanan dan 10 ke atas relatif terhadap posisi (0,0)
        - Perpindahan bola yang dinyatakan dalam bentuk (ke kanan, ke atas): (10, 10)
        """)
        
        st.write('')
        st.markdown("<h5 style='text-align: left;'>Pukulan ke-2</h5>", unsafe_allow_html=True)
        st.markdown("""
        - Posisi bola pukulan ke-2: (7,4)
        - Posisi bola relatif terhadap posisi terakhirnya: 3 ke kiri dan 6 ke bawah relatif terhadap posisi (10,10)
        - Perpindahan bola yang dinyatakan dalam bentuk (ke kanan, ke atas): (-3,-6)
        """)
             
        
    with tab5:
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Kegiatan 3</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)

        st.write('Untuk memindahkan bola golf dari titik (0, 0) ke titik (7,4), seorang pemain (Pemain 3) melakukan satu pukulan seperti pada gambar berikut.')
        
        st.markdown("<h5 style='text-align: left;'>Pemain 3</h4>", unsafe_allow_html=True)
        url_github4 = "https://github.com/enjunaja/belajar-vektor/blob/main/gambar/gambar4.png?raw=true"
        st.image(url_github4, caption='Perpindahan bola berdasarkan pukulan Pemain 3 (Takahashi, S. & Inoue, I.,  2008)')
        st.write('')
        st.markdown("<h5 style='text-align: center;'>Data Pukulan Bola Pemain 3</h5>", unsafe_allow_html=True)
        st.write('')
        
        st.markdown("<h5 style='text-align: left;'>Pukulan ke-1</h5>", unsafe_allow_html=True)
        st.markdown("""
        - Posisi bola pukulan ke-1: (7,4)
        - Posisi bola relatif terhadap posisi terakhirnya: 7 ke kanan dan 4 ke atas relatif terhadap posisi (0,0)
        - Perpindahan bola yang dinyatakan dalam bentuk (ke kanan, ke atas): (7,4)
        """)
        
    with tab6:
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Kesimpulan</h4>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>==================================================================================</h4>", unsafe_allow_html=True)

        st.write('Berdasarkan kegiatan 1, 2, dan 3, dapat kita simpulkan bahwa:')
        jawaban1 = st.text_input('(a,b)+(c,d)=')
        if jawab1 != '':
            if jawaban1 == "(a+c,b+d)" or jawaban1 == "(a+c, b+d)" or jawaban1 == "[a+c, b+d]" or jawaban1 == "[a+c,b+d]":
                st.write("Kamu benar! (a,b)+(c,d)=(a+c, b+d)")
            else:
                st.write("Jawaban kamu masih salah, seharusnya (a,b)+(c,d)=(a+c, b+d)")
        else: 
            st.write("Tuliskan jawabanmu pada kotak")

        jawaban2 = st.text_input('(a,b)-(c,d)=')
        if jawaban2 != '':
            if jawaban2 == "(a-c,b-d)" or jawaban2 == "(a-c, b-d)" or jawaban2 == "[a-c,b-d]" or jawaban2 == "[a-c, b-d]":
                st.write("Kamu benar! (a,b)-(c,d)=(a-c, b-d)")
            else:
                st.write("Jawaban kamu masih salah, seharusnya (a,b)-(c,d)=(a-c, b-d)")
        else: 
            st.write("Tuliskan jawabanmu pada kotak")
        
         
        
             
