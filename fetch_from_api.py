import pandas as pd
import requests
import os
posts=requests.get("https://jsonplaceholder.typicode.com/posts")
users=requests.get("https://jsonplaceholder.typicode.com/users")
posts_data_frame=pd.DataFrame(posts.json())
users_data_frame=pd.DataFrame(users.json())
merged=posts_data_frame.merge(users_data_frame,right_on="id",left_on="userId")#means it will merge where user_id==id
os.makedirs("fetched_dataset",exist_ok=True)
merged.to_csv("fetched_dataset/dataset.csv",index=False)
