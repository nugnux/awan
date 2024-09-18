import streamlit as st

st.title('FISIKA KOMPUTASI AWAN')
st.write('Situs Official Puan')
st.latex(r''' \int_a^b \frac{\partial^2 y}{\partial x^2}dx''')
st.page_link("http://www.google.com", label="Google", icon="🌎")
st.page_link("http://www.nugroho.xyz", label="Nug", icon="🌎")

print('Halo')
print('Tadaa...')

for i in range (10):
  st.write('Saya tidak akan nakal lagi')
