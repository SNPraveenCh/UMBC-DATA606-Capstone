import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt


# Load data with caching
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/SNPraveenCh/UMBC-DATA606-Capstone/main/data/Airbnb_Data_Updated.csv'
    df = pd.read_csv(url)
    return df

# Function to plot value counts
def plot_value_counts(df, column_name):
    values_count = df[column_name].value_counts().reset_index()
    values_count.columns = [column_name, 'count']
    chart = alt.Chart(values_count).mark_bar().encode(
        x=alt.X(column_name, sort='-y', axis=alt.Axis(labelAngle=0)),
        y='count'
    ).properties(
        title=f'Value Counts of {column_name}'
    )
    return chart

# Add a title to the web app
st.sidebar.title('Airbnb Data Visualization')

# Main content
st.title('Airbnb Data Visualization')

# Placeholder for main content
main_placeholder = st.empty()

# Display home page content by default


# Load data
df = load_data()

# Sidebar for selecting option
selected_option = st.sidebar.radio('Select Option', ['Home', 'Distribution of Price Range', 'Distribution of Listings by Host Identity','Histogram of Prices', 'Room Type Distribution by City' ,'Number of Reviews vs. Listing Price', 'Box Plot of Prices by Room Type','Correlation Matrix','Distribution of Listings by Room Type','Distribution of Listings by City','Average Price of Listings by City','Pie Chart of Room Types','Top Neighbourhoods with Highest Average Price'])

# Display content based on selected option
if selected_option == 'Home':
    main_placeholder.empty()  # Clear the placeholder
    st.write("## Background")
    st.write("### What is it about?")
    st.write("This dataset contains information related to Airbnb listings, offering valuable insights into various aspects of short-term rental properties. It includes details such as location, property type, amenities, pricing, and reviews, collected from Airbnb listings across different regions. This dataset presents an opportunity for data scientists and researchers to explore and analyze factors influencing Airbnb rental prices, understand market trends, and identify patterns in guest preferences and property characteristics. By leveraging this dataset, stakeholders in the hospitality industry can gain actionable insights to optimize pricing strategies, enhance guest experiences, and improve the overall efficiency of Airbnb hosting. Moreover, researchers can use this dataset to develop predictive models, recommendation systems, and other data-driven solutions aimed at improving decision-making processes and maximizing value for both hosts and guests in the Airbnb ecosystem.")
    st.write("### Why does it matter?")
    st.write("The dataset matters for several reasons. Firstly, it provides valuable insights into the dynamics of the short-term rental market, particularly through the lens of Airbnb listings. Understanding factors influencing rental prices and property characteristics can benefit various stakeholders, including property owners, travelers, and policymakers. Property owners can use the insights gained from the dataset to optimize pricing strategies, attract more guests, and maximize revenue. Travelers can make more informed decisions when selecting accommodations based on factors such as location, amenities, and pricing trends. Policymakers can leverage this data to develop regulations and policies that promote fair competition, consumer protection, and sustainable growth in the short-term rental industry. Overall, the dataset serves as a valuable resource for analyzing market trends, driving informed decision-making, and fostering innovation in the hospitality sector.")
    st.write("## Data")
    st.write("### Data Source")
    st.write("[Kaggle/airbnb-price-dataset](https://www.kaggle.com/datasets/rupindersinghrana/airbnb-price-dataset)")
    st.write("### Data Size")
    st.write("101.5 MB")
    st.write("### Data Shape")
    st.write("Rows: 74111, Columns: 29")
    st.write("### Time Period")
    st.write("2008 to 2017")
    with main_placeholder:
        st.write("Welcome to the Home Page")
        st.write("Explore the data by selecting an option from the sidebar.")
elif selected_option == 'Distribution of Price Range':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        st.subheader(f'Value Counts of price_range')
        st.altair_chart(plot_value_counts(df, 'price_range'), use_container_width=True)
elif selected_option == 'Histogram of Prices':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        st.subheader("Histogram of Prices")
        histogram = alt.Chart(df).mark_bar().encode(
            alt.X("price", bin=True),
            y='count()',
        ).properties(
            width=600,
            height=400,
            title="Histogram of Prices"
        )
        st.altair_chart(histogram)
elif selected_option == 'Box Plot of Prices by Room Type':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        st.subheader("Box Plot of Prices by Room Type")
        boxplot = alt.Chart(df).mark_boxplot().encode(
            x=alt.X('room_type', axis=alt.Axis(labelAngle=0)),
            y='price'
        ).properties(
            width=600,
            height=400,
            title="Box Plot of Prices by Room Type"
        )
        st.altair_chart(boxplot)
elif selected_option == 'Correlation Matrix':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        # Correlation Matrix
        st.subheader("Correlation Matrix")

        # Compute correlation matrix
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        correlation_matrix = numeric_df.corr()

        # Convert correlation matrix to long format
        corr_df = correlation_matrix.stack().reset_index()
        corr_df.columns = ['variable1', 'variable2', 'correlation']

        # Create heatmap using Altair
        heatmap = alt.Chart(corr_df).mark_rect().encode(
            x='variable1:N',
            y='variable2:N',
            color=alt.Color('correlation:Q', scale=alt.Scale(scheme='blueorange'))
        ).properties(
            width=600,
            height=400,
            title='Correlation Matrix'
        ).encode(
            tooltip=['variable1', 'variable2', alt.Tooltip('correlation', format='.2f')]
        )

        st.altair_chart(heatmap)
elif selected_option == 'Distribution of Listings by Room Type':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        st.subheader("Distribution of Listings by Room Type")
        room_type_counts = df['room_type'].value_counts().reset_index()
        room_type_counts.columns = ['Room Type', 'Count']
        bar_chart = alt.Chart(room_type_counts).mark_bar().encode(
            x='Room Type',
            y='Count',
            color=alt.Color('Room Type', legend=None)
        ).properties(
            width=600,
            height=400,
            title='Count of Listings by Room Type'
        )
        st.altair_chart(bar_chart)
elif selected_option == 'Distribution of Listings by City':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        st.subheader("Distribution of Listings by City")
        room_type_counts = df['city'].value_counts().reset_index()
        room_type_counts.columns = ['City', 'Count']
        bar_chart = alt.Chart(room_type_counts).mark_bar().encode(
            x=alt.X('City', axis=alt.Axis(labelAngle=0)),
            y='Count',
            color=alt.Color('City', legend=None)
        ).properties(
            width=600,
            height=400,
            title='Count of Listings by City'
        )
        st.altair_chart(bar_chart)
elif selected_option == 'Average Price of Listings by City':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        st.subheader("Average Price of Listings by City")
        avg_price_by_city = df.groupby('city')['price'].mean().reset_index()
        bar_chart = alt.Chart(avg_price_by_city).mark_bar().encode(
            x='city',
            y='price',
            color=alt.Color('city', legend=None),
            tooltip=['city', 'price']
        ).properties(
            width=600,
            height=400,
            title='Average Price by City'
        ).configure_axisX(labelAngle=0)  # Rotate x-axis labels
        st.altair_chart(bar_chart)
elif selected_option == 'Pie Chart of Room Types':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        st.subheader("Pie Chart of Room Types")
        room_type_counts = df['room_type'].value_counts().reset_index()
        room_type_counts.columns = ['Room Type', 'Count']
        pie_chart = alt.Chart(room_type_counts).mark_arc().encode(
            color='Room Type',
            tooltip=['Room Type', 'Count'],
            theta='Count'
        ).properties(
            width=400,
            height=400,
            title="Distribution of Room Types"
        )
        st.altair_chart(pie_chart)
elif selected_option == 'Distribution of Listings by Host Identity':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        # Count the number of listings by host identity
        host_identity_counts = df['host_identity_verified'].value_counts().reset_index()
        host_identity_counts.columns = ['Host Identity Verified', 'Count']

        # Create a pie chart
        pie_chart = alt.Chart(host_identity_counts).mark_arc().encode(
            color='Host Identity Verified',
            tooltip=['Host Identity Verified', 'Count'],
            theta='Count'
        ).properties(
            width=400,
            height=400,
            title="Distribution of Listings by Host Identity"
        )

        # Display the pie chart
        st.write("## Distribution of Listings by Host Identity")
        st.altair_chart(pie_chart)
elif selected_option == 'Number of Reviews vs. Listing Price':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        scatter_reviews_price = alt.Chart(df).mark_circle().encode(
        x='number_of_reviews',
        y='price',
        tooltip=['number_of_reviews', 'price']
        ).properties(
            width=600,
            height=400,
            title="Number of Reviews vs. Listing Price"
        )

        st.subheader("Number of Reviews vs. Listing Price")
        st.altair_chart(scatter_reviews_price)
elif selected_option == 'Room Type Distribution by City':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        room_type_by_city_counts = df.groupby(['city', 'room_type']).size().reset_index(name='count')
        bar_chart_room_type_city = alt.Chart(room_type_by_city_counts).mark_bar().encode(
            x=alt.X('city', axis=alt.Axis(labelAngle=45)),
            y='count',
            color='room_type',
            tooltip=['city', 'room_type', 'count']
        ).properties(
            width=600,
            height=400,
            title='Room Type Distribution by City'
        )

        st.subheader("Room Type Distribution by City")
        st.altair_chart(bar_chart_room_type_city)
elif selected_option == 'Top Neighbourhoods with Highest Average Price':
    main_placeholder.empty()  # Clear the placeholder
    with main_placeholder:
        # Calculate average price by neighbourhood and filter top 10
        top_neighbourhoods = df.groupby('neighbourhood')['price'].mean().nlargest(10).reset_index()

        # Create a horizontal bar chart
        bar_chart_neighbourhood_price = alt.Chart(top_neighbourhoods).mark_bar().encode(
            x='price:Q',
            y=alt.Y('neighbourhood:N', sort='-x'),
            tooltip=['neighbourhood:N', 'price:Q']
        ).properties(
            width=600,
            height=400,
            title='Top Neighbourhoods with Highest Average Price'
        )
        st.subheader("Top Neighbourhoods with Highest Average Price")
        st.altair_chart(bar_chart_neighbourhood_price)


