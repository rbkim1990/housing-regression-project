from joblib import load
import pandas as pd
import sys

cols_to_use = ['OverallQual', 'GrLivArea', 'ExterQual',
 'KitchenQual', 'GarageCars', 'GarageArea', 'BsmtQual', 'TotalBsmtSF',
 '1stFlrSF', 'FullBath', 'GarageFinish', 'TotRmsAbvGrd', 'FireplaceQu',
 'YearBuilt', 'YearRemodAdd']

def generic_conversion(val: str) -> int:
    '''
    Returns the corresponding numerical value to the categorical value.
    Input must be one of the five, 'Ex', 'Gd', 'TA', 'Fa', 'Po'.
    Outputs the corresponding int value based on the following scale.
    '''
    if val == 'Ex':
        return 5
    elif val == 'Gd':
        return 4
    elif val == 'TA':
        return 3
    elif val =='Fa':
        return 2
    else:
        return 1

def garage_finish(val: any) -> int:
    '''
    Returns the corresponding numerical value to the categorical value 
    specifically for the 'GarageFinish' column.
    Input must be one of 'Fin', 'RFn', 'Unf', 'NA'.
    Outputs the corresponding int value based on the following scale.
    '''
    if val == 'Fin':
        return 3
    elif val == 'RFn':
        return 2
    elif val == 'Unf':
        return 1
    else:
        return 0

def init():
    '''
    Initialize the model and the standard scaler function, 
    both of which are located in the models folder
    '''
    global model
    global standard_scaler
    model = load('./models/linear_regression.joblib')
    standard_scaler = load('./models/standard_scaler.joblib')

def preprocess(df: pd.DataFrame, standard_scaler) -> pd.DataFrame:
    '''
    Preprocess dataframe to limit columns for prediction, change categorical values to numerical values
    Input must be a dataframe that is like the trained dataset.
    Output will be a processed dataframe.
    '''
    # limit columns to those used by model, as well as correctly order dataframe
    df = df.copy()
    df = df[cols_to_use]

    # fill NaNs and apply categorical conversion for the relevant columns
    for col in ['ExterQual', 'KitchenQual', 'BsmtQual', 'FireplaceQu', 'GarageFinish']:
        df.loc[:, col] = df[col].fillna('None')
        if col == 'GarageFinish':
            df.loc[:, 'GarageFinish'] = df['GarageFinish'].apply(garage_finish)
        else:
            df.loc[:, col] = df[col].apply(generic_conversion)

    # drop rows with any remaining NaNs
    df = df.dropna()

    # apply standard scaler to the dataframe
    df = pd.DataFrame(standard_scaler.transform(df), columns=cols_to_use)
    return df

def predict(df: pd.DataFrame, model) -> pd.DataFrame:
    '''
    Generates predictions on a dataframe that has been correctly preprocessed.
    Input must be a preprocessed dataframe with columns in correct order.
    Output will be a pandas Series of predicted 'SalePrice' 
    '''
    # generate predictions from the model
    preds = model.predict(df)

    # convert array to Series and round to two places
    preds_df = pd.DataFrame([round(x,2) for x in preds]).T

    # rename columns for readability
    preds_df.columns=['SalePricePredictions']

    # instantiate as a pandas Series and return
    return preds_df

def predict_with_ids(ids: pd.Series, df: pd.DataFrame, model) -> pd.DataFrame:
    '''
    Generates predictions on a dataframe that has been correctly preprocessed.
    Input must be a Series of ids and a preprocessed dataframe with columns in correct order.
    Output will be a pandas DataFrame of predicted 'SalePrice' 
    '''
    # generate predictions from the model
    preds = model.predict(df)

    # convert array to Series and round to two places
    preds = pd.Series([round(x,2) for x in preds])

    # combine ids series and prediction series
    preds_df = pd.DataFrame([ids, preds]).T

    # rename columns for readability
    preds_df.columns=['Id', 'SalePricePredictions']

    # convert dtype of the 'Id' column to be ints
    preds_df['Id'] = preds_df['Id'].astype(int)

    # instantiate as a pandas Series and return
    return preds_df

if __name__ == '__main__':
    '''
    Entry function if Python file is called from the command line.
    A path to the csv must be provided, 
    as well as an output path for the resulting predictions (which will be in csv format)
    '''
    # check to see if there are less arguments than are necessary
    if len(sys.argv) < 1:
        print('Enter path for csv')
        exit()
    elif len(sys.argv) < 2:
        print('Enter path for output predictions file')
    else:
        csv_path = sys.argv[1]
        output_path = sys.argv[2]
    
    # initiate the model
    init()

    # read the csv into a pandas DataFrame
    df = pd.read_csv(csv_path)
    ids = None
    if 'Id' in df.columns:
        ids = df['Id']
    print('Sucessfully read csv into a dataframe')
    print()

    # preprocess the DataFrame
    df = preprocess(df, standard_scaler)
    print('Successfully preprocessed the dataframe')
    print()

    # generate predictions
    if ids is None:
        preds = predict(df, model)
    else:
        preds = predict_with_ids(ids, df, model)
    print('Successfully generate predictions. First 5 "SalePrice" predictions:')
    print(preds[:5])
    print()

    # save predictions to the output path
    preds.to_csv(output_path, index=False)
    print(f'Successfully saved predictions to {output_path}. Exiting...')
    exit()