import streamlit as st

def units(value,unit_from,unit_to):
    
    conversions = {
        "meter_centimeter":100,
        
        "centimeter_meter":0.01,

        "meter_kilometer":0.001,

        "kilometer_meter":1000,

        "mile_kilometer":1.609,

        "gram_kilogram":0.001,

        "kilogram_gram":1000,
        
        "mile_meter": 1609.34,

        "meter_mile":  0.000621371,

        "mile_centimeter": 160934,

        "centimeter_mile":  0.0000062137 
}

    key = f"{unit_from}_{unit_to}" 
    if key in conversions:
        conversion = conversions[key]
        return value * conversion 
    
    
    else: 
        return "Not supported!"
    
st.markdown("""<style> 
            .stApp{ background-color:#f8f9fa;}
            </style>""",unsafe_allow_html=True)    

st.markdown("<h1 style='color: blue;'>Unit Converter Application</h1>", unsafe_allow_html=True)


value = st.number_input("Enter tve value: ",min_value=1.0,step=1.0 )

unit_from = st.selectbox("Select the unit you are converting from :", ["meter","kilometer","kilogram","gram","centimeter","mile"])

unit_to = st.selectbox("Select the unit you are converting to ", ["kilometer","meter","kilogram","gram","centimeter","mile"])

if st.button("convert now"):
   
    result = units(value,unit_from,unit_to) # calling main function

    st.info(f"**Answer: {value} {unit_from} to {unit_to} = {result}** " )
    


    

    