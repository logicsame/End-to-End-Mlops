import streamlit as st
import numpy as np
from mlproject.pipeline.prediction import PredictionPipeline

def main():
    st.title("Wine Quality Prediction App")

    st.write("Enter the characteristics of the wine to predict its quality:")

    # Input fields
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=20.0, value=7.0)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=2.0, value=0.5)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=1.0, value=0.3)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=50.0, value=2.0)
    chlorides = st.number_input("Chlorides", min_value=0.0, max_value=1.0, value=0.08)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0, max_value=100, value=30)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0, max_value=300, value=100)
    density = st.number_input("Density", min_value=0.9, max_value=1.1, value=0.996)
    pH = st.number_input("pH", min_value=2.0, max_value=4.0, value=3.2)
    sulphates = st.number_input("Sulphates", min_value=0.0, max_value=2.0, value=0.5)
    alcohol = st.number_input("Alcohol", min_value=8.0, max_value=15.0, value=10.5)

    if st.button("Predict Wine Quality"):
        try:
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                    free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            st.success(f"The predicted wine quality is: {predict}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Something went wrong. Please check your inputs and try again.")

if __name__ == "__main__":
    main()