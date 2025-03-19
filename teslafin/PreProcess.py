import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas.plotting as pd_plot

class PreProcess:
    """
    Handles preprocessing of Tesla stock data.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()

    def preprocess(self):
        """
        Convert 'Year' column to datetime and extract month and year.
        """
        self.df["Year"] = pd.to_datetime(self.df["Year"], errors='coerce')
        self.df.dropna(subset=["Year"], inplace=True)  # Remove invalid dates
        self.df["Month"] = self.df["Year"].dt.month
        self.df["Year_Num"] = self.df["Year"].dt.year
        return self.df
    def handle_missing_values(self):
        """
        Handle missing values by filling them with the previous value.
        """
        self.df.fillna(method='ffill', inplace=True)
        return self.df

    def remove_duplicates(self):
        """
        Remove duplicate rows.
        """
        self.df.drop_duplicates(inplace=True)
        return self.df
