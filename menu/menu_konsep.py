def konsep_menu():
  import streamlit as st
  import numpy as np

  # Mendefinisikan CSS untuk menyesuaikan ukuran teks di tab
  custom_tab_style = (
    "display: flex; justify-content: center; align-items: center; "
    "font-size: 24px;"  # Sesuaikan ukuran teks sesuai kebutuhan Anda
  )

  # Menampilkan tab dengan gaya khusus
  st.markdown(
    f'<div style="{custom_tab_style}">My Tab</div>',
    unsafe_allow_html=True
  )
  
  st.markdown("<h2 style='text-align: center;'> 💻 Vektor sebagai Representasi Data</h2>", unsafe_allow_html=True)
  st.write("")

  tab1, tab2, = st.tabs(["Tuple", "Vektor"])

  with tab1: 
        st.markdown("<h5 style='text-align: left;'>Tuple</h4>", unsafe_allow_html=True)

  with tab2: 
        st.markdown("<h5 style='text-align: left;'>Vektor</h4>", unsafe_allow_html=True)
  
 
