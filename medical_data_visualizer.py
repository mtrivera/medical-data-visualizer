import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Create a 'bmi' column
df['bmi'] = (df['weight'] / ((df['height'] * 0.01) ** 2))

# Add 'overweight' column
df['overweight'] = np.where((df.bmi > 25), 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df.cholesterol > 1, 1, 0)
df['gluc'] = np.where(df.gluc > 1, 1, 0)

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
    return fig.fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Drop bmi column, not needed for heatmap
    df_heat = df_heat.drop('bmi', axis=1)

    # Calculate the correlation matrix
    corr = df_heat.corr()
   
    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr,
        mask=mask,
        vmin=-0.1,
        vmax=0.3,
        annot=True,
        fmt='0.1f',
        center=0,
        linewidths=0.1,
        linecolor='white',
        cbar_kws={
            "shrink": 0.55,
            "ticks":[0.24, 0.16, 0.08, 0.00, -0.08]
        }
    )
   
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
