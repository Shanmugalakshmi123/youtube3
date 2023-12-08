import streamlit as st
from googleapiclient.discovery import build
import subprocess
#import running
import os
from pprint import pprint
import sys
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from pandas.io import sql
import pymysql
import cryptography
#import MySQLdb

#con = MySQLdb.connect() 
#my_conn = create_engine("mysql://usrid:password@localhost/my_db")
#myconn=create_engine("mysql+pymysql://root:@127.0.0.1/test", pool_recycle=3600)

#dbConnection    = myconn.connect()
#my_data = pd.read_sql("SELECT * FROM student WHERE class='four'",dbConnection)
#print(my_data)

import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Hit on a Channel",
    ("Rijk Band","Corey Schafer","1littlecoder","Tamil Mom Portfolio","Fanilo Andrianasolo","Data Science Tamil","Streamlit","Idea Freeze","Website Learners","Poli Couple💃🕺")
)
add_selectbox1 = st.sidebar.selectbox(
    "Wanna know the statistics",
    ("Report","Graph"
    )
)
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Shanthini12345*",
database="youtube_api1"
)
mycursor=mydb.cursor()
#mycursor.execute("create table channel3(name1 varchar(50),id varchar(50),subs int, views int, desc1 varchar(5000), playlist_id varchar(50) )")
#data1=(Channel_id,Channel_Name,Channel_type,Channel_views,Channel_Description,Channel_status)
#result=str(pd.DataFrame(mycursor.execute("select channel_name from channel1 where channel_name='Rijk Band'")))
#raw_code = st.text_area("channel name")
#st.write(result)
#@my_data = pd.read_sql("select channel_name from channel1 where channel_name='Rijk Band'", mydb)
#st.write(my_data)
usrid="root"
password="Shanthini12345*"
my_db="youtube_api1"
my_conn = create_engine("mysql+pymysql://root:Shanthini12345*@localhost/youtube_api1")
my_data = pd.read_sql("select channel_name,channel_views from channel1 where channel_name='"+add_selectbox+"'",my_conn)
video=pd.read_sql("select video_name,comment_count,like_count,duration from video where video.playlist_id=(select playlist_id from playlist where channel_id=(select channel_id from channel1 where channel_name='"+add_selectbox+"'))",my_conn)

st.write("Channel Name",my_data)
st.write("Video Name",video)