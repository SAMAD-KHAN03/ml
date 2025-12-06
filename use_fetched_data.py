import pandas as pd
import matplotlib.pyplot as plt
import ast
userdf=pd.read_csv("fetched_dataset/dataset.csv")
userdf['city']=userdf["address"].apply(lambda x:ast.literal_eval(x)['city'])
city_count=userdf['city'].value_counts().head(10)
plt.figure(figsize=[10,6])
plt.pie(city_count,labels=city_count.index,autopct='%1.1f%%',startangle=0)
plt.show()
