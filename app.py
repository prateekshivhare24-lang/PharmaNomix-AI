import streamlit as st
from google import genai

# Streamlit Cloud के Secrets से API key को ऑटोमैटिक उठाने के लिए सेटअप
if "api_key" in st.secrets:
    SECRET_API_KEY = st.secrets["api_key"]
else:
    # लोकल कंप्यूटर पर बैकअप के लिए आपकी चाबी
    SECRET_API_KEY = "AQ.Ab8RN6Kr-TY7C1Dor0JMtg332aHv8GCWhe92QHKGgLuvdfm9Yg"

# Client को सही सीक्रेट की (Key) के साथ कनेक्ट करना
client = genai.Client(api_key=SECRET_API_KEY)

# Google SEO and Search Configuration Settings
st.set_page_config(
    page_title="PharmaNomix AI - Medical Naming Tool", 
    page_icon="💊",
    menu_items={
        'About': "PharmaNomix AI is an advanced naming engine developed by Prateek Shivhare to help medical store owners find names."
    }
)

# Website Header Title
st.title("💊 PharmaNomix AI")

# Tagline
st.caption("Developed by PRATEEK SHIVHARE")

st.write("Find unique and meaningful names for your new medical store or pharma startup.")

# Creating input fields for the user
store_type = st.selectbox(
    "Select Business Type:",
    ["Allopathic Medical Store", "Ayurvedic/Pharmacy", "Healthcare Startup", "Generic Medicine Shop"]
)

location = st.text_input("Enter your City/Location (e.g., Chhindwara):", placeholder="e.g. Nagpur, Chhindwara")
keywords = st.text_input("Any specific keywords you want in the name? (Optional):", placeholder="e.g. Cure, Med, Health, Care")

# Action triggered when the user clicks the button
if st.button("Generate Unique Names ✨"):
    if not location:
        st.warning("Please enter a city or location name.")
    else:
        with st.spinner("AI is thinking of the best names... Please wait..."):
            try:
                prompt = f"""
                You are an expert business naming assistant specialized in the pharmaceutical and healthcare industry.
                A user wants to open a "{store_type}" located in "{location}". 
                Additional preferred keywords are: "{keywords}".
                
                Please generate 10 unique, catchy, modern, and highly professional names in English.
                For each name, provide:
                1. The Name itself.
                2. A brief, meaningful explanation in clear, professional English explaining why this name is good and its branding meaning.
                3. A creative slogan/tagline for that name.
                
                Make sure the names sound professional and are easy to pronounce. Do not give generic or common names. Everything must be outputted in English.
                """
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                st.success("Here are 10 excellent names for you:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Something went wrong: {e}. Please check your connection or setup.")