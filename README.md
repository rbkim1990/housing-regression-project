
# Predicting House Prices in Ames, IA

![](https://livability.com/sites/default/files/1Reiman%20Gardens.JPG)
_Courtesy of the Ames Chamber of Commerce_

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

### Data Dictionary
|**Feature**|**Type**|**Description**|
|---|---|---|
|Id | int |  Observation number |
|PID| int |  Parcel identification number  - can be used with city web site for parcel review. |
|MS SubClass| int | Identifies the type of dwelling involved in the sale.	|
|MS Zoning| obj | Identifies the general zoning classification of the sale. |
|Lot Frontage| float | Linear feet of street connected to property. |
|Lot Area| float | Lot size in square feet. |
|Street| obj| Type of road access to property. |
|Alley| obj | Type of alley access to property. |
|Lot Shape| obj | General shape of property. |
|Land Contour| obj | Flatness of the property. |
|Utilities| obj | Type of utilities available. |
|Lot Config| obj | Lot configuration. |
|Land Slope| obj | Slope of property. |
|Neighborhood| obj | Physical locations within Ames city limits. |
|Condition 1| obj | Proximity to various conditions. |
|Condition 2| obj | Proximity to various conditions (if more than one is present). |
|Bldg Type| obj | Type of dwelling. |
|House Style| obj | Style of dwelling.|
|Overall Qual| obj | Rates the overall material and finish of the house. |
|Overall Cond| obj | Rates the overall condition of the house. |
|Year Built| int | Original construction date. |
|Year Remod/Add| int | Remodel date (same as construction date if no remodeling or additions).|
|Roof Style| obj | Type of roof.|
|Roof Matl| obj | Roof material.|
|Exterior 1| obj | Exterior covering on house.|
|Exterior 2| obj | Exterior covering on house (if more than one material).|
|Mas Vnr Type| obj | Masonry veneer type.|
|Mas Vnr Area| obj | Masonry veneer area in square feet. |
|Exter Qual| obj | Evaluates the quality of the material on the exterior.|
|Exter Cond| obj | Evaluates the present condition of the material on the exterior.|
|Foundation| obj | Type of foundation.|
|Bsmt Qual| obj | Evaluates the height of the basement. |
|Bsmt Cond| obj | Evaluates the general condition of the basement. |
|Bsmt Exposure| obj | Refers to walkout or garden level walls. |
|BsmtFin Type 1| obj | Rating of basement finished area. |
|BsmtFin SF 1| float | Type 1 finished square feet. |
|BsmtFinType 2| obj | Rating of basement finished area (if multiple types).|
|BsmtFin SF 2| float | Type 2 finished square feet.|
|Bsmt Unf SF| float | Unfinished square feet of basement area.|
|Total Bsmt SF| float | Total square feet of basement area.|
|Heating| obj | Type of heating.|
|HeatingQC| obj | Heating quality and condition.|
|Central Air| obj | Central air conditioning.|
|Electrical| obj |  Electrical system.|
|1st Flr SF| float | First Floor square feet. | 
|2nd Flr SF| float | Second floor square feet. |
|Low Qual Fin SF| float | Low quality finished square feet (all floors).|
|Gr Liv Area| float | Above grade (ground) living area square feet.|
|Bsmt Full Bath| int | Basement full bathrooms.|
|Bsmt Half Bath| int | Basement half bathrooms.|
|Full Bath| int | Full bathrooms above grade.|
|Half Bath| int | Half baths above grade.|
|Bedroom| int | Bedrooms above grade (does NOT include basement bedrooms). |
|Kitchen| int | Kitchens above grade.|
|KitchenQual| obj | Kitchen quality.|
|TotRmsAbvGrd| int |	Total rooms above grade (does not include bathrooms).|
|Functional| obj | Home functionality (Assume typical unless deductions are warranted).|
|Fireplaces| int | Number of fireplaces. |
|FireplaceQu| obj | Fireplace quality. |
|Garage Type| obj | Garage location. |
|Garage Yr Blt| int | Year garage was built.|	
|Garage Finish| obj | Interior finish of the garage.|
|Garage Cars| int | Size of garage in car capacity. |
|Garage Area| float |  Size of garage in square feet.|
|Garage Qual| obj | Garage quality. |
|Garage Cond| obj | Garage condition.|
|Paved Drive| obj | Paved driveway. |
|Wood Deck SF| float | Wood deck area in square feet. |
|Open Porch SF| float | Open porch area in square feet. |
|Enclosed Porch| float | Enclosed porch area in square feet. |
|3-Ssn Porch| float | Three season porch area in square feet. |
|Screen Porch| float | Screen porch area in square feet. |
|Pool Area| float | Pool area in square feet. |
|Pool QC| obj| Pool quality.|
|Fence| obj | Fence quality. |
|Misc Feature| obj | Miscellaneous feature not covered in other categories.|
|Misc Val| float | $Value of miscellaneous feature.|
|Mo Sold| int | Month Sold (MM).|
|Yr Sold| int | Year Sold (YYYY).|
|Sale Type| obj | Type of sale. |
|Sale Condition| obj | Condition of sale.|
|SalePrice| float| Sale price $$.|

### Repository Structure
**Folders**
- data : Data files created and needed for project.
- images : Image files that either have been produced by the project for presentation or other images added to presentation.
- notebooks : Notebooks used to clean, analylze, and model predictions here.
- submissions : CSV files used to submit predictions to Kaggle.

**Notebooks**  
There are 12 notebooks, each of them serving one or more of the following purposes:
- Cleaning and resolving null values
- Organizing data by categorical and numerical features
- Exploratory data analysis
- Modeling

**Other Files**
- Presentation.pdf: Presentation for Non-Technical Audience

### Executive Summary
The project started with a need to clean the data. The Ames dataset, while very detailed, also has some issues of missing values. Using the MissingNo library, I was able to located the missing (null) values and visually represent them on the notebook. Most of the missing values were due to the fact that the Ames dataset uses "NA" to describe a feature that is lacking (ie. garage quality when there is no garage). Knowing that this would cause errors in the later models that I was to use, I filled the "NA" values with "None". These entries consisted about 90% of the missing data. Other entries, however, were more technically challenging to resolve. For the column "Lot Frontage", there were many missing values for no known reason. I used a linear regression model on a related column, "Lot Area", to predict the values for "Lot Frontage." This allowed me to have a good estimate of what the "Lot Frontage" should be while keeping the data's integrity (without deleting or dismissing data).  

I next decided to do some basic exploratory data analysis (EDA) with a correlation heatmap and a few histograms. I spent the least amount of time on this portion of the project although, in retrospect, I should have spent more time getting to know the data intimately. I ended my EDA with a list of numerical features that had the highest correlation to "SalePrice" in the training data.

I divided the data into categorical and numerical features. I created a few basic models with the cleaned data, until I realized that some of the categorical features could be converted to a numerical scale (ie. the features that ranked quality from Excellent to Poor). I also realized that one of the numerical features "MS SubClass" used numbers to categorize types of houses, and should be joined with the categorical features. I cleaned up the data a little bit more and then continued the modeling process.

Throughout the many models created, I tried a variety of tecniques to help with feature engineering and selection. I used the Polynomial Features function on my numerical columns to get all the interaction and squared terms of each feature. I also one-hot encoded the categorical features. That totalled to a lot of features! I had to come up with a few different ways to select the best features.  

I mainly used the Lasso regression technique to root out the features that have the least impact on the accuracy of the model (I used the R2 score mainly to determine the veracity of my predictions). I also used the Recursive Feature Elimination (RFE) technique to figure out the best coefficients to use on my model. I also tried my hand in a little bit of Grid Searching to tune the hyperparameters of the ElasticNet regression technique. With all that being said and done, each model came up with something a little bit different, with varying R2 scores. I achieved a model with a R2 score of 0.92, but was still left wondering if there wasn't a better way to approach this problem effecitively.

In hindsight, I realized that there are other factors that are just as important as being able to use modeling techniques effectively. I realized that having the subject matter expertise to inform modeling can be a great insight to more effective predictions. Furthermore, it goes without saying that having experience in modeling is also critical to achieving good predicitons. With that being said, this project was a significant learning experience for me as I grow as a better Data Scientist.
