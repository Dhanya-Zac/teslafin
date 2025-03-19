import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class BoxPlots:
    def __init__(self, data):
        assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
        self.df = data

    def boxplot_daywise(self, column, ax):
        """ Boxplot for days of the week. """
        assert column in self.df.columns, f"Column '{column}' not found in data"
        
        self.df['day'] = self.df['date'].dt.dayofweek
        sns.boxplot(x='day', y=column, data=self.df, ax=ax)
        ax.set_title(f"Boxplot of {column} across Days of the Week")
        ax.set_xlabel("Day of Week")
        ax.set_ylabel(f"{column} Value")
        ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    def boxplot_weeks(self, column, ax):
        """ Boxplot for weeks. """
        assert column in self.df.columns, f"Column '{column}' not found in data"
        
        self.df['week'] = self.df['date'].dt.isocalendar().week
        sns.boxplot(x='week', y=column, data=self.df, ax=ax)
        ax.set_title(f"Boxplot of {column} across Weeks")
        ax.set_xlabel("Week")
        ax.set_ylabel(f"{column} Value")

    def boxplot_monthwise(self, column, ax):
        """ Boxplot for months. """
        assert column in self.df.columns, f"Column '{column}' not found in data"
        
        self.df['month'] = self.df['date'].dt.month
        sns.boxplot(x='month', y=column, data=self.df, ax=ax)
        ax.set_title(f"Boxplot of {column} across Months")
        ax.set_xlabel("Month")
        ax.set_ylabel(f"{column} Value")

    def boxplot_years(self, column, ax):
        """ Boxplot for years. """
        assert column in self.df.columns, f"Column '{column}' not found in data"
        
        self.df['year'] = self.df['date'].dt.year
        sns.boxplot(x='year', y=column, data=self.df, ax=ax)
        ax.set_title(f"Boxplot of {column} across Years")
        ax.set_xlabel("Year")
        ax.set_ylabel(f"{column} Value")


# Example usage
data = {'date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
        'value': range(100)}
df = pd.DataFrame(data)

# Create subplots (2 rows, 3 columns) for boxplots
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Instantiate the BoxPlots class
box_plots = BoxPlots(df)

# Plot each boxplot in a different subplot
box_plots.boxplot_years('value', axes[0, 0])  # Top-left
box_plots.boxplot_weeks('value', axes[0, 1])  # Top-center
box_plots.boxplot_monthwise('value', axes[0, 2])  # Top-right
box_plots.boxplot_daywise('value', axes[1, 0])  # Bottom-left

# Hide the last subplot (optional, if you don't need it)
axes[1, 2].axis('off')

# Adjust the layout
plt.tight_layout()
plt.show()
