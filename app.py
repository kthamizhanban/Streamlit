import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("Kanmani Thamizhanban")
st.subheader("Data Engineer")

col1,col2=st.columns([3,1])

with col1:
    st.subheader("About me")
    st.text("A skilled data engineer with proven expertise in using new \n tools and technical developments to drive improvements \n throughout an entire data lifecycle")
with col2:
    image=Image.open('Kanmani.jpeg')
    st.image(image,width=250)

    st.sidebar.caption('Wish to connect?')
    st.sidebar.write('raymondcy95@gmail.com')
    pdf_file=open('Resume.pdf','rb')
    st.sidebar.download_button('Download resume',pdf_file,file_name='Resume.pdf',mime='pdf')

st.subheader("Relevent Experience")
experience_table=pd.DataFrame ({
    "Job Title": ["Data Engineer","Application Development Specialist"],
    "Company": ["Accenture","IQVIA"],
    "Experience": ["3","2"]
})
experience_table=experience_table.set_index('Job Title')
st.table(experience_table)

st.subheader("Projects")
df=pd.read_csv('titanic.csv')

subjects=['English','Math','Science','Law','Chemistry']
scores=[55,97,67,86,94]
st.bar(subjects,scores,color='red',edgecolor='black')
#plt.xlabel('Subject',fontsize=12)
#plt.ylabel('Scores')
#plt.title('Student Scores')
st.show()