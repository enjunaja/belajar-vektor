import streamlit as st
import numpy as np

def kalkulator_menu():
  st.header("Kalkulator Perkalian Vektor")
  def hitung():
   
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

  hitung()
