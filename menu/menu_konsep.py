def konsep_menu():
  import streamlit as st
  import numpy as np

  st.write(" ")
  st.markdown("<h3 style='text-align: center;'> Ruang Vektor </h3>", unsafe_allow_html=True)
  st.markdown("<h6 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor Berbasis DNR!</h3>", unsafe_allow_html=True)
  st.write("")
  st.markdown("<h5 style='text-align: leftr;'>Materi</h5>", unsafe_allow_html=True)

  tab1, tab2, tab3, tab4, tab5 = st.tabs(["Lingkup Materi", "Tupel", "Vektor", "Operasi Vektor", "Vektor Fitur"])
  with tab1: 
        st.markdown("<h5 style='text-align: left;'>Lingkup Materi</h5>", unsafe_allow_html=True)
    
  with tab2: 
        st.markdown("<h5 style='text-align: left;'>Tupel</h5>", unsafe_allow_html=True)

  with tab3: 
        st.markdown("<h5 style='text-align: left;'>Vektor</h5>", unsafe_allow_html=True)

  with tab4: 
        st.markdown("<h5 style='text-align: left;'>Operasi Vektor</h5>", unsafe_allow_html=True)

  with tab5: 
        st.markdown("<h5 style='text-align: left;'>Vektor Fitur</h5>", unsafe_allow_html=True)
