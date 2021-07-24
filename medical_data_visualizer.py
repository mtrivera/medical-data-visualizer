import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Create a 'bmi' column
df['bmi'] = round((df['weight'] / ((df['height'] * 0.01) ** 2)), 1)

# Add 'overweight' column
df['overweight'] = 0
df['overweight'] = np.where((df.bmi > 25), 1, df.overweight)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[(df.cholesterol == 1), 'cholesterol'] = 0
df.loc[(df.cholesterol > 1), 'cholesterol'] = 1

df.loc[(df.gluc == 1), 'gluc'] = 0
df.loc[(df.gluc > 1), 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio','variable','value'])['value'].count())
    df_cat.rename(columns={'value':'total'}, inplace=True)
    df_cat.reset_index(inplace=True)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(
        col="cardio",
        x="variable",
        y="total",
        hue="value",
        data=df_cat,
        kind="bar"
    )
 
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
