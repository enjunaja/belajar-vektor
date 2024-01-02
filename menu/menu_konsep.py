def konsep_menu():
  import streamlit as st
  import numpy as np

  tabs = [HOME, APPLICATION  ]

  option_data = [
    {'icon': "🏠", 'label': HOME},
    {'icon': "🤖", 'label': APPLICATION}

  ]

  over_theme = {'txc_inactive': 'black', 'menu_background': '#F5B7B1', 'txc_active': 'white', 'option_active': '#CD5C5C'}
  font_fmt = {'font-class': 'h3', 'font-size': '50%'}

  chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True)

  if chosen_tab == HOME:
    st.text('Fixed width text')

  elif chosen_tab == APPLICATION:
    st.text('Fixed width text')

