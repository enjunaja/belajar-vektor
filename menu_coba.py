import streamlit as st

def coba_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> Ini menu untuk coba program </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor Berbasis DNR!</h3>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='text-align: left;'>Silahkan tulis kode programnya</h4>", unsafe_allow_html=True)
    
    # Menampilkan tautan ke file PowerPoint
    st.markdown("[Download PowerPoint Presentation](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fenjunaja%2Fbelajar-vektor%2Fmain%2FOrganisasi%2520Objek%2520Matematika%2520Ruang%2520Vektor.pptx&wdOrigin=BROWSELINK)")

    import streamlit as st

    # Mengubah warna latar belakang dengan st.markdown()
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0; /* Ubah ke kode warna yang Anda inginkan */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Konten aplikasi Streamlit di bawah
    st.write("Ini adalah konten Streamlit dengan latar belakang yang berbeda.")

   
