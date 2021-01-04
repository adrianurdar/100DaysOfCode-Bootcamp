# -*- coding: utf-8 -*-
"""2020 - College Salary Report (U.S.).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N74NswCpfaHISiRoLGZpSRbKKOT5D6fK
"""

import pandas as pd

"""Format output numbers"""

pd.options.display.float_format = '{:,.2f}'.format

"""Read file"""

df = pd.read_csv("highest_paying_jobs.csv")

"""Display the head and tail"""

df.head()

df.tail()

"""Clean the data frame"""

df.isna()

# Switch the header
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

df['Early Career Pay'] = pd.to_numeric(df['Early Career Pay'])

df['Mid-Career Pay'] = pd.to_numeric(df['Mid-Career Pay'])

"""# Find out what's the highest starting salary and it's major"""

print(f"The highest starting salary: ${df['Early Career Pay'].max()}")
print(f"The highest starting salary major: {df['Major'][df['Early Career Pay'].idxmax()]}")

"""# Find out what's the lowest starting salary and it's major"""

print(f"The lowest starting salary: ${df['Early Career Pay'].min()}")
print(f"The lowest starting salary major: {df['Major'][df['Early Career Pay'].idxmin()]}")

"""# Find out what's the highest spread and it's major"""

# Add Spread to the df
spread_col = df['Mid-Career Pay'] - df['Early Career Pay']
df.insert(1, 'Spread', spread_col)
df.head()

df.drop('Spread', inplace=True, axis=1)

df.sort_values('Spread', ascending=False)
df.head()

"""# Find out what's the lowest spread and it's major"""

df.tail()