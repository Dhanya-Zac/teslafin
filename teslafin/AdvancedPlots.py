class AdvancedPlots:
    """
    Generates visualizations for Tesla stock data.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe

    def seasonal_plot(self):
        """
        Creates a seasonal plot of Tesla's closing prices.
        """
        assert "Month" in self.df.columns and "Year_Num" in self.df.columns, "Data must be preprocessed first"

        plt.figure(figsize=(12, 6))
        colors = plt.cm.rainbow(np.linspace(0, 1, self.df["Year_Num"].nunique()))

        for (year, color) in zip(self.df["Year_Num"].unique(), colors):
            subset = self.df[self.df["Year_Num"] == year]
            plt.plot(subset["Month"], subset["closing_price"], label=year, color=color)

        plt.xlabel("Month")
        plt.ylabel("Closing Price")
        plt.title("Seasonal Plot of Tesla Closing Prices")
        plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        plt.legend(title="Year", loc="upper left")
        plt.show()

    def lag_plot(self, lag=1, num_plots=10):
        """
        Generates lag plots to show linear dependencies between lagged closing prices.

        Parameters:
        lag (int): The lag value for the first plot. Default is 1.
        num_plots (int): The number of lag plots to generate (default is 10). The plots will be for lags from `lag` to `lag+num_plots-1`.
        """
        assert "closing_price" in self.df.columns, "DataFrame must contain 'closing_price' column"

        # Create subplots with 2 rows and 5 columns (for up to 10 lag plots)
        rows = 2
        cols = 5
        fig, axes = plt.subplots(rows, cols, figsize=(20, 7))

        # Flatten axes array for easier iteration
        axes = axes.flatten()

        # Loop through lag values and generate lag plots
        for i in range(num_plots):
            current_lag = lag + i
            ax = axes[i]
            pd_plot.lag_plot(self.df["closing_price"], lag=current_lag, ax=ax)
            ax.set_title(f"Lag {current_lag}")
            ax.grid(True)

        plt.tight_layout()
        plt.show()



    def autocorrelation(self, max_lag=10):
        """
        Calculate the Autocorrelation Function (ACF) of the closing prices for a range of lags.

        Parameters:
        max_lag (int): Maximum lag value for which to compute ACF

        Returns:
        dict: A dictionary with lag values as keys and their corresponding autocorrelation as values
        """
        assert "closing_price" in self.df.columns, "DataFrame must contain 'closing_price' column"

        # Convert closing_price to numpy array
        series = self.df["closing_price"].values
        acf_values = {}

        # Calculate ACF for each lag from 1 to max_lag
        for lag in range(1, max_lag + 1):
            # Shift the series by lag, align it with the original series, and calculate correlation
            shifted_series = series[lag:]
            original_series = series[:-lag]

            # Calculate the correlation
            correlation = np.corrcoef(original_series, shifted_series)[0, 1]
            acf_values[lag] = correlation

        return acf_values
