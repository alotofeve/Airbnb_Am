import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="centered")

# Display title and text
st.title("Amsterdam visit: ")
st.subheader("Museums and nearby airbnb housing")
st.markdown("With a limited budget, the price above €100 /night are excluded")

st.subheader("Rijksmuseum")
st.image('Rijksmuseum.jpg')
st.write("Rijksmuseum ticket [link](https://www.rijksmuseum.nl/en/visit/practical-info/opening-hours-and-prices)")
# Read dataframe
dataframe1 = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_Rijksmuseum.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Distance (Meters)",
        "Location",
    ],
)

dataframe2 = dataframe1[dataframe1["Price"] <= 100]

# Display as integer
dataframe2["Airbnb Listing ID"] = dataframe2["Airbnb Listing ID"].astype(int)
# Round of values
dataframe2["Price"] = "€" + dataframe2["Price"].round(2).astype(str)
# Rename the number to a string
dataframe2["Location"] = dataframe2["Location"].replace(
    {1.0: "Rijksmuseum", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe2)
st.markdown("Below is a map showing all the Airbnb listings and the location of Rijksmuseum")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe2,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Distance (Meters)", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe2.iloc[0][2], lon=dataframe2.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)


st.subheader("Van Gogh Museum")
st.image('van-gogh-museum.jpg')
st.write("Van Gogh Museum ticket [link](https://www.vangoghmuseum.nl/en/visit/tickets-and-ticket-prices)")
# Read dataframe
dataframe3 = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_VanGoghmuseum.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Distance (Meters)",
        "Location",
    ],
)

dataframe4 = dataframe3[dataframe3["Price"] <= 100]

# Display as integer
dataframe4["Airbnb Listing ID"] = dataframe4["Airbnb Listing ID"].astype(int)
# Round of values
dataframe4["Price"] = "€" + dataframe4["Price"].round(2).astype(str)
# Rename the number to a string
dataframe4["Location"] = dataframe4["Location"].replace(
    {1.0: "Van Gogh Museum", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe4)
st.markdown("Below is a map showing all the Airbnb listings and the location of Van Gogh Museum")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe4,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Distance (Meters)", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe4.iloc[0][2], lon=dataframe4.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)
