import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of cat")
col1,col2=st.columns(2)
with col1:
  st.subheader("persian cat")
  st.image("./perasian.jpeg",caption="French Bulldogs",width=300,use_column_width=True)
  st.write("French Bulldogs are cute")
with col2:
  st.subheader("ragdoll cat")
  st.image("./ragdoll.webp",caption="Golden Retriver",width=300,use_column_width=True)
  st.write("Golden Retriver dogs are cute")
