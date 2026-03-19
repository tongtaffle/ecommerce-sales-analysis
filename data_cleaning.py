# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a data cleaning script file.
"""

import pandas as pd

df = pd.read_csv("train.csv")

### Check information###
print('+++ Information +++')
df.info()
df.describe()

#Example data
print('+++ Example data +++')
print(df.head())

## Missing values
print('+++ Missing value +++')
print(df.isnull().sum()) #Postal code have 11 null
#Removed Postal code
df = df.drop(columns=['Postal Code'])

## Duplicate
print('+++ Duplicate +++')
print('Duplicate :',df.duplicated().sum(),'times')

##Convert date to date time
print('+++ Date time +++')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
print('alreay converted date time format successfully')

## Delete unuse columns
print("+++ Delete some columns +++")
df = df.drop(columns=['Row ID'])
print(df['Country'].nunique(),'| If 1 means that every rows are united state') # Every rows are United state
df = df.drop(columns=['Country'])

## Create new columns
print("+++ Create new columns")
# rename
df = df.rename(columns={'Sales': 'Total Sales'})

# date features
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month

# shipping
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# helper
df['Order Count'] = 1

##Outliers
print('+++ Outliers +++')
print(df.describe())
Q1 = df['Total Sales'].quantile(0.25)
Q3 = df['Total Sales'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Total Sales'] < lower) | (df['Total Sales'] > upper)]

print(len(outliers))
print(df['Shipping Days'].describe())
print('Nothing weird')

## clean text
print('+++ Clean text +++')
columns_to_strip = ['Ship Mode', 'City', 'State', 'Region', 'Segment', 'Category', 'Sub-Category']
for col in columns_to_strip:
    df[col] = df[col].str.strip()

# standardize text
df['Segment'] = df['Segment'].str.lower()
df['Category'] = df['Category'].str.lower()
df['Sub-Category'] = df['Sub-Category'].str.lower()
print('ALready cleaned text successfully')

##Data type
print("+++ Data type +++")
print(df.dtypes)

### Export New file for SQL ###
df.to_csv("cleaned_data.csv", index=False, encoding='utf-8-sig')
print ("File upload!")