import streamlit as st

def test_menu():
    # Judul aplikasi
    st.markdown("<h3 style='text-align: center;'> Ruang Vektor </h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'> 💻 Media Pembelajaran Ruang Vektor Berbasis DNR!</h6>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h6 style='text-align: left;'>Mari kita cek pemahamanmu tentang Ruang Vektor!</h6>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Test 1", "Test 2", "Test 3", "Test 4", "Test 5"])
    with tab1: 
        st.markdown("<h5 style='text-align: left;'>Test 1</h5>", unsafe_allow_html=True)
    
    with tab2: 
        st.markdown("<h5 style='text-align: left;'>Test 2</h5>", unsafe_allow_html=True)
    
    with tab3: 
        st.markdown("<h5 style='text-align: left;'>Test 3</h5>", unsafe_allow_html=True)
    
    with tab4: 
        st.markdown("<h5 style='text-align: left;'>Test 4</h5>", unsafe_allow_html=True)
    
    with tab5: 
        st.markdown("<h5 style='text-align: left;'>Test 5</h5>", unsafe_allow_html=True)

    
