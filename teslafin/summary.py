def _init_(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe

    def get_summary(self):
        #Returns mean, median, and standard deviation of the closing price of tesla stock dataset.
        assert "closing_price" in self.df.columns, "DataFrame must contain 'closing_price' column"
        return {
            "Mean": self.df["closing_price"].mean(),
            "Median": self.df["closing_price"].median(),
            "Std Dev": self.df["closing_price"].std(),
            "Min": self.df["closing_price"].min(),
            "Max": self.df["closing_price"].max(),
            "Quantiles": self.df["closing_price"].quantile([0.25, 0.5, 0.75]).to_dict()
        }
        
    def autocorrelation(self, last_lag=10): # Fixed: Corrected indentation

        #Calculate the Autocorrelation Function (ACF) of the closing prices for a range of lags.
        #Parameters: last_lag (int): Maximum lag value for which to compute ACF
        #Returns a dictionary with lag values as keys and their corresponding autocorrelation as values

        # Convert closing_price to numpy array
        series = self.df["closing_price"].values
        acf = {}

        # Calculate ACF for each lag from 1 to last_lag
        for lag in range(1, last_lag + 1):
            # Shift the series by lag, align it with the original series, and calculate correlation
            shifted_series = series[lag:]
            original_series = series[:-lag]

            # Calculate the correlation
            correlation = np.corrcoef(original_series, shifted_series)[0, 1]
            acf[lag] = correlation

        return acf
