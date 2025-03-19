import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot  # Corrected import

class AdvancedPlots:
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()

    def seasonal_plot(self):
        """
        Creates a seasonal plot of Tesla's closing prices.
        Each year's data is plotted separately for comparison.
        """
        assert "Month" in self.df.columns and "Year" in self.df.columns, "Data must be preprocessed first"
        
        # Ensure there is enough data to plot
        if self.df["Year"].nunique() < 1:
            raise ValueError("Not enough yearly data for a seasonal plot.")

        plt.figure(figsize=(12, 6))
        colors = plt.cm.rainbow(np.linspace(0, 1, self.df["Year"].nunique()))

        for (year, color) in zip(self.df["Year"].unique(), colors):
            subset = self.df[self.df["Year"] == year]
            plt.plot(subset["Month"], subset["closing_price"], label=int(year), color=color)

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
        num_plots (int): Number of lag plots to generate (default is 10).
                        The plots will be for lags from `lag` to `lag+num_plots-1`.
        """
        assert "closing_price" in self.df.columns, "DataFrame must contain 'closing_price' column"
        
        # Check if data is sufficient
        if len(self.df) < lag + num_plots:
            raise ValueError("Not enough data points for the requested lag plots.")

        rows, cols = 2, 5  # Arrange plots in a 2x5 grid
        fig, axes = plt.subplots(rows, cols, figsize=(20, 7))
        axes = axes.flatten()

        for i in range(num_plots):
            current_lag = lag + i
            ax = axes[i]
            lag_plot(self.df["closing_price"], lag=current_lag, ax=ax)
            ax.set_title(f"Lag {current_lag}")
            ax.grid(True)

        plt.tight_layout()
        plt.show()

