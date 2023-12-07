import pandas as pd
import numpy as np
from scipy import stats

class SkewTransform:
    def __init__(self, df):
        self.df = df

    def boxcox_transform(self, column):

        skew = stats.skew(self.df[column])
        if skew > 1:
            boxcox_sample = self.df[column]
            
            boxcox_transform = stats.boxcox(boxcox_sample)
            boxcox_transform = pd.Series(boxcox_transform[0])
            self.df[column] = boxcox_transform

        
    def yeojohnson_transform(self, column):

        yeojohnson_transform = self.df[column]
        yeojohnson_transform = stats.yeojohnson(yeojohnson_transform)
        yeojohnson_transform = pd.Series(yeojohnson_transform[0])
        self.df[column] = yeojohnson_transform
