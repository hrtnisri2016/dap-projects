import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2 > 25
df['overweight'] = df['overweight'].replace({True: 1, False: 0})

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'] > 1
df['cholesterol'] = df['cholesterol'].replace({True: 1, False: 0})

df['gluc'] = df['gluc'] > 1
df['gluc'] = df['gluc'].replace({True: 1, False: 0})

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 
                                 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. We have to rename 'value' column for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()
    df_cat = df_cat.to_frame().rename(columns={'value' : 'total'}).reset_index()

    # Draw the catplot with 'sns.catplot()'
    catplot = sns.catplot(kind='bar', 
                           data=df_cat, 
                           col='cardio', 
                           x='variable', 
                           y='total', 
                           hue='value')
    
    # # Get the figure for the output
    fig = catplot.figure
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    cond1 = df['ap_lo'] <= df['ap_hi']
    cond2 = df['height'] >= df['height'].quantile(0.025)
    cond3 = df['height'] <= df['height'].quantile(0.975)
    cond4 = df['weight'] >= df['weight'].quantile(0.025)
    cond5 = df['weight'] <= df['weight'].quantile(0.975)
    df_heat = df[cond1 & cond2 & cond3 & cond4 & cond5]

    # Calculate the correlation matrix
    corr = df_heat.corr().round(1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, fmt='.1f', linewidths=0.5, 
                square=True, cbar_kws = {'shrink':0.5}, annot=True, center=0)

    fig.savefig('heatmap.png')
    return fig
