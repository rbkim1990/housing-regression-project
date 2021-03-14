
# Predicting House Prices with the Ames, IA Dataset
![](https://livability.com/sites/default/files/1Reiman%20Gardens.JPG)
_Courtesy of the Ames Chamber of Commerce_

#### Using the Streamlit Web App
1. Clone locally
2. Navigate to project folder in CLI
3. `pip install requirements.txt'
4. `streamlit run SalePricePredictor.py`

### Background Information
The Ames, IA housing data is an especially robust and detailed data set that provides ample opportunity to practice linear regression techniques. Coupled with the need to increase subject-matter expertise, the housing data allowed for development of good data science practices in general.

### Goal
The goal of this project is to determine what features are most important in predicting the price of a house in the Ames market. Furthermore, we want to develop a linear regression model that achieves high accuracy of prediction (on the train data itself).

### Project Outline
1. Import Ames Housing data
2. Clean the data (mostly resolving null values)
3. Perform Exploratory Data Analysis to have a basic idea of important features
4. Create a linear regression model that is highly accurate (using the R2 and RMSE scores) to predict sale price
5. Analyze model to see what the most important features are, and present findings to stakeholders

### Data Dictionary of final features in model
|**Feature**|**Type**|**Description**|
|---|---|---|
|Overall Qual| obj | Rates the overall material and finish of the house. |
|Year Built| int | Original construction date. |
|Year Remod/Add| int | Remodel date (same as construction date if no remodeling or additions).|
|Exter Qual| obj | Evaluates the quality of the material on the exterior.|
|Bsmt Qual| obj | Evaluates the height of the basement. |
|Total Bsmt SF| float | Total square feet of basement area.|
|1st Flr SF| float | First Floor square feet. | 
|Gr Liv Area| float | Above grade (ground) living area square feet.|
|Full Bath| int | Full bathrooms above grade.|
|KitchenQual| obj | Kitchen quality.|
|TotRmsAbvGrd| int |	Total rooms above grade (does not include bathrooms).|
|FireplaceQu| obj | Fireplace quality. |
|Garage Finish| obj | Interior finish of the garage.|
|Garage Cars| int | Size of garage in car capacity. |
|Garage Area| float |  Size of garage in square feet.|

### Repository Structure
**Folders**
- datasets : Datasets from Kaggle, as well as cleaned datasets produced from notebook and a data dictionary.
- images : Image files that have been produced by the project for presentation.
- models : Persisted models and other functions for inference and deployment.
- notebooks : Notebooks used to clean, analylze, and model predictions here.

**Notebooks**  
There are 2 notebooks with following purposes:
- Cleaning and resolving null values, as well as other preprocessing
- Modeling

**Other Files**
- Presentation.pdf: Presentation for Non-Technical Audience
- SalePricePredictor.py: Streamlit Web App for interactive predictions
- score.py: Python file for batch inferencing
  - `python score.py <dataset_file_path> <output_csv_file_path>'

### Executive Summary
The project started with a need to clean the data. The Ames dataset, while very detailed, also has some issues of missing values. Using the MissingNo library, I was able to located the missing (null) values and visually represent them on the notebook. Most of the missing values were due to the fact that the Ames dataset uses "NA" to describe a feature that is lacking (ie. garage quality when there is no garage). Knowing that this would cause errors in the later models that I was to use, I filled the "NA" values with "None". These entries consisted about 90% of the missing data. Other entries, however, were more technically challenging to resolve. For the column "Lot Frontage", there were many missing values for no known reason. I used a linear regression model on a related column, "Lot Area", to predict the values for "Lot Frontage." This allowed me to have a good estimate of what the "Lot Frontage" should be while keeping the data's integrity (without deleting or dismissing data).  

I next decided to do some basic exploratory data analysis (EDA) with a correlation heatmap and a few histograms. I spent the least amount of time on this portion of the project although, in retrospect, I should have spent more time getting to know the data intimately. I ended my EDA with a list of numerical features that had the highest correlation to "SalePrice" in the training data.

I divided the data into categorical and numerical features. I created a few basic models with the cleaned data, until I realized that some of the categorical features could be converted to a numerical scale (ie. the features that ranked quality from Excellent to Poor). I also realized that one of the numerical features "MS SubClass" used numbers to categorize types of houses, and should be joined with the categorical features. I cleaned up the data a little bit more and then continued the modeling process.

Throughout the many models created, I tried a variety of tecniques to help with feature engineering and selection. I used the Polynomial Features function on my numerical columns to get all the interaction and squared terms of each feature. I also one-hot encoded the categorical features. That totalled to a lot of features! I had to come up with a few different ways to select the best features.  

I mainly used the Lasso regression technique to root out the features that have the least impact on the accuracy of the model (I used the R2 score mainly to determine the veracity of my predictions). I also used the Recursive Feature Elimination (RFE) technique to figure out the best coefficients to use on my model. I also tried my hand in a little bit of Grid Searching to tune the hyperparameters of the ElasticNet regression technique. With all that being said and done, each model came up with something a little bit different, with varying R2 scores. I achieved a model with a R2 score of 0.92, but was still left wondering if there wasn't a better way to approach this problem effecitively.

In hindsight, I realized that there are other factors that are just as important as being able to use modeling techniques effectively. I realized that having the subject matter expertise to inform modeling can be a great insight to more effective predictions. Furthermore, it goes without saying that having experience in modeling is also critical to achieving good predicitons. With that being said, this project was a significant learning experience for me as I grow as a better Data Scientist.
