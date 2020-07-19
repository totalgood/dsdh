import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

pd.options.display.max_rows = 20
df = pd.read_csv('epa_hap_daily_summary.csv')
samples = df.sample(10000)
display(df.describe(include='all'))

pollutants = df['parameter_name'].value_counts()
display(pollutants)
df = pd.get_dummies(df, columns=['parameter_name'])
pollutant_columns = [
    c for c in df.columns if c.startswith('parameter_name_')]

for c in pollutant_columns:
    mask = df[c].astype(bool)
    pollutant = c[len('parameter_name_'):]
    df[c][mask] *= df['arithmetic_mean'][mask]

for i, c in enumerate(pollutant_columns):
    mask = df[c].astype(bool)
    strata = df[['latitude', 'longitude', c]][mask]
    g = strata.groupby(['latitude', 'longitude']).mean()
    g['latitude'], g['longitude'] = zip(*g.index.values)
    fig, ax = plt.subplots()

    g = pd.DataFrame(np.array([g['longitude'].values, g['latitude'].values, g[c].values])).T
    sns.scatterplot(x=g['longitude'], y=g['latitude'], ax=ax, c=i)

    pollutant = c[len('parameter_name_'):]
    plt.title(pollutant.title())
    plt.grid('on')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.show(block=False)
    break
