def konsep_menu():
  import streamlit as st
  import numpy as np

  #Mendefinisikan CSS untuk menyesuaikan ukuran teks di tab
  custom_tab_style = (
    "display: flex; justify-content: center; align-items: center; "
    "font-size: 24px;"  # Sesuaikan ukuran teks sesuai kebutuhan Anda
  )

  st.markdown("<h2 style='text-align: center;'> 💻 Vektor sebagai Representasi Data</h2>", unsafe_allow_html=True)
  st.write("")

  tab1, tab2, = st.tabs(["Tuple", "Vektor"])

  with tab1:
    st.markdown("<h5 style='text-align: left;'>Tonton video berikut untuk belajar tentang Tuple</h4>", unsafe_allow_html=True)
    # Path ke file video lokal sebagai contoh
    video_path = "https://youtu.be/j63I-rpm56E"

    # Menampilkan video dari file lokal
    st.video(video_path)

  with tab2:
    st.markdown("<h5 style='text-align: left;'>Buka PPT berikut untuk belajar tentang Tuple</h4>", unsafe_allow_html=True)
    drive_file_url = "https://drive.google.com/uc?id=1Z5qoSXDVDPewkL5dsrCKe1TnV0cNWbYS"
    # Menampilkan tautan ke file
    st.markdown(f"[Lihat Presentasi]({drive_file_url})")
  
 
