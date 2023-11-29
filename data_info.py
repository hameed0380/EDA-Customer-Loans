import pandas as pd

class DataFrameInfo:
    ''' To generate useful information about your DataFrame'''
    
    def __init__(self, df) -> None:
        self.df = df

    def describe(self):
        return self.df.describe()