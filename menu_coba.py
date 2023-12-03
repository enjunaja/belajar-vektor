import streamlit as st

def coba_menu():
        
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> Ini menu untuk coba program </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor Berbasis DNR!</h3>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='text-align: left;'>Silahkan tulis kode programnya</h4>", unsafe_allow_html=True)
    
    # Menampilkan tautan ke file PowerPoint
    st.markdown("[Download PowerPoint Presentation](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fenjunaja%2Fbelajar-vektor%2Fmain%2FOrganisasi%2520Objek%2520Matematika%2520Ruang%2520Vektor.pptx&wdOrigin=BROWSELINK)")
    
    def combine_rgb(red, green, blue):
        # Kombinasi nilai RGB untuk membuat warna baru
        combined_color = (red, green, blue)
        return combined_color
    
    def display_color_box(color):
        # Menampilkan kotak dengan warna yang dihasilkan
        st.write(f"Warna RGB yang dihasilkan: {color}")
        st.markdown(
            f"""
            <div style='background-color: rgb{color}; width: 100px; height: 100px;'></div>
            """,
            unsafe_allow_html=True
        )
    
    def main():
        st.title('Kombinasi Warna RGB')
        
        # Input nilai-nilai RGB dari pengguna
        red = st.slider('Merah (0-255)', 0, 255, 128)
        green = st.slider('Hijau (0-255)', 0, 255, 128)
        blue = st.slider('Biru (0-255)', 0, 255, 128)
        
        # Tombol untuk melakukan kombinasi nilai RGB
        if st.button('Gabungkan Warna'):
            combined_color = combine_rgb(red, green, blue)
            display_color_box(combined_color)
    
    main()

    
   
