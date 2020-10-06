import pandas as pd

# create dataframe
df_sample = pd.DataFrame({
    'size': ['small', 'medium', 'large', 'small', 'medium'],
    'datetime': ['2017-08-14 03:29:25', '2017-08-16 00:15:27', '2020-09-06 11:09:33', '2021-09-06 11:16:55', '2022-09-05 12:04:26'],
    'color': ['red', 'red', 'green', 'blue', 'blue']
})

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
now_year = pd_ts_now.year
now_date = pd_ts_now.date()

print(now_year)
print(now_date)
print()

# filter only dates up today
df_thru_today = df_sample.query(" date_col<=@now_date ")

print("Here is the filter dates sample.")
print(df_thru_today)
print()
