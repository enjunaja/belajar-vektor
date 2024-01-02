def konsep_menu():
  import streamlit as st
  import numpy as np

  tab1, tab2, tab3 = st.tabs(["Tujuan", "Kegiatan 1", "Kegiatan 2"])

  option_data = [
    {'icon': "🏠", 'label': Tujuan},
    {'icon': "🤖", 'label': Kegiatan 1}
    {'icon': "🤖", 'label': Kegiatan 2}

  ]

  over_theme = {'txc_inactive': 'black', 'menu_background': '#F5B7B1', 'txc_active': 'white', 'option_active': '#CD5C5C'}
  font_fmt = {'font-class': 'h3', 'font-size': '50%'}

  chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True)

  with tab1: 
        st.markdown("<h5 style='text-align: left;'>Tujuan Pembelajaran</h4>", unsafe_allow_html=True)

  with tab2: 
        st.markdown("<h5 style='text-align: left;'>Kegiatan1</h4>", unsafe_allow_html=True)
  
  with tab3: 
        st.markdown("<h5 style='text-align: left;'>Kegiatan 2</h4>", unsafe_allow_html=True)

