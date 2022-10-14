import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.lineplot(data=df['value'], color='crimson')

    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019") 

    # Save image and return fig 
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Make year and month columns
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Map the month integers to their proper names
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    df_bar["month"] = df_bar["month"].apply(lambda data: months[data-1])
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=months)

    # Group by year column
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.to_frame().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(7, 7))
    sns.barplot(data=df_bar, x='year', y='value', hue='month', palette='tab10')

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend(loc='upper left', title='Months')
    plt.xticks(rotation='vertical')

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

    # The first boxplot
    sns.boxplot(ax=ax1, data=df_box, x="year", y="value")
    ax1.set_yticks(np.arange(0, 220000, 20000))
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)") 

    # The second boxplot
    sns.boxplot(ax=ax2, data=df_box, x='month', y='value', 
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_yticks(np.arange(0, 220000, 20000))
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
