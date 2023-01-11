import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

plt.style.use('fivethirtyeight')

pd.set_option('display.max_columns', 89)

# Global Variables
StartDate = '2022-01-01'
EndDate = '2023-01-01'

# Initial DataFrame of Imported Clean Data
df = pd.read_csv('Data/CustomerQuotedProduct_clean.csv', encoding='Latin-1')
df.head()

# Filtered DataFrame of Cleaned Data
df2 = df.loc[(df['fldDate'] >= StartDate) & (df['fldDate'] < EndDate)]
df2.head()

# (Line count) of Furniture Catagories Quoted
plt.figure(figsize=(15, 5))
sns.countplot(x='fldGroupTypeID', data=df2)
plt.title(f'{StartDate} - {EndDate} furniture Catagories Count')
plt.xlabel('Furniture Catagories Quoted')

# (Line Count) of Parts by Type that was Quoted.
plt.figure(figsize=(10, 30))
sns.histplot(y='fldOpsWorksheetID', data=df2)
plt.title(f'{StartDate} - {EndDate} Groups Count')
plt.ylabel('Furniture System Catagories')
plt.xlabel('count of entries')

# (Line Count) of Manufacturer Entries.
plt.figure(figsize=(10, 15))
sns.histplot(y='fldManufacturer_ID', data=df2)
plt.title(f'{StartDate} - {EndDate} Manufacturers Quoted')
plt.ylabel('Manufacturers')
plt.xlabel('count of Quoted lines')
