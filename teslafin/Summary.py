class Summary:
    """
    Computes basic statistics on Tesla stock data.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe

    def get_summary(self):
        """
        Returns mean, median, and standard deviation of the closing price.
        """
        assert "closing_price" in self.df.columns, "DataFrame must contain 'closing_price' column"
        return {
            "Mean": self.df["closing_price"].mean(),
            "Median": self.df["closing_price"].median(),
            "Std Dev": self.df["closing_price"].std(),
            "Min": self.df["closing_price"].min(),
            "Max": self.df["closing_price"].max(),
            "Quantiles": self.df["closing_price"].quantile([0.25, 0.5, 0.75]).to_dict()
        }
