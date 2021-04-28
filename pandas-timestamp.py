import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 999)

# create dataframe
df_sample = pd.DataFrame({
    'size': ['small', 'medium', 'large', 'small', 'medium'],
    'datetime': ['2017-08-14 03:29:25', '2017-08-16 00:15:27', '2020-09-06 11:09:33', '2021-09-06 11:16:55', '2022-09-05 12:04:26'],
    'color': ['red', 'red', 'green', 'blue', 'blue']
})

# faster way to convert str date into datetime
# https://www.reddit.com/r/learnpython/comments/6evlv5/faster_ways_to_convert_from_string_to_datetime/
date_cache = {k: pd.to_datetime(k) for k in df_sample['datetime'].unique()}
df_sample['date_col_fast'] = df_sample['datetime'].map(date_cache)

# add additional datetime columns
df_sample['date_col'] = pd.to_datetime(df_sample['datetime']).dt.date
df_sample['year_col'] = pd.to_datetime(df_sample['datetime']).dt.year
df_sample['month_col'] = pd.to_datetime(df_sample['datetime']).dt.month
df_sample['year_month_col'] = pd.to_datetime(df_sample['datetime']).dt.to_period('M')

print("Here is the dataframe sample.")
print(df_sample)
print()

# calculate today
pd_ts_now = pd.Timestamp.now()
df_sample['now_year'] = pd_ts_now.year
df_sample['now_date'] = pd_ts_now.date()

# faster way to calculate difference in dates
df_sample['age_years_fast'] = (df_sample['now_date'] - df_sample['date_col'])
df_sample['age_years_fast'] = [x.years for x in df_sample['age_years_fast'] ]

# calculate age in years
df_sample['age_years'] = (df_sample['now_date'] - df_sample['date_col']) / np.timedelta64(1, 'Y')

print(now_year)
print(now_date)
print()

# filter only dates up today
df_thru_today = df_sample.query(" date_col<=now_date ")

print("Here is the filter dates sample.")
print(df_thru_today)
print()
