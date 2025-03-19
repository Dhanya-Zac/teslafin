import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

class LogTransform:
    def __init__(self, dataframe, freq=None):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()
        self.freq = freq

    def decompose(self, model='multiplicative'):
        if self.freq is None:
            raise ValueError("Frequency must be set for decomposition.")

        if "closing_price" not in self.df.columns:
            raise KeyError("DataFrame must contain 'closing_price' column")

        result = seasonal_decompose(self.df['closing_price'], model=model, period=self.freq)
        result.plot()
        plt.show()

    def histogram(self, bins=50):
        if "log_closing_price" not in self.df.columns:
            raise KeyError("DataFrame must contain 'log_closing_price' column. Run transform_data() first.")

        plt.figure(figsize=(10, 6))
        plt.hist(self.df['log_closing_price'], bins=bins, edgecolor='black', alpha=0.7)
        plt.title('Histogram of Log-Transformed Tesla Stock Data', fontsize=16)
        plt.xlabel('log_closing_price', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()

    def transform_data(self):
        """
        Apply log transformation to the closing price data.

        Returns:
            pd.DataFrame: DataFrame with the log-transformed 'closing_price' column added.
        """
        if "closing_price" not in self.df.columns:
            raise KeyError("DataFrame must contain 'closing_price' column")

        # Avoid log(0) errors
        self.df["log_closing_price"] = np.log(self.df["closing_price"].replace(0, np.nan))

        return self.df
