import numpy as np
import scipy.stats as stats

class SkewTransform:
    # TODO add Yeo Johnson transform

    def __init__(self, df):
        self.df = df
    
    def identify_skewed_columns(self, threshold=2):
        '''
        Function applies the .skew() method to each column the dataframe
        and returns a list of columns with a skew above a given threshold. 

        Threshold: The threshold value to filter the returned column list. 
        '''
        numerical_columns = self.df.select_dtypes(include=[np.number]).columns
        skewness = self.df[numerical_columns].apply(lambda n: n.skew())
        skewed_columns = skewness[abs(skewness) > threshold].index.tolist()
        return skewed_columns
    
    def transform_log(self, threshold=2):
        '''
        Function applies log transformation to list of skewed columns. Occurs inplace.

        Threshold: The threshold passed to the identify_skewed_columns() function.
        '''
        skewed_columns = self.identify_skewed_columns(threshold)
        for column in skewed_columns: 
            self.df[column] = self.df[column].map(lambda i: np.log1p(i) if i > 0 else 0)