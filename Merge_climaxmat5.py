#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df1=pd.read_excel("Clima_mensual.xlsx")
df2=pd.read_excel("mat5.xlsx")
import pandas as pd

dft = pd.merge(df1, df2, on=['mes_anio'], how='inner')


# In[8]:


dft


# In[ ]:





# In[ ]:




