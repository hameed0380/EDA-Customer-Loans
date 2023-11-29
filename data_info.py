import pandas as pd

class DataFrameInfo:
    ''' To generate useful information about your DataFrame'''
    
    def __init__(self, df) -> None:
        self.df = df

    def describe(self):
        '''
        Returns the statistical information about the dataframe
        '''
        return self.df.describe()
    
    def get_median(self, column=None):
        '''
        Prints median of a numeric column.
        If column not provided, it prints median of the whole dataframe for all numeric columns.
        '''
        if column != None:
            print(self.df[column].median(numeric_only=True))
        else:
            print(self.df.median())

    def get_std(self, column=None):
        '''
        Prints std of numerical column.
        If column not provided, it prints the std of the whole df for all numerical columns.
        '''
        if column != None:
            print(self.df[column].std(numeric_only=True))
        else:
            print(self.df.std())

    def get_mean(self, column=None):
        '''
        Prints mean of a numeric column.
        If column not provided, it prints mean of the whole dataframe for all numeric columns.
        '''
        if column != None:
            print(self.df[column].mean(numeric_only=True))
        else:
            print(self.df.mean())

    def shape(self):
        '''
        Returns the shape of the method
        '''
        return self.df.shape
    
    def count_distinct_categories(self, column):
        if self.df[column].dtype == 'category':
            return self.df[column].value_counts() 
        else:
            print("This dtype is not a category dtype.\nMake sure to convert first.")

    def get_missing_values(self): 
        percent_missing = round(self.df.isnull().sum() * 100 / len(self.df), 2)
        missing_value_df = pd.DataFrame({'column_name': self.df.columns,
                                        'percent_missing': percent_missing})
        missing_value_df = missing_value_df.loc[missing_value_df["percent_missing"] != 0]
        # Only get columns that having missing values
        return missing_value_df