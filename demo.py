import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("Persian cats")
  st.image("./Perasian.jpeg",caption="Persian Cat",width=300,use_column_width=true)
  st.write("Persian cats are cute")
with col2:
  st.subheader("Ragdoll Cat")
  st.image("./ragdoll.webp",caption="Ragdoll Cat",width=300,use_column_width=true)
  st.write("Ragdoll cats are proud")
