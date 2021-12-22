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


st.sidebar.header("Please Filter Here")

subgenre = st.sidebar.multiselect(
    "Subgenre",
    options=df["Subgenre"].unique()
    )

year = st.sidebar.slider(
    'Select Year Range',
    min_value = 1920, max_value = 2020, 
    value = 2018
    ) 

country = st.sidebar.radio(
    "Country",
    df["Country"].drop_duplicates(),
    index=0
    )


df_selection = df.query( 
        'Subgenre == @subgenre & YEAR <= @year & Country == @country'
        )

st.dataframe(df_selection)

