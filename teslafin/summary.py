import pandas as pd
import numpy as np

class Summary:
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        assert "closing_price" in dataframe.columns, "DataFrame must contain 'closing_price' column"
        self.df = dataframe

    def summary(self):
        """
        Returns mean, median, and standard deviation of the closing price.
        Also includes min, max, and quantiles.
        """
        return {
            "Mean": self.df["closing_price"].mean(),
            "Median": self.df["closing_price"].median(),
            "Std Dev": self.df["closing_price"].std(),
            "Min": self.df["closing_price"].min(),
            "Max": self.df["closing_price"].max(),
            "Quantiles": self.df["closing_price"].quantile([0.25, 0.5, 0.75]).to_dict()
        }

    def autocorrelation(self, last_lag=10):
        """
        Calculates the Autocorrelation Function (ACF) of log-transformed closing prices.

        Parameters:
            last_lag (int): Maximum lag value for which to compute ACF.

        Returns:
            dict: Lag values as keys and their corresponding autocorrelation as values.
        """
        if "log_closing_price" not in self.df.columns:
            raise KeyError("DataFrame must contain 'log_closing_price' column. Run transform_data() first.")

        series = self.df["log_closing_price"].values
        acf = {}

        for lag in range(1, last_lag + 1):
            if len(series) <= lag:  # Ensure we have enough data
                break
            shifted_series = series[lag:]
            original_series = series[:-lag]
            correlation = np.corrcoef(original_series, shifted_series)[0, 1]
            acf[lag] = correlation

        return acf
