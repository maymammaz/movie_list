#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:16:28 2021

@author: mayroque
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:31:50 2021

@author: mayroque
"""

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Horror Movie List",
                   page_icon=":bar_chart:",
                   layout='wide')
df = pd.read_excel(

  io='list.xlsx',
  engine= 'openpyxl',
  sheet_name='Movies',
  usecols='A,C,D,F,G,J,L,M,N,O,P,Q',

).fillna('')



#years=df.sort_values(by=["YEAR"])
# defaultcols = ["name", "host_name", "neighbourhood", "room_type", "price"]


# SIDEBAR

st.sidebar.header("Please Filter Here")

subgenre = st.sidebar.multiselect(
    "Subgenre",
    options=df["Subgenre"].unique()
    )
               
#year = st.sidebar.multiselect(
#    "Year",
#    options=df["YEAR"].unique()
#    )


year = st.sidebar.slider(
    'Select Year Range',
    min_value = st.sidebar.number_input("Oldest", step=1),
    max_value = st.sidebar.number_input("Newest", step=1),
    step=1,
    #year= df.query["YEAR"]("min_value<=year<=max_value").sort_values("YEAR")    
    ) 


country = st.sidebar.radio(
    "Country",
    df["Country"].drop_duplicates(),
    index=0
    )


df_selection = df.query( 
        'Subgenre == @subgenre & YEAR <= @year & Country == @country'
        )


#oldest = st.sidebar.number_input("Oldest", min_value=0),
#newest = st.sidebar.number_input("Maximum", min_value=0, value=5)
#df.query("@oldest<=year<=@newest").sort_values("YEAR")

st.dataframe(df_selection)


# conda install spyder=5.1.5