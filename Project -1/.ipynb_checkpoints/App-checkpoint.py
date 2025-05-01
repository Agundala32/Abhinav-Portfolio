{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "rBWbTmmU8_p9",
    "outputId": "e76af586-1350-48d6-c491-667a6fdbeba3"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in e:\\anaconda\\lib\\site-packages (1.39.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in e:\\anaconda\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\ritee\\appdata\\roaming\\python\\python311\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (2.2.3)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (10.2.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in e:\\anaconda\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in e:\\anaconda\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in e:\\anaconda\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in e:\\anaconda\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in e:\\anaconda\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in e:\\anaconda\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\ritee\\appdata\\roaming\\python\\python311\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog<6,>=2.1.5 in e:\\anaconda\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: jinja2 in e:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in e:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in e:\\anaconda\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\ritee\\appdata\\roaming\\python\\python311\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in e:\\anaconda\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\ritee\\appdata\\roaming\\python\\python311\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in e:\\anaconda\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in e:\\anaconda\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in e:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in e:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in e:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in e:\\anaconda\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in e:\\anaconda\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\ritee\\appdata\\roaming\\python\\python311\\site-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in e:\\anaconda\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in e:\\anaconda\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in e:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in e:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in e:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in e:\\anaconda\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in e:\\anaconda\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\ritee\\appdata\\roaming\\python\\python311\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "import numpy as np\n",
    "import xgboost as xgb\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "from sklearn.preprocessing import StandardScaler\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "GJB1O3QH9QPc"
   },
   "outputs": [],
   "source": [
    "\n",
    "model = pickle.load(open('xgboost_model.pkl', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "gr8LATqD9nQ5",
    "outputId": "0c1ca98f-b36c-437e-fb66-140fe7b2026e"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-29 00:32:08.046 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.470 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\ritee\\AppData\\Roaming\\Python\\Python311\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-10-29 00:32:08.470 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.470 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.470 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Energy Production Predictor')\n",
    "st.subheader('Enter Input Parameters:')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "n7m10Mjw9toW",
    "outputId": "e95d2d7f-e4b6-4852-d308-dbef6af09115"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-29 00:32:08.481 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.486 Session state does not function when running a script without `streamlit run`\n",
      "2024-10-29 00:32:08.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.489 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "temperature = st.number_input('Temperature', min_value=-20.0, max_value=40.0, value=20.0)\n",
    "exhaust_vacuum = st.number_input('Exhaust Vacuum', min_value=25.0, max_value=85.0, value=55.0)\n",
    "amb_pressure = st.number_input('Ambient Pressure', min_value=985.0, max_value=1035.0, value=1015.0)\n",
    "r_humidity = st.number_input('Relative Humidity', min_value=20.0, max_value=100.0, value=60.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "XHanvPpJ92t4",
    "outputId": "0a324b70-ffda-44ad-9497-50d2b2376723"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-29 00:32:08.503 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.503 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.503 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.503 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.503 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button('Predict Energy Production'):\n",
    "    input_data = np.array([[temperature, exhaust_vacuum, amb_pressure, r_humidity]])\n",
    "    scaler = StandardScaler()\n",
    "    input_scaled = scaler.fit_transform(input_data)\n",
    "    prediction = model.predict(input_scaled)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "SRCHQ7xw97YU",
    "outputId": "3dd54a48-93d0-464e-ff67-4710c92dff94"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-29 00:32:08.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button('Predict Energy Production'):\n",
    "    try:\n",
    "        # Create input array\n",
    "        input_data = np.array([[temperature, exhaust_vacuum, amb_pressure, r_humidity]])\n",
    "\n",
    "        # Scale the input\n",
    "        scaler = StandardScaler()\n",
    "        input_scaled = scaler.fit_transform(input_data)\n",
    "\n",
    "        # Make prediction\n",
    "        prediction = model.predict(input_scaled)\n",
    "\n",
    "        # Display prediction\n",
    "        st.success(f'Predicted Energy Production: {prediction[0]:.2f} MW')\n",
    "    except Exception as e:\n",
    "        st.error(f'An error occurred: {str(e)}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "hYC5Rnd99_3p",
    "outputId": "c30bf604-f4a2-4dbc-c002-b4107bdb2c5f"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-29 00:32:08.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 00:32:08.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=1, _parent=DeltaGenerator())"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.sidebar.markdown('''\n",
    "### About\n",
    "This app predicts energy production based on environmental parameters using an XGBoost model.\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "nXyl8e4P-1or"
   },
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "# Install streamlit if not already installed\n",
    "# !pip install streamlit  # This line is now commented out as it's only needed for initial setup\n",
    "\n",
    "\n",
    "# Load the pre-trained XGBoost model\n",
    "\n",
    "# Set the title and subheader of the Streamlit app\n",
    "\n",
    "# Create number input widgets for the user to enter input parameters\n",
    "\n",
    "\n",
    "\n",
    "# Create a button to trigger the prediction\n",
    "\n",
    "\n",
    "        # Create input array from user inputs\n",
    "\n",
    "        # Initialize a StandardScaler for feature scaling\n",
    "\n",
    "\n",
    "        # Fit and transform the input data using the scaler\n",
    "\n",
    "\n",
    "        # Make a prediction using the loaded XGBoost model\n",
    "\n",
    "\n",
    "        # Display the prediction to the user\n",
    "\n",
    "\n",
    "\n",
    "        # Handle potential errors during prediction\n",
    "\n",
    "\n",
    "# Add a sidebar with information about the app\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {
    "id": "BY-qHA3MAwj6"
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ok2NcAiqA2n_"
   },
   "source": [
    "##\n",
    "This Streamlit app predicts energy production using an XGBoost model.  Users input temperature, exhaust vacuum, ambient pressure, and relative humidity. The app then scales the input using `StandardScaler` and predicts energy production using a pre-loaded XGBoost model (`xgboost_model.pkl`). The prediction, displayed in MW, is shown to the user.  Error handling is included. A sidebar provides a brief description of the app.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {
    "id": "u4AO5_3WA4Q6"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
