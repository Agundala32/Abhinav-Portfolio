import streamlit as st, pickle, numpy as np, xgboost as xgb, warnings
warnings.filterwarnings('ignore')

with open('xgboost_model.pkl', 'rb') as file:
    model = pickle.load(file=file)

st.title('Energy Production Predictor')
st.subheader('Enter Input Parameters:')

temperature = st.number_input('Temperature', min_value=-20.0, max_value=40.0, value=30.0)
exhaust_vacuum = st.number_input('Exhaust Vacuum', min_value=25.0, max_value=85.0, value=70.0)
amb_pressure = st.number_input('Ambient Pressure', min_value=985.0, max_value=1035.0, value=1000.0)
r_humidity = st.number_input('Relative Humidity', min_value=20.0, max_value=100.0, value=50.0)

if st.button('Predict Energy Production'):
    try:
        # Create input array
        input_data = np.array([[temperature, exhaust_vacuum, amb_pressure, r_humidity]])

        # Make prediction
        prediction = model.predict(input_data)

        # Display prediction
        st.success(f'Predicted Energy Production: {prediction[0]:.2f} MW')
    except Exception as e:
        st.error(f'An error occurred: {str(e)}')

st.sidebar.markdown('''
### About
This app predicts energy production based on environmental parameters using an XGBoost model.
''')

# Install streamlit if not already installed
# !pip install streamlit  # This line is now commented out as it's only needed for initial setup


# Load the pre-trained XGBoost model

# Set the title and subheader of the Streamlit app

# Create number input widgets for the user to enter input parameters



# Create a button to trigger the prediction

    # Create input array from user inputs

    # Initialize a StandardScaler for feature scaling

    # Fit and transform the input data using the scaler

    # Make a prediction using the loaded XGBoost model

    # Display the prediction to the user

    # Handle potential errors during prediction


# Add a sidebar with information about the app



"""##
This Streamlit app predicts energy production using an XGBoost model.  Users input temperature, exhaust vacuum, ambient pressure, and relative humidity. The app then scales the input using `StandardScaler` and predicts energy production using a pre-loaded XGBoost model (`xgboost_model.pkl`). The prediction, displayed in MW, is shown to the user.  Error handling is included. A sidebar provides a brief description of the app.

"""

