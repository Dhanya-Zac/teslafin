import pandas as pd

class PreProcess:
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.df = dataframe.copy()
    
    def preprocess(self):
        # Ensure 'Year' column exists before processing
        if "Year" in self.df.columns:
            # Convert 'Year' to datetime format
            self.df["Year"] = pd.to_datetime(self.df["Year"], errors='coerce')
            # Remove invalid dates
            self.df.dropna(subset=["Year"], inplace=True)
            # Extract month
            self.df["Month"] = self.df["Year"].dt.month
            # Extract year
            self.df["Year"] = self.df["Year"].dt.year
        else:
            print("Warning: 'Year' column not found in dataframe.")
        return self.df.copy()

    def missing_values(self):
        # Handle missing values using forward fill
        self.df.fillna(method='ffill', inplace=True)
        return self.df.copy()

    def remove_duplicates(self):
        # Remove duplicate rows
        self.df.drop_duplicates(inplace=True)
        return self.df.copy()
