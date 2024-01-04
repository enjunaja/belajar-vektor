import streamlit as st

def test_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> Ruang Vektor </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor Berbasis DNR!</h6>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h6 style='text-align: left;'>Mari kita cek pemahamanmu tentang Ruang Vektor!</h6>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Test 1", "Test 2", "Test 3", "Test 4", "Test 5"])
    
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
        st.write("Tuliskanlah notasi yang tepat untuk menyatakan gambar grayscale berukuran 5x5 pixel dalam bentuk vektor secara umum")
        st.text_input('Tuliskan pendapatmu untuk latihan 2 pada box berikut!')
    
    with tab3: 
        st.markdown("<h5 style='text-align: left;'>Test 3</h5>", unsafe_allow_html=True)
    
    with tab4: 
        st.markdown("<h5 style='text-align: left;'>Test 4</h5>", unsafe_allow_html=True)
    
    with tab5: 
        st.markdown("<h5 style='text-align: left;'>Test 5</h5>", unsafe_allow_html=True)

    
