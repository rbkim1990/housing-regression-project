from joblib import load
import streamlit as st
import pandas as pd
import score

# Streamlit page configuration on load
st.set_page_config(page_title = 'House Price Predictor',
                   page_icon = ':house:',
                   layout = 'wide',
                   initial_sidebar_state = 'expanded')

st.header('Predicting the Sale Price :house:')
st.write('A web app to predict sale price of a home given certain data points')

# grabbing input values for model
# default values are set to median of each distribution
overall_qual = st.sidebar.number_input(label = 'Rate the overall material and finish of the house from 1 (Poor) - 10 (Excellent)',
                                min_value = 1,
                                max_value = 10,
                                value = 6)

gr_liv_area = st.sidebar.number_input(label = 'Above grade (ground) living area square feet',
                                min_value = 1,
                                max_value = 6000,
                                value = 1464)

exter_qual = st.sidebar.number_input(label = 'Evaluate the quality of the material on the exterior from 1 (Poor) to 5 (Excellent)',
                                min_value = 1,
                                max_value = 5,
                                value = 3)


kitchen_qual = st.sidebar.number_input(label = 'Kitchen quality from 1 (Poor) to 5 (Excellent)',
                                min_value = 1,
                                max_value = 5,
                                value = 3)

garage_cars = st.sidebar.number_input(label = 'Size of garage in car capacity',
                                min_value = 0,
                                max_value = 5,
                                value = 2)

garage_area = st.sidebar.number_input(label = 'Size of garage in square feet',
                                min_value = 0,
                                max_value = 1500, 
                                value = 480)

bsmt_qual = st.sidebar.number_input(label = 'Evaluate the height of the basement from 0 (No Basement), 1 (<70 inches), 2 (70-79 inches), 3 (80-89 inches), 4 (90-99 inches), 5 (100+ inches)',
                                min_value = 0,
                                max_value = 5,
                                value = 4)

total_bsmt_sf = st.sidebar.number_input(label = 'Total square feet of basement area',
                                min_value = 0,
                                max_value = 7000, 
                                value = 992)

first_flr_sf = st.sidebar.number_input(label = 'First Floor square feet',
                                min_value = 0,
                                max_value = 5000, 
                                value = 1088)

full_bath = st.sidebar.number_input(label = 'Full bathrooms above grade',
                            min_value = 0,
                            max_value = 5,
                            value = 2)

garage_finish = st.sidebar.number_input(label = 'Interior finish of the garage from 0 (No Garage), 1 (Unfinished), 2 (Rough Finished), 3 (Finished)',
                                min_value = 0,
                                max_value = 3,
                                value = 2)

tot_rms_abv_grd = st.sidebar.number_input(label = 'Total rooms above grade (does not include bathrooms)',
                                    min_value = 0,
                                    max_value = 20,
                                    value = 6)

fireplace_qu = st.sidebar.number_input(label='Fireplace quality from 0 (No Fireplace), 1 (Poor - Ben Franklin Stove), 2 (Fair - Prefabricated Fireplace in basement), 3 (Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement), 4 (Good - Masonry Fireplace in main level), or 5 (Excellent - Exceptional Masonry Fireplace)',
                                min_value = 0,
                                max_value = 5,
                                value = 2)

year_built = st.sidebar.number_input(label = 'Original construction date',
                                min_value = 1800,
                                max_value = 2020,
                                value = 1973)

year_remod_add = st.sidebar.number_input(label = 'Remodel date (same as construction date if no remodeling or additions)',
                                    min_value = 1900,
                                    max_value = 2020,
                                    value = 1994)

# loading model and standard scaler
model = load('./models/linear_regression.joblib')
standard_scaler = load('./models/standard_scaler.joblib')

# converting input values into correct format (in this case, a DataFrame)
vals = pd.DataFrame([overall_qual, gr_liv_area, exter_qual, kitchen_qual, garage_cars, garage_area, bsmt_qual, total_bsmt_sf, first_flr_sf, full_bath, garage_finish, tot_rms_abv_grd, fireplace_qu, year_built, year_remod_add]).T
vals.columns = ['OverallQual', 'GrLivArea', 'ExterQual', 'KitchenQual', 'GarageCars', 'GarageArea', 'BsmtQual', 'TotalBsmtSF', '1stFlrSF', 'FullBath', 'GarageFinish', 'TotRmsAbvGrd', 'FireplaceQu', 'YearBuilt', 'YearRemodAdd']

# preprocessing input values
vals = score.preprocess(vals, standard_scaler)

# predicting on input values
pred = score.predict(vals, model)
st.write(f'## Sale Price predicted to be **${pred.loc[0, "SalePricePredictions"]:,}**')