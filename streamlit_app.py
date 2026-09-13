import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px


# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="World Weather Dashboard",
    layout="wide"
)


# -----------------------------
# Load data from SQLite
# -----------------------------
conn = sqlite3.connect("weather.db")

df = pd.read_sql_query(
    "SELECT * FROM weather",
    conn
)

conn.close()


# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filter Weather Data")

min_temp = int(df["Temperature_F"].min())
max_temp = int(df["Temperature_F"].max())

temperature_range = st.sidebar.slider(
    "Temperature Range (°F)",
    min_value=min_temp,
    max_value=max_temp,
    value=(min_temp, max_temp)
)

cities = ["All Cities"] + sorted(df["City"].unique().tolist())

selected_city = st.sidebar.selectbox(
    "Select a City",
    cities
)


# -----------------------------
# Apply filters
# -----------------------------
filtered_df = df[
    (df["Temperature_F"] >= temperature_range[0]) &
    (df["Temperature_F"] <= temperature_range[1])
]

if selected_city != "All Cities":
    filtered_df = filtered_df[
        filtered_df["City"] == selected_city
    ]


# -----------------------------
# Dashboard title
# -----------------------------
st.title("World Weather Dashboard")

st.write(
    "Explore current temperatures and weather conditions "
    "for cities around the world. Use the filters in the sidebar "
    "to explore different temperature ranges and cities."
)


# -----------------------------
# Summary metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Cities Shown",
        len(filtered_df)
    )

with col2:
    if not filtered_df.empty:
        st.metric(
            "Average Temperature",
            f"{filtered_df['Temperature_F'].mean():.1f} °F"
        )
    else:
        st.metric(
            "Average Temperature",
            "N/A"
        )

with col3:
    if not filtered_df.empty:
        st.metric(
            "Highest Temperature",
            f"{filtered_df['Temperature_F'].max():.0f} °F"
        )
    else:
        st.metric(
            "Highest Temperature",
            "N/A"
        )


# -----------------------------
# Weather data table
# -----------------------------
st.subheader("Weather Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)


# -----------------------------
# Visualization 1
# Temperature by city
# -----------------------------
st.subheader("Temperature by City")

if not filtered_df.empty:

    temperature_chart = px.bar(
        filtered_df.sort_values("Temperature_F"),
        x="City",
        y="Temperature_F",
        color="Temperature_F",
        title="Current Temperature by City",
        labels={
            "City": "City",
            "Temperature_F": "Temperature (°F)"
        }
    )

    st.plotly_chart(
        temperature_chart,
        use_container_width=True
    )

else:
    st.warning(
        "No cities match the selected filters."
    )


# -----------------------------
# Visualization 2
# Temperature distribution
# -----------------------------
st.subheader("Temperature Distribution")

if not filtered_df.empty:

    temperature_histogram = px.histogram(
        filtered_df,
        x="Temperature_F",
        nbins=15,
        title="Distribution of Temperatures",
        labels={
            "Temperature_F": "Temperature (°F)"
        }
    )

    st.plotly_chart(
        temperature_histogram,
        use_container_width=True
    )


# -----------------------------
# Visualization 3
# Weather conditions
# -----------------------------
st.subheader("Weather Condition Frequency")

if not filtered_df.empty:

    condition_counts = (
        filtered_df["Condition"]
        .value_counts()
        .reset_index()
    )

    condition_counts.columns = [
        "Condition",
        "Count"
    ]

    condition_chart = px.bar(
        condition_counts,
        x="Condition",
        y="Count",
        title="Weather Conditions Across Cities",
        labels={
            "Condition": "Weather Condition",
            "Count": "Number of Cities"
        }
    )

    st.plotly_chart(
        condition_chart,
        use_container_width=True
    )


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.write(
    "Data source: Weather Around the World. "
    "Weather data was collected through web scraping, "
    "cleaned with Pandas, stored in SQLite, "
    "and visualized with Streamlit and Plotly."
)