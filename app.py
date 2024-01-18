import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt


#st.snow()
st.title("Kanmani Thamizhanban")
#color[your text]
st.subheader("Transforming big data into bigger opportunities!")
col1, col2= st.columns([2,1])
with col1:
    st.subheader("")
    st.subheader("About Me")
    st.text("Passionate about the power of data to drive insights\nand innovation, I am poised to apply my advanced data\nengineeringskills and extensive industry acumen to address concrete \nchallenges and derive actionable insights for\nstrategic decision-making.")
with col2:
    st.subheader("")
    st.subheader("")
    st.subheader("")
    image = Image.open('DE_image.jpeg')
    st.image(image,width = 200)


st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: raymondcy95@gmail.com')
#rb means converting pdf file to raw binary format
pdf_file = open('Kanmani Thamizhanban Resume 2024.pdf', 'rb')
st.sidebar.download_button('Download Resume',pdf_file,file_name='Kanmani Thamizhanban Resume 2024.pdf',mime='pdf')

tab_skills,tab_exp,tab_pro,tab_cont,tab_pic = st.tabs(['Skills','Experience','Projects','Contact Me',"Take a picture"])

with tab_exp:
    #Experience
    st.subheader("Relevant Experience")
    experience_table = pd.DataFrame({
            "Job Title":["Data Engineering Senior Analyst","Application Development Specialist","Data Engineering Associate"],
            "Company":["Accenture","IQVIA","Accenture"],
            "Job Description":["Providing expertise in data storage structures, data mining, and data cleansing","Collaborated with cross-functional teams to identify areas for process improvement and recommended data-driven solutions, reducing operational costs by 30%.","Meticulously processed 150 job postings/day on the University’s job portal (Navigator)"],
    })
    #experience_table = experience_table.set_index('Job Title')
    st.table(experience_table)
with tab_pro:
    #Projects GRID
    st.subheader("Academic Project- Analysis of Titanic Survivor Dataset")
    titanic_data = pd.read_csv('titanic.csv')
    interval = alt.selection_interval()
    scatter = alt.Chart(titanic_data).mark_point().encode(
        x = 'Age',
        y = 'Fare',
        color=alt.condition(interval,'Sex', alt.value('lightgray'))
    ).add_selection(
        interval
        ).properties(
            width=300,height=200)

    bar = alt.Chart(titanic_data).mark_bar().encode(
        x='sum(Survived):Q',
        y='Pclass:N',
        color='Pclass:N',
        ).properties(
            width=300,
            height=200
        ).transform_filter(
            interval
        )
    st.altair_chart(scatter | bar)
    st.subheader("Summary")
    st.write("The First part includes scatter plots and a heatmap for the relationship between fare, gender, and age. The second part includes a contingency table and a bar chart representing the relationship between passenger class and survival. By combining these analyses, we can gain a more comprehensive understanding of how different factors relate to survival and the relationships between fare, gender, and age in the Titanic dataset.")

with tab_skills:
    #Skills Section - In the form of a bar chart
    skill_data = pd.DataFrame(
        {
            "Skills Level":[70,90,80,90,90,70],
            "Skills":["Python","SQL","Scripting","Data_Modeling","Data_Profiling","Analytical"]
        })
    skill_data = skill_data.set_index('Skills')
    with st.container():
        st.subheader("Skills")
        st.bar_chart(skill_data)
    with st.expander("See More Skills"):
        st.write("● Data storage: Oracle, PostgreSQL, MySQL, SAP HANA, Microsoft SQL server\n ● Data Integration and ETL Tools: Informatica PowerCenter, Nexxus ETL, lnformatica Intelligent Cloud Services (IICS)\n ● Orchestration Tools: Git, AWS S3, MuleSoft Anypoint\n ● Programming Languages/softwares: Python, Jupyter Notebook\n ● Query Language: SQL\n ● Bl Tools: Microsoft Power Bl, Advanced Excel, Tableau- Basic\n ● Project Management Tools: Jira, SNOW\n ● Miscellaneous: Web scraping, Postman API, Splunk monitoring\n ● Unix/Powershell scripting\n ● Salesforce-Veeva CRM\n ● Performance improvement/tuning")

with tab_cont:
    # Streamlit form
    form = st.form('my_form')
    fullname = form.text_input(label='Enter your Full Name', value='')
    age = st.slider("Select your age")
    gender = st.radio("Select your gender",('Male','Female','Other'))
    message = form.text_area(label="Your Message", value='', height=100)
    terms = st.checkbox("Accept terms and condition")
    submit = form.form_submit_button(label='Submit')
    # Handle form submission
    if submit:
        if terms:
            st.success('Form Completed: Thankyou for visitng')
        else:
            st.error('Please accept the terms and conditions')
    st.write("Name",fullname,"Age: ",age,"Gender: ",gender,"Message",message)

    #Add a map
    # # Create a DataFrame with latitude and longitude columns
    data = {
        'Location': ['Kitchener', 'Waterloo', 'Guelph', 'Cambridge'],
        'LAT': [43.451639, 43.464258, 43.5467, 43.3616],
        'LON': [-80.492533, -80.520410, -80.2482, -80.3144]
        }
    df = pd.DataFrame(data)
    st.map(df)

with tab_pic:
    picture = st.camera_input("Take a picture with me")
    if picture:
        st.image(picture)
