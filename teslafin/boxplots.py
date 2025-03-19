# 5 plots in one page

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def boxplot_daywise(data, column, ax):
    """ Boxplot for days of the week. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    # Convert 'date' column to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(data['date']):
        data['date'] = pd.to_datetime(data['date'])

    data['day'] = data['date'].dt.dayofweek
    sns.boxplot(x='day', y=column, data=data, ax=ax)
    ax.set_title(f"Boxplot of {column} across Days of the Week")
    ax.set_xlabel("Day of Week")
    ax.set_ylabel(f"{column} Value")
    ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

def boxplot_weeks(data, column, ax):
    """ Boxplot for weeks. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    data['week'] = data['date'].dt.isocalendar().week
    sns.boxplot(x='week', y=column, data=data, ax=ax)
    ax.set_title(f"Boxplot of {column} across Weeks")
    ax.set_xlabel("Week")
    ax.set_ylabel(f"{column} Value")

def boxplot_monthwise(data, column, ax):
    """ Boxplot for months. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    data['month'] = data['date'].dt.month
    sns.boxplot(x='month', y=column, data=data, ax=ax)
    ax.set_title(f"Boxplot of {column} across Months")
    ax.set_xlabel("Month")
    ax.set_ylabel(f"{column} Value")

def boxplot_years(data, column, ax):
    """ Boxplot for years. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    data['year'] = data['date'].dt.year
    sns.boxplot(x='year', y=column, data=data, ax=ax)
    ax.set_title(f"Boxplot of {column} across Years")
    ax.set_xlabel("Year")
    ax.set_ylabel(f"{column} Value")

# Example usage
data = {'date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
        'value': range(100)}
df = pd.DataFrame(data)

# Create subplots (2 rows, 3 columns) for boxplots and lag plot
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Plot each boxplot in a different subplot
boxplot_years(df, 'value', axes[0, 0])  # Top-left
boxplot_weeks(df, 'value', axes[0, 1])  # Top-center
boxplot_monthwise(df, 'value', axes[0, 2])  # Top-right
boxplot_daywise(df, 'value', axes[1, 0])  # Bottom-left

# Plot the lag plot in the remaining subplot
lag_plot(df, 'value', axes[1, 1], lags=1)  # Bottom-center

# Hide the last subplot (optional)
axes[1, 2].axis('off')

# Adjust the layout
plt.tight_layout()
plt.show()

##############################################################
# 5 plots separated
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def lag_plot(data, column, lags=1):
    """
    Creates a lag plot to show the autocorrelation of a time series data.
    
    Parameters:
        data (pd.DataFrame): Data containing the time series.
        column (str): Column name to plot.
        lags (int): The number of lags to create.
        
    Returns:
        None
    """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    # Create the lagged version of the column
    lagged_data = data[column].shift(lags)
    
    # Drop rows with missing values (due to shifting)
    data_lagged = data.dropna(subset=[column])
    
    # Plot the lag plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=lagged_data.iloc[lags:], y=data_lagged[column].iloc[lags:])
    plt.title(f"Lag Plot of {column} with {lags} lag")
    plt.xlabel(f"{column} (Lagged)")
    plt.ylabel(f"{column} (Current)")
    plt.show()

def boxplot_daywise(data, column):
    """ Boxplot for days of the week. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    # Convert 'date' column to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(data['date']):
        data['date'] = pd.to_datetime(data['date'])

    data['day'] = data['date'].dt.dayofweek
    plt.figure(figsize=(12, 6))  # Create a new figure
    sns.boxplot(x='day', y=column, data=data)
    plt.title(f"Boxplot of {column} across Days of the Week")
    plt.xlabel("Day of Week")
    plt.ylabel(f"{column} Value")
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.show()

def boxplot_weeks(data, column):
    """ Boxplot for weeks. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    data['week'] = data['date'].dt.isocalendar().week
    plt.figure(figsize=(12, 6))  # Create a new figure
    sns.boxplot(x='week', y=column, data=data)
    plt.title(f"Boxplot of {column} across Weeks")
    plt.xlabel("Week")
    plt.ylabel(f"{column} Value")
    plt.show()

def boxplot_monthwise(data, column):
    """ Boxplot for months. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data.columns, f"Column '{column}' not found in data"
    
    data['month'] = data['date'].dt.month
    plt.figure(figsize=(12, 6))  # Create a new figure
    sns.boxplot(x='month', y=column, data=data)
    plt.title(f"Boxplot of {column} across Months")
    plt.xlabel("Month")
    plt.ylabel(f"{column} Value")
    plt.show()

def boxplot_years(data, column):
    """ Boxplot for years. """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame"
    assert column in data. columns, f"Column '{column}' not found in data"
    
    data['year'] = data['date'].dt.year
    plt.figure(figsize=(12, 6))  # Create a new figure
    sns.boxplot(x='year', y=column, data=data)
    plt.title(f"Boxplot of {column} across Years")
    plt.xlabel("Year")
    plt.ylabel(f"{column} Value")
    plt.show()
