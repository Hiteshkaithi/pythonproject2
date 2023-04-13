import pandas as pd
sales = pd.read_csv("/Users/hiteshreddy/Documents/hitesh.csv")
#print(sales)
date=pd.DatetimeIndex(sales['Date'])
#print(date)
sales['month']=date.month
#print(sales)
df=sales.groupby(['month','Name']).sum('User').sort_values(['month','User'],ascending=False)
# print(df)
top_five=df.groupby('month').head(5)
print(top_five)
