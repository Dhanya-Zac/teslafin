# Class Preprocess removes duplicate values, handles missing values, date formatting
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()

    def preprocess(self):
        #change date to datetime format to ensure only valid dates are present
        self.df["Year"] = pd.to_datetime(self.df["Year"], errors='coerce')
        # Remove invalid dates
        self.df.dropna(subset=["Year"], inplace=True)
        #Extract month
        self.df["Month"] = self.df["Year"].dt.month
        #Extract year
        self.df["Year"] = self.df["Year"].dt.year
        return self.df

    def missing_values(self):
        # Function missing_values handles all missing values and fills them
        # using the previous value
        self.df.fillna(method='ffill', inplace=True)
        return self.df

    def remove_duplicates(self):
        #Function remove_duplicates removes all duplicate rows in the dataset
        self.df.drop_duplicates(inplace=True)
        return self.df
