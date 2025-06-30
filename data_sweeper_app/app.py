import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Application Data sweeper", layout="wide")

st.markdown("""
<h1 style='color:black; font-family:Arial;'>Streamlit Data sweeper app 🗑️🛠️</h1>
<h4 style='color:gray; font-family:mono; font-weight:bold;'>Clean, filter, and download your data easily 📀📊
</h4>   """, unsafe_allow_html=True)

# custom css
st.markdown(
    """
            <style>.stApp{
            background-color:;
            color:;
        
            }
            
            .features-heading {
            color: gray;
            font-family:poppins;
            font-size: 40px;
            margin-top:16px;
            margin-bottom:10px;
            
            }

            .features-text {
            color: gray; 
            }

             .stFileUploader label {
            color:white;
            font-size: 32px;  !important; 
            font-weight:800; !important; 
            }

            .error{
            color:white;
            font:bold;
            }

            .cleaning{
            color:#4169E1;
            font-family: 'Montserrat', sans-serif;
           font-size:32px;
           font-weight:bold;
        
            }

            .box-label{
            color:white;
            }
            </style>
            """,
    unsafe_allow_html=True,
)

st.markdown(
    """
     <div class="features-heading">   
   Features:
 </div>

 <div class = "features-text">    
✅ Upload CSV or Excel files  </br>
✅ Remove duplicates and missing values </br>
✅ Filter and sort data dynamically </br>
✅ Download the cleaned dataset instantly </div></br>""",
    unsafe_allow_html=True,
)

upload_Files = st.file_uploader(
    "Upload your CSV or EXCEL files here",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)

if upload_Files:
    for file in upload_Files:
        file_Extension = os.path.splitext(file.name)[-1]

        if file_Extension == ".csv":
            df = pd.read_csv(file)

        elif file_Extension == ".xlsx":
            df = pd.read_excel(file)

        else:
            st.markdown(
                f"""<div class ="error"> you uploaded unsupported file {file_Extension }""",
                unsafe_allow_html=True,
            )
            continue

    st.write(f"File Name : **{file.name}**")
    st.write(f"File Size : **{file.size}**")

    st.write("Extracting the top records from the DataFrame")
    st.dataframe(df.head())

    st.markdown(
        """<div class="cleaning">   
   🎫Data cleanings here!"
 
 </div>""",
        unsafe_allow_html=True,
    )
    
    if st.checkbox(f"clean data for {file.name}"):
       
        col1, col2 = st.columns(2)

        with col1:

         if st.button(f"Removing duplicates from {file.name}"):
            df.drop_duplicates(inplace=True)
            st.write("All duplicates removed")
            st.success("✅ Duplicates removed!")
            st.dataframe(df.head())


        with col2:
     
         if st.button(f" missing values for {file.name}"):
          numeric_cols = df.select_dtypes(include=["number"]).columns
          df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
          st.success("✅ Missing values filled!")
          st.dataframe(df.head())

        st.markdown("<h3 style='color:#4169E1; font-family:Arial;'>📊 Select columns</h3>", unsafe_allow_html=True)

        columns = st.multiselect(
            f"choose columns for {file.name}", df.columns, default=df.columns
        )

        df = df[columns]

        st.markdown("<h3 style='color:#4169E1; font-family:Arial;'>📊 Data Visualization</h3>", unsafe_allow_html=True)

        if st.checkbox(f"show visulaisation for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])

        
        # if st.checkbox(f"🛠️ Clean data for {file.name}"):
        #     col1, col2 = st.columns(2)  

            
        #     # Handling Missing Values here
        #     with col2:
        #         if st.button(f"📌 Fill Missing Values for {file.name}"):
        #             numeric_cols = df.select_dtypes(include=['number']).columns
        #             df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        #             st.success("✅ Missing values filled!")
        #             st.dataframe(df.head())
