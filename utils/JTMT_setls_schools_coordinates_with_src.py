#!/usr/bin/env python
# coding: utf-8

# ### ספריות
# 

# In[1]:


import pandas as pd
import os
import sys

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


# ### העלת משתנים להרצת הקוד
# 

# In[2]:


# מיקום תיקייה נוכחית
cwd = os.getcwd()

education_folder_path = os.path.dirname(cwd)


# In[3]:


# תאריך
file_date=pd.Timestamp.today().strftime('%y%m%d')


# ### פונקציות גלובליות
# 

# In[4]:


# הוספת נתיב modules כנתיב יחסי
sys.path.append('../modules')

from global_functions import remove_spaces_in_columns, up_load_df


# ### העלאת טבלאות
# 

# In[5]:


# בתי ספר מעיריית בית שמש
BShemesh_manual=up_load_df(r'{}\background_files\JTMT_setls_schools_coordinates_with_src'.format(education_folder_path),'250121_BShemesh_manual')
BShemesh_manual=remove_spaces_in_columns(BShemesh_manual)

BShemesh_moe_coordinates=up_load_df(r'{}\background_files\JTMT_setls_schools_coordinates_with_src'.format(education_folder_path),'250121_BShemesh_moe_coordinates')
BShemesh_moe_coordinates=remove_spaces_in_columns(BShemesh_moe_coordinates)

# בתי ספר מממשרד החינוך
Gschool_manual=up_load_df(r'{}\background_files\JTMT_setls_schools_coordinates_with_src'.format(education_folder_path),'250121_Gschool_manual')
Gschool_manual=remove_spaces_in_columns(Gschool_manual)

Gschool_moe_mosdot_coordinates=up_load_df(r'{}\background_files\JTMT_setls_schools_coordinates_with_src'.format(education_folder_path),'250121_Gschool_moe_mosdot_coordinates')
Gschool_moe_mosdot_coordinates=remove_spaces_in_columns(Gschool_moe_mosdot_coordinates)

# בתי ספר מעיריית ירושלים
JLM_moe_coordinates=up_load_df(r'{}\background_files\JTMT_setls_schools_coordinates_with_src'.format(education_folder_path),'250121_JLM_moe_coordinates')
JLM_moe_coordinates=remove_spaces_in_columns(JLM_moe_coordinates)

JLM_muni_coordinates=up_load_df(r'{}\background_files\JTMT_setls_schools_coordinates_with_src'.format(education_folder_path),'250121_JLM_muni_coordinates')
JLM_muni_coordinates=remove_spaces_in_columns(JLM_muni_coordinates)


# ### עיבוד
# 

# In[6]:


# חיבור כל הטבלאות
JTMT_setls_schools_coordinates_with_src = pd.concat([BShemesh_manual, BShemesh_moe_coordinates, Gschool_manual, 
                         Gschool_moe_mosdot_coordinates, JLM_moe_coordinates, JLM_muni_coordinates], 
                         ignore_index=True)


# In[8]:


JTMT_setls_schools_coordinates_with_src.to_excel(r'{}\background_files\{}_JTMT_setls_schools_coordinates_with_src.xlsx'.format(education_folder_path, file_date), index=False)

