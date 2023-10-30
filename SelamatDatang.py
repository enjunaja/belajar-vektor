import streamlit as st
import numpy as np

# Judul aplikasi
st.title("Aplikasi dengan Sidebar")

# Membuat sidebar
menu = st.sidebar.selectbox("Menu", ["Beranda", "Tentang", "Kalkulator", "Kontak"])

if menu == "Beranda":
    st.header("Selamat datang di Beranda")
    st.write("Ini adalah halaman beranda aplikasi kami.")

elif menu == "Tentang":
    st.header("Tentang Kami")
    st.write("Kami adalah perusahaan yang fantastis!")
    
elif menu == "Kalkulator":
    
    def main():
        st.title('Kalkulator Perkalian Vektor')

        # Input vektor pertama
        st.header('Vektor Pertama')
        vector1 = st.text_input('Masukkan vektor pertama (pisahkan angka dengan spasi):')

        # Input vektor kedua
        st.header('Vektor Kedua')
        vector2 = st.text_input('Masukkan vektor kedua (pisahkan angka dengan spasi):')

        # Konversi input ke dalam bentuk list
        vector1 = [float(x) for x in vector1.split()]
        vector2 = [float(x) for x in vector2.split()]

        # Hitung perkalian vektor
        result = np.dot(vector1, vector2)

        # Tampilkan hasil
        st.header('Hasil Perkalian Vektor')
        st.write(f'Vektor Pertama: {vector1}')
        st.write(f'Vektor Kedua: {vector2}')
        st.write(f'Hasil Perkalian: {result}')

    if __name__ == '__main__':
        main()
        
elif menu == "Kontak":
    st.header("Kontak Kami")
    st.write("Hubungi kami di alamat email: example@example.com")




