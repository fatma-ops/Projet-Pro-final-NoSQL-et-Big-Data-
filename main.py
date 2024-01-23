import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.write("""
# My first app
Hello *world!*
""")

client = MongoClient("mongodb+srv://batman:jesuisbatman@bdd-cours-mongo.qbpym7c.mongodb.net/?retryWrites=true&w=majority")

data = pd.read_csv("flight_dataset.csv")