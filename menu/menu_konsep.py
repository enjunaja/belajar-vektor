def konsep_menu():
  import streamlit as st
  import numpy as np

  # Mendefinisikan CSS untuk menyesuaikan ukuran teks di tab
  #custom_tab_style = (
   # "display: flex; justify-content: center; align-items: center; "
    #"font-size: 24px;"  # Sesuaikan ukuran teks sesuai kebutuhan Anda
  #)

  #st.markdown("<h2 style='text-align: center;'> 💻 Vektor sebagai Representasi Data</h2>", unsafe_allow_html=True)
  #st.write("")

  #tab1, tab2, = st.tabs(["Tuple", "Vektor"])

 # with tab1:
  #  st.markdown("<h5 style='text-align: left;'>Tuple</h4>", unsafe_allow_html=True)

 # with tab2: 
     #   st.markdown("<h5 style='text-align: left;'>Vektor</h4>", unsafe_allow_html=True)
  
 

  # Menggunakan HTML untuk menyesuaikan ukuran teks pada tab
  tabs_html = """
  <style>
    .custom-tab {
        font-size: 24px;
    }
  </style>
  """

  st.markdown(tabs_html, unsafe_allow_html=True)

  # Membuat tab dengan teks yang lebih besar
  selected_tab = st.radio("Pilih Tab", ["<div class='custom-tab'>Tuple</div>", "<div class='custom-tab'>Vektor</div>"], format_func=lambda x: "")

  # Menampilkan konten sesuai dengan tab yang dipilih
  if selected_tab == "<div class='custom-tab'>Tuple</div>":
    st.write("Konten untuk Tab Tuple")
  else:
    st.write("Konten untuk Tab Vektor")

