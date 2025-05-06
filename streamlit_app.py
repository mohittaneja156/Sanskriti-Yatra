import streamlit as st
import pandas as pd

# Sample data for attractions
data = {
    "Attraction": [
        "Chand Baori", "Hawa Mahal", "The Root Bridges", "Skeletons of Roopkund Lake", 
        "Jal Mahal", "The Blue City of Jodhpur", "Ellora Caves", "Mahabat Maqbara"
    ],
    "Location": [
        "Abhaneri", "Jaipur", "Cherrapunjee", "Chamoli", 
        "Jaipur", "Jodhpur", "Verul", "Junagadh"
    ],
    "Description": [
        "Thousands of exquisitely carved stone water storage wells...",
        "The 953 windows undoubtedly make this the world’s most beautiful screened porch...",
        "Centuries-old bridges grown from tangled roots.",
        "A lake with hundreds of ancient skeletons surrounding it...",
        "More than half of this Indian palace is drowned...",
        "Once an indicator of social class...",
        "This complex of vertically-excavated Buddhist, Jain...",
        "This otherworldly palace-mausoleum complex..."
    ],
    "lat": [
        27.1469, 26.9934, 25.2986, 30.2217,
        26.2625, 26.2939, 20.0207, 21.5289
    ],
    "lon": [
        77.4200, 75.8267, 91.5822, 80.2006,
        75.8503, 73.1477, 75.2270, 70.9632
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app title
st.title("Explore India")

# Display map
st.subheader("Map of Attractions")
st.map(df[['lat', 'lon']])

# Display categories as buttons
st.subheader("Categories")
categories = {
    "Architecture": 100,
    "History & Culture": 71,
    "Temples": 56,
    "Sacred Spaces": 37,
    "Religion": 35,
    "History": 31,
    "Hinduism": 30,
    "Ruins": 27,
    "Forts": 23,
    "Architectural Oddities": 22,
    "Museums": 21,
    "Unique Restaurants & Bars": 4,
}
for category, count in categories.items():
    st.button(f"{category} ({count})")

# Display unusual attractions in a grid
st.subheader("Unusual Attractions in India")
cols = st.columns(4)
for idx, row in df.iterrows():
    with cols[idx % 4]:
        st.subheader(row['Attraction'])
        st.caption(row['Description'])
        st.text(f"Location: {row['Location']}")