import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Boxplots:
    """
    Generates boxplots for analyzing Tesla stock data over different time intervals.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()

        # Ensure 'date' column exists and is in datetime format
        assert 'Year' in self.df.columns, "DataFrame must contain a 'date' column"
        self.df['Year'] = pd.to_datetime(self.df['Year'])

    def boxplot_daywise(self):
        """ Boxplot for days of the week. """
        self.df["Day"] = self.df["Year"].dt.dayofweek
        plt.figure(figsize=(10, 6))
        sns.boxplot(x="Day", y="closing_price", data=self.df)
        plt.xticks(ticks=range(7), labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        plt.xlabel("Day of the Week")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Days of the Week")
        plt.show()

    def boxplot_weeks(self):
        """ Boxplot for weeks of the year. """
        self.df["Week"] = self.df["Year"].dt.isocalendar().week
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="Week", y="closing_price", data=self.df)
        plt.xlabel("Week of the Year")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Weeks")
        plt.xticks(rotation=90)
        plt.show()

    def boxplot_monthwise(self):
        """ Boxplot for months of the year. """
        self.df["Month"] = self.df["Year"].dt.month
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="Month", y="closing_price", data=self.df)
        plt.xlabel("Month")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Months")
        plt.xticks(ticks=range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        plt.show()

    def boxplot_years(self):
        """ Boxplot for years. """
        self.df["Year_Num"] = self.df["Year"].dt.year  # Using "Year_Num" for consistency
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="Year_Num", y="closing_price", data=self.df)
        plt.xlabel("Year")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Years")
        plt.xticks(rotation=45)
        plt.show()
