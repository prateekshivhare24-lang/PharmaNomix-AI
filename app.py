import streamlit as st
from google import genai

# Initialize the client securely using your working API Key
client = genai.Client(api_key="AQ.Ab8RN6Kr-TY7C1Dor0JMtg332aHv8GCWhe92QHKGgLuvdfm9Yg")

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

# Your customized tagline
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
                # Prompt Engineering - Instructing the AI to return everything in English
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
                
                # Requesting a response from the updated model
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                # Displaying the final English results on the screen
                st.success("Here are 10 excellent names for you:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Something went wrong: {e}. Please check your connection or setup.")