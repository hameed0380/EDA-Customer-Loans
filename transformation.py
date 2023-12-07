import pandas as pd
from scipy import stats
from data_info import DataFrameInfo


class DataTransformation:
    ''' 
    Class to handle the conversion of different columns in the dataframe.
    '''

    def __init__(self, df):
        self.df = df


    def dates_conversion(self, date_column):
        '''
        Convert pandas object dtype into a pandas datetime dtype.
        
        date_column: name of the pandas dataframe column to be converted.
        '''
        # for formats that use short form followed by year
        self.df[date_column] = pd.to_datetime(self.df[date_column], format="%b-%Y")
        return self.df
    
    def convert_term_float(self, term_column):
        ''' 
        Convert the 'term' column to float format. 

        term_column: name of the pandas dataframe column to be converted to float.
        '''
        # extract the digits and converts to float
        self.df[term_column] = self.df[term_column].str.extract('(\d+)', expand=False).astype(float)
        return self.df
    
    def convert_categorical(self, cat_column):
        '''
        Converting column to categorical dtype and returns updated df

        cat_colum: name of the pandas dataframe column to be converted to category dtype
        '''
        self.df[cat_column] = self.df[cat_column].astype('category')
        return self.df
    
    def convert_cat_to_numerical(self, category_column):
        '''
        Converting categorical columns to numerical columns

        category_column: name of the pandas df column being converted to numerical
        '''
        self.df[category_column] = self.df[category_column].factorize()[0]
        self.df[category_column] = self.df[category_column] + 1
        return self.df
    
    def convert_to_float(self, column):
        '''
        Converts column to float dtype

        column: name of the pandas df column being converted
        '''
        self.df[column] = self.df[column].astype(float)
        return self.df

    def drop_column(self, column):
        '''
        Returns dropped columns

        column: name of the pandas df column being dropped
        '''
        return self.df.drop(column, axis=1, inplace=True)
    
    def impute_columns(self, column, impute_type):
        '''
        Imputes DataFrame columns. 
        Must decide whether to impute column with the median or the mean and impute the NULL values. 
        
        column: name of the pandas df column being imputed
        impute_type: whether to impute median or mean
        '''
        if impute_type == "median":
            self.df[column].fillna(self.df[column].median(), inplace=True)
        elif impute_type == "mean":
            self.df[column].fillna(self.df[column].median(), inplace=True)
        else:
            print("Please enter a valid imputation method.\n Either median or mean.")
        return self.df
    