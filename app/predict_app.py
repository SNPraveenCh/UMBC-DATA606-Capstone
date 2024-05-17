import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.preprocessing import OneHotEncoder

# Load the pre-trained model
with open('../notebooks/random_forest_model.pkl', 'rb') as f:
    model = joblib.load(f)

# Define function to preprocess user input
def preprocess_input(accommodates, bedrooms, bathrooms, number_of_reviews, review_scores_rating, beds, property_type, neighbourhood, city, room_type, bed_type, cancellation_policy, cleaning_fee):
    # Create DataFrame with user input
    input_data = pd.DataFrame({
        'accommodates': [accommodates],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'number_of_reviews': [number_of_reviews],
        'review_scores_rating': [review_scores_rating],
        'beds': [beds],
        'property_type': [property_type],
        'neighbourhood': [neighbourhood],
        'city': [city],
        'room_type': [room_type],
        'bed_type': [bed_type],
        'cancellation_policy': [cancellation_policy],
        'cleaning_fee': [cleaning_fee]
    })
    numerical_features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews','review_scores_rating','beds']
    categorical_features = ['property_type','neighbourhood','city','room_type','bed_type','cancellation_policy',
                        'cleaning_fee']

    # One-hot encode categorical features
    encoder = OneHotEncoder(sparse=False)
    encoded_categories = encoder.fit_transform(input_data[categorical_features])

    # Concatenate numerical features with encoded categorical features
    input_data_encoded = pd.concat([input_data[numerical_features], pd.DataFrame(encoded_categories, columns=encoder.get_feature_names_out(categorical_features))], axis=1)
    

    return input_data_encoded

# Define function to predict price range
def predict_price_range(input_data_encoded):
    # Make predictions
    prediction = model.predict(input_data_encoded)
    return prediction[0]

# Streamlit app
def main():
    st.title("Airbnb Price Range Prediction")
    st.write("Enter the details below to predict the price range:")

    # Get user inputs
    accommodates = st.number_input("Number of accommodates", min_value=1, max_value=16, step=1, value=1)
    bathrooms = st.number_input("Number of bathrooms", min_value=0.0, max_value=8.0, step=0.5, value=1.0)
    bedrooms = st.number_input("Number of bedrooms", min_value=0, max_value=10, step=1, value=1)
    beds = st.number_input("Number of beds", min_value=0, max_value=18, step=1, value=1)
    number_of_reviews = st.number_input("Number of reviews", min_value=0, step=1, value=0)
    review_scores_rating = st.number_input("Review scores rating", min_value=0, max_value=100, value=90)
    
    # Categorical features
    property_type = st.selectbox("Property type", ['Apartment', 'House', 'Cabin', 'Condominium', 'Dorm', 'Townhouse', 'Loft', 'Villa', 'Other'])
#     neighbourhood = st.text_input("Neighbourhood", "")
    city = st.selectbox("City", ['Boston','Chicago','DC','LA','NYC','SF' ])
    if city == 'Boston':
        neighbourhood = ['Downtown', 'Chinatown', 'Allston-Brighton', 'Financial District', 'Jamaica Plain', 'Back Bay' ]
    elif city == 'Chicago':
        neighbourhood = ['Lakeview', 'Logan Square', 'Lincoln Park', 'Loop', 'Wicker Park' ]
    elif city == 'DC':
        neighbourhood = ['Capitol Hill', 'Columbia Heights', 'Logan Circle', 'U Street Corridor', 'Dupont Circle', 'Adams Morgan']
    elif city == 'LA':
        neighbourhood = ['Mid-Wilshire', 'Hollywood', 'Long Beach', 'Venice', 'Santa Monica', 'Silver Lake']
    elif city == 'NYC':
        neighbourhood = ['Williamsburg', 'Bedford-Stuyvesant', 'Bushwick', 'Upper West Side', 'Harlem', 'Hells Kitchen', 'Upper East Side', 'Crown Heights', 'Astoria', ]
    elif city == 'SF':
        neighbourhood = ['Mission District', 'Richmond District', 'Bernal Heights', 'Noe Valley', 'SoMa', 'Sunnyside', 'Pacific Heights']
    neighbourhood = st.selectbox("Neighborhood", neighbourhood)
    room_type = st.selectbox("Room type", ['Entire home/apt', 'Private room', 'Shared room'])
    bed_type = st.selectbox("Bed type", ['Real Bed', 'Futon', 'Pull-out Sofa', 'Airbed', 'Couch'])
    cancellation_policy = st.selectbox("Cancellation policy", ['strict', 'moderate', 'flexible'])
    cleaning_fee = st.selectbox("Cleaning fee", ['True', 'False'])

    # Preprocess input data
    input_data = preprocess_input(accommodates, bedrooms, bathrooms, number_of_reviews, review_scores_rating, beds, property_type, neighbourhood, city, room_type, bed_type, cancellation_policy, cleaning_fee)

    # Make prediction
    if st.button("Predict"):
        prediction = predict_price_range(input_data)
        st.success(f"The predicted price range is: {prediction}")

if __name__ == "__main__":
    main()
