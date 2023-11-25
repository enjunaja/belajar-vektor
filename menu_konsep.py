def konsep_menu():
  import streamlit as st
  import numpy as np

  st.write(" ")
  st.markdown("<h4 style='text-align: leftr;'>Perkalian Vektor</h4>", unsafe_allow_html=True)
  def hitung():
   
      # Input vektor pertama
      st.markdown("<h5 style='text-align: leftr;'>Vektor Pertama</h5>", unsafe_allow_html=True)
      vector1 = st.text_input('Masukkan vektor pertama (pisahkan angka dengan spasi):')

      # Input vektor kedua
      st.markdown("<h5 style='text-align: leftr;'>Vektor Kedua</h5>", unsafe_allow_html=True)
      vector2 = st.text_input('Masukkan vektor kedua (pisahkan angka dengan spasi):')
      st.write(" ")

      # Konversi input ke dalam bentuk list
      vector1 = [float(x) for x in vector1.split()]
      vector2 = [float(x) for x in vector2.split()]

      # Hitung perkalian vektor
      result = np.dot(vector1, vector2)

      # Tampilkan hasil
      st.markdown("<h5 style='text-align: leftr;'>Hasil Perkalian Vektor</h5>", unsafe_allow_html=True)
      st.write(f'Vektor Pertama: {vector1}')
      st.write(f'Vektor Kedua: {vector2}')
      st.write(f'Hasil Perkalian: {result}')

  hitung()
