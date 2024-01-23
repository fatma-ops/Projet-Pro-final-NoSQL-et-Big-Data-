import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.write("""
# My first app
Hello *world!*
""")

client = MongoClient()

find = client['IPSSI']['crimeUS'].find()

df = pd.DataFrame(find)

st.write(df)