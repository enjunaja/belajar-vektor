import streamlit as st

def test_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> Ruang Vektor </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor Berbasis DNR!</h6>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h6 style='text-align: left;'>Mari kita cek pemahamanmu tentang Ruang Vektor!</h6>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Test 1", "Test 2", "Test 3"])
    
    with tab1: 
        st.markdown("<h5 style='text-align: left;'>Latihan 1</h5>", unsafe_allow_html=True)
        st.write("")
        st.write("Perhatikan gambar berikut. Pada gambar terlihat bagaimana suatu vektor dapat digunakan untuk merepresentasikan warna.")
        url_warna = "https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/warna.png"
        st.image(url_warna, caption='Merepresentasikan Warna dengan Vektor', width=300)
        st.write("")
        st.write("Apa yang dapat kamu ceritakan tentang gambar tersebut?")
        st.text_input('Tuliskan pendapatmu untuk latihan 1 pada box berikut!')
        
    with tab2:
        st.markdown("<h5 style='text-align: left;'>Latihan 2</h5>", unsafe_allow_html=True)
        st.write("")
        st.write("Perhatikan gambar grayscale berukuran 5x5 pixel berikut.")
        url_gs = "https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/5x5image.png"
        st.image(url_gs, caption='Merepresentasikan Gambar dengan Vektor', width=300)
        st.write("")
        st.write("Bagaimanakah kamu merepresentasikan gambar tersebut dalam suatu vektor? Jelaskan?")
        st.write("Tuliskanlah notasi yang tepat untuk menyatakan gambar grayscale berukuran 5x5 pixel dalam bentuk vektor secara umum!")
        st.text_input('Tuliskan pendapatmu untuk latihan 2 pada box berikut!')
    
    with tab3: 
        st.markdown("<h5 style='text-align: left;'>Latihan 3</h5>", unsafe_allow_html=True)
        st.write("")
        st.write("Perhatikan definisi vektor sebagai berikut.")
        st.button('Sebuah vektor dengan panjang n dapat merepresentasikan seberapa sering setiap kata dalam kamus berisi n kata muncul dalam sebuah dokumen. Misalnya, (25; 2; 0) berarti kata pertama dalam kamus muncul sebanyak 25 kali, kata kedua dua kali, dan kata ketiga sama sekali tidak muncul.')
        st.markdown("""
        Anggap kita memilih lima kata kunci berikut: mahasiswa, program, pendidikan, ilmu, komputer.
        - Apakah vektor dokumen untuk kalimat: "Mahasiswa Pendidikan Ilmu Komputer dididik untuk menjadi seorang guru dalam bidang komputer"?
        - Apakah vektor dokumen untuk kalimat: "Ilmu komputer merupakan pengembangan dari Matematika, sehingga wajar kedua program studi tersebut berada dalam satu fakultas"?
        - Apakah vektor dokumen untuk kalimat: "Algoritma dan Pemrograman merupakan salah satu mata kuliah wajib di program studi berbasis keilmuan komputer"?
        - Berilah contoh kalimat dalam bahasa Indonesia yang sesuai dengan vektor dokumen (2, 1, 1, 0, 0)
        - Anggap u; v adalah dua vektor dokumen, dengan u = v. Apakah dokumen-dokumen tersebut sama? Mengapa atau mengapa tidak?
        """)
        st.text_input('Tuliskan pendapatmu untuk latihan 3 pada box berikut!')
    
   
    
