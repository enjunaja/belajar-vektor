# main_app.py

import streamlit as st
from menu.menu_beranda import beranda_menu
from menu.menu_tentang import tentang_menu
from menu.menu_konsep import konsep_menu
from menu.menu_lkm import lkm_menu
from menu.menu_test import test_menu
from menu_coba import coba_menu

# Menggunakan HTML dan CSS kustom untuk mengatur gambar latar belakang
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/background.png?token=GHSAT0AAAAAACMH4J3IYHUJJ76EORWMNDQIZMTRKAQ");
    background-size: cover;
}
</style>
'''
# Menampilkan HTML
st.markdown(page_bg_img, unsafe_allow_html=True)

with st.sidebar:
    st.title("Mari Belajar!")

# Pilihan menu dalam sidebar
menu = st.sidebar.selectbox("Menu", ["Beranda", "Tentang", "Konsep Materi", "Lembar Kerja", "Test", "Coba Program"])
# Tampilkan konten sesuai dengan pilihan menu
if menu == "Beranda":
    beranda_menu()

elif menu == "Tentang":
    tentang_menu()

elif menu == "Konsep Materi":
    konsep_menu()

elif menu == "Lembar Kerja":
    lkm_menu()

elif menu == "Test":
    test_menu()

elif menu == "Coba Program":
    coba_menu()

with st.sidebar:
    st.sidebar.image("https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/Webinar-pana.png?token=GHSAT0AAAAAACMH4J3JRXEHZLA7ZX6LRG3MZMTRFOQ",width=100)
