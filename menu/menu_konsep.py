def konsep_menu():
  import streamlit as st
  import numpy as np

  st.markdown("<h3 style='text-align: center;'> Materi </h3>", unsafe_allow_html=True)
  st.markdown("<h6 style='text-align: center;'> 💻 Vektor sebagai Representasi Data</h3>", unsafe_allow_html=True)
  st.write("")

  tab1, tab2, = st.tabs(["Tuple", "Vektor"])

  with tab1: 
        st.markdown("<h5 style='text-align: left;'>Tuple</h4>", unsafe_allow_html=True)

  with tab2: 
        st.markdown("<h5 style='text-align: left;'>Vektor</h4>", unsafe_allow_html=True)
  
 
