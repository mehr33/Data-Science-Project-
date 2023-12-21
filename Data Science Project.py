#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[3]:



df=pd.read_csv('priceoye (9).csv')


# In[4]:


df.dtypes


# In[5]:



df['productBox href'] = df['productBox href'].astype(str).replace("https://", "", regex=True)
df['i-amphtml-fill-content src 2'] = df['i-amphtml-fill-content src 2'].astype(str).replace("https://", "", regex=True)
df['price-diff-saving'] = df['price-diff-saving'].str.replace(r'\(|OFF\)', '', regex=True)

df['price-box'] = df['price-box'].str.replace('Rs. ', '', regex=True).str.replace(',', '', regex=True).str.strip()
# Convert the cleaned 'price-box' column values to integers
df['price-box'] = pd.to_numeric(df['price-box'], errors='coerce').astype('Int64')

df['price-diff-retail'] = df['price-diff-retail'].str.replace('Rs. ', '', regex=True).str.replace(',', '', regex=True).str.strip()
# Convert the cleaned 'price-box' column values to integers
df['price-diff-retail'] = pd.to_numeric(df['price-diff-retail'], errors='coerce').astype('Int64')


df.dtypes


# In[6]:


df=df.drop(['i-amphtml-layout-fill','i-amphtml-fill-content src'],axis=1)
df


# In[7]:


duplicate_rows_df=df[df.duplicated()]
print('Duplicated Rows =:    ',duplicate_rows_df)


# In[8]:


df=df.rename(columns={'productBox href':'Urls','i-amphtml-fill-content src 2':'Images','p-title':'Pro_Name','price-box':'Price','price-diff-retail':'Retail','price-diff-saving':'Discount'})
df


# In[9]:


print(df.isnull().sum())
print(df.dropna())
print(df)
print(df.isnull().sum())


# In[10]:


for column in df:
    print(column,' :: ', df[column].isnull().sum())
df['Brand'].fillna(df['Brand'].mean,inplace=True)


# In[11]:


for column in df:
    print(column,' :: ', df[column].isnull().sum())


# In[12]:


df=df.drop(['Discount'],axis=1)
df


# In[14]:


#sns.boxplot(x=df['Price'])


# In[38]:


#sns.boxplot(x=df['Discount'])


# In[15]:


df['Brand'].value_counts().nlargest(50).plot(kind='bar', figsize=(10, 5))
plt.title("Number of Brand")
plt.ylabel('Y Label')
plt.xlabel('X Label')
plt.show()


# In[16]:


plt.figure(figsize=(10,5))
c=df.corr()
sns.heatmap(c,cmap='BrBG',annot=True)
c


# In[ ]:


fig, ax=plt.subplots(figsize=(10,6))
ax.scatter(df['Urls'],df['Price'])
ax.set_xlabel('Urls')
ax.set_ylabel('Price')
plt.show()


# In[ ]:





# In[ ]:




