import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot  

class AdvancedPlots:
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()
        
        # Ensure log transformation is available
        if "log_closing_price" not in self.df.columns:
            assert "closing_price" in self.df.columns, "DataFrame must contain 'closing_price' column"
            self.df["log_closing_price"] = np.log(self.df["closing_price"])

    def seasonal_plot(self, use_log=True):
        """
        Creates a seasonal plot of Tesla's closing prices (log-transformed if use_log=True).
        """
        assert "Month" in self.df.columns and "Year" in self.df.columns, "Data must be preprocessed first"
        
        column = "log_closing_price" if use_log else "closing_price"
        
        plt.figure(figsize=(12, 6))
        colors = plt.cm.rainbow(np.linspace(0, 1, self.df["Year"].nunique()))

        for (year, color) in zip(self.df["Year"].unique(), colors):
            subset = self.df[self.df["Year"] == year]
            plt.plot(subset["Month"], subset[column], label=int(year), color=color)

        plt.xlabel("Month")
        plt.ylabel("Log Closing Price" if use_log else "Closing Price")
        plt.title(f"Seasonal Plot of Tesla {'Log' if use_log else ''} Closing Prices")
        plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        plt.legend(title="Year", loc="upper left")
        plt.show()

    def lag_plot(self, lag=1, num_plots=10):
        """
        Generates lag plots using log-transformed closing prices.
        """
        assert "log_closing_price" in self.df.columns, "DataFrame must contain 'log_closing_price' column"
        
        rows, cols = 2, 5  
        fig, axes = plt.subplots(rows, cols, figsize=(20, 7))
        axes = axes.flatten()

        for i in range(num_plots):
            current_lag = lag + i
            ax = axes[i]
            lag_plot(self.df["log_closing_price"], lag=current_lag, ax=ax)
            ax.set_title(f"Lag {current_lag} (Log Transformed)")
            ax.grid(True)

        plt.tight_layout()
        plt.show()
