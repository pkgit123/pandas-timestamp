# pandas-timestamp
Playbook for working with pandas timestamp

When working with date and datetime in pandas, the basic workflow of pd.to_datetime() creates timestamp object.

Similarly, to specify current datetime, the pd.Timestamp.now() creates timestamp object.  

The possible datatypes include:
* timestamp
* datetime
* date
* period, e.g. pd.Timestamp.to_period('M') -> YYYY-MM
* string, e.g. .strftime()
