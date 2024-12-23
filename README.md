# PREDICTON-OF-HOUSE-PRICE-USING-ML-MODEL
The dataset contains information about real estate transactions in Chennai.

## App Link -
https://predicton-of-house-price-using-ml-model-daqhaaoezl2yv86xztgntt.streamlit.app/

## General Information:
Number of entries: 7109
Number of columns: 22

## Key Columns:
1. **PRT_ID:** Unique property identifier.
2. **AREA:** The area/location where the property is situated (e.g., Karapakkam, Anna Nagar).
3. **INT_SQFT:** The interior square footage of the property.
4. **DATE_SALE:** The date the property was sold.
5. **DIST_MAINROAD:** Distance of the property from the main road (in meters).
6. **N_BEDROOM:** Number of bedrooms in the property.
7. **N_BATHROOM:** Number of bathrooms in the property.
8. **N_ROOM:** Total number of rooms in the property.
9. **SALE_COND:** Sale condition (e.g., AbNormal, Family).
10. **PARK_FACIL:** Parking facility availability (Yes/No).
11.**DATE_BUILD:** The date the property was built.
12. **BUILDTYPE:** The type of building (e.g., Commercial, Residential).
13. **UTILITY_AVAIL:** Utilities available (e.g., AllPub, ELO).
14. **STREET:** Type of street access (e.g., Paved, Gravel).
15. **MZZONE:** Market zone classification (e.g., A, RH).
16. **QS_ROOMS, QS_BATHROOM, QS_BEDROOM, QS_OVERALL:** Quality scores for various property features.
17.**REG_FEE:** Registration fee for the property.
18. **COMMIS:** Commission charged for the property.
19. **SALES_PRICE:** The final sale price of the property.

## Supervised learning:
This column comes under the supervised learning and the dependent column is the Sales Price.
So I have used Regression model.

## Project Overview:

My project focuses on predicting house prices based on various features such as location, size, number of rooms, and other property-specific attributes. By utilizing the XGBoost regression model, I've aimed to capture complex relationships within the data to enhance prediction accuracy.

## Key Components:

**1. Data Preprocessing:**

Handling Missing Values: I've addressed missing data points, which is crucial for maintaining model performance.
Feature Encoding: Categorical variables have been encoded appropriately to make them suitable for the regression model.
Feature Scaling: Ensuring numerical features are scaled can improve model convergence and performance.

**2. Model Selection and Training:**

XGBoost Regression: I've chosen XGBoost, a robust ensemble learning method known for its efficiency and performance in regression tasks. 
Hyperparameter Tuning: Adjusting parameters to optimize the model's performance is a critical step in enhancing predictive accuracy.

**3. Model Evaluation:**

Performance Metrics: Utilizing metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared provides a comprehensive understanding of the model's accuracy and reliability.

**4. Deployment:**

Streamlit Application: Deploying the model via a user-friendly interface allows users to input property features and receive price predictions, demonstrating practical applicability.

## Observations:

Feature Engineering: The selection and transformation of features significantly impact model performance. Consider exploring additional features or interaction terms that might capture underlying patterns in the data.

Model Validation: Implementing cross-validation techniques can provide a more robust assessment of the model's performance and help in detecting overfitting.

Comparative Analysis: Evaluating other regression models alongside XGBoost, such as Linear Regression, Random Forest, or Neural Networks, could offer insights into the relative strengths and weaknesses of each approach for this specific dataset.

Documentation: Providing detailed explanations of your methodology, including data preprocessing steps, feature selection rationale, and hyperparameter choices, would enhance the reproducibility and clarity of your work.

## Conclusion:

My project demonstrates a solid application of machine learning techniques for house price prediction, with effective use of the XGBoost algorithm and deployment through a Streamlit app. 
