import streamlit as st
from googleapiclient.discovery import build
import subprocess
#import running
import os
from pprint import pprint
import sys
from streamlit.connections import SQLConnection
import pymongo
import pandas as pd
#import google_auth_oauthlib.flow
name=st.text_input('Enter a youtube channel')
#schafers=st.form_submit_button('schafers')
#def schafers_click():
    #with open("running.py") as f:
     #   exec(f.read())
    #exec(open("running.py").read())
    #os.system('python running.py')
    #subprocess.run(["python","running.py"])
    #name=st.text_input("hi")
#if st.button("schafers"):
    #st.write(schafers_click())


import pandas
import numpy
import mysql.connector
api_key="AIzaSyBMQWD174cIpmzRt9bPYfms9n_5zSzaD_0"
api_service="youtube"
api_version="v3"
youtube=build(api_service,api_version,developerKey=api_key)
request = youtube.channels().list(
        part="statistics,snippet,contentDetails,status",
        #id="UCpWT_QfKk7BJIpn709YgsYA"
        #id="UCtOtzF5LuR0UIcKsKSG9_aw"
        #id="UCXAz74jWHL8E-k7f3A73GzQ"
        #id="UC3LD42rjj-Owtxsa6PwGU5Q"
        #id="UCuI5XcJYynHa5k_lqDzAgwQ"
        #id="UCj0aKGrBN6x2_PY0c6RrGNw"
        #id="UCenpjMao0ukGDychNQ77gVg"
        #id="UCpV_X0VrL8-jg3t6wYGS-1g"
        #id="UCCezIgC97PvUuR4_gbFUs5g"
        #id="UCGboL10j61nVtyxHIRTiIeQ"
        id="UCjBukMyq--98YtJu1Z5O0xQ"
        )
response=request.execute()

#for i in response['items']:
 #   data=dict(Channel_Name=i["snippet"]["title"],
  # #           Channel_id=i["id"],
   #           Subs_count=i['statistics']['subscriberCount'],
      #        Channel_views=i['statistics']['viewCount'],
     #         Channel_Description=i['snippet']['description'],
       #       Playlist_id=i['contentDetails']['relatedPlaylists']['uploads'])
       #
Channel_Name="hi"
Channel_id="u"
Subs_count=0
Channel_views=0
Channel_Description="us"
Playlist_id="u"
for i in response['items']: 
    Channel_Name=i["snippet"]["title"]
   # print(Channel_Name)
    Channel_id=i["id"]
    #print(Channel_id)
    Subs_count=i['statistics']['subscriberCount']
    #print(Subs_count)
    Channel_views=i['statistics']['viewCount']
    #print(Channel_views)
    Channel_Description=i['snippet']['description']
    #print(Channel_Description)
    Playlist_id=i['contentDetails']['relatedPlaylists']['uploads']
    #print(Playlist_id)
    Channel_type=""
    Channel_status=i['status']['privacyStatus']



request2=youtube.videos().list(
    part="statistics,snippet,contentDetails",
    id="8QURqbTFmc0"
)

response2=request2.execute()
for i in response2['items']:
    Video_Id=i["id"]
    Video_Name=i["snippet"]["title"]
    Video_Description=i["snippet"]["description"]
    Tags=i["etag"]
    PublishedAt=i["snippet"]["publishedAt"]
    View_Count=i["statistics"]["viewCount"]
    Like_Count=i["statistics"]["likeCount"]
    Dislike_Count=0
   # Dislike_Count=i["statistics"]["dislikeCount"]
    Favorite_Count=i["statistics"]["favoriteCount"]
    Comment_Count=i["statistics"]["commentCount"]
    Duration=i["contentDetails"]["duration"]
    #Thumbnail=i["processingDetails"]["thumbnailsAvailability"]
    Thumbnail=""
    Caption_Status=i["contentDetails"]["caption"]

request3=youtube.commentThreads().list(
    part="snippet,replies",
    videoId="8QURqbTFmc0"
)
response3=request3.execute()
for i in response3['items']:
    Comment_Id=i["id"]
    Comment_Text=i["snippet"]["topLevelComment"]
request9=youtube.comments().list(
    part="snippet",
    id=Comment_Id
)
response9=request9.execute()
for i in response9['items']:
    Comment_Author=i["snippet"]["authorDisplayName"]
    Comment_PublishedAt=i["snippet"]["publishedAt"]
#pprint(response)
request7=youtube.commentThreads().list(
    part="snippet,replies",
    videoId="8QURqbTFmc0"
)
response7=request7.execute()
for i in response7['items']:
    Comment_Id1=i["id"]
request10=youtube.comments().list(
    part="snippet",
    id=Comment_Id1
)
response10=request10.execute()
for i in response10['items']:
    Comment_Text1=i["snippet"]["textOriginal"]
    Comment_Author1=i["snippet"]["authorDisplayName"]
    Comment_PublishedAt1=i["snippet"]["publishedAt"]

request4=youtube.videos().list(
    part="statistics,snippet,contentDetails",
    id="DYCgIJ4E4cg"
)

response4=request4.execute()
for i in response4['items']:
    Video_Id2=i["id"]
    Video_Name2=i["snippet"]["title"]
    Video_Description2=i["snippet"]["description"]
    Tags2=i["etag"]
    PublishedAt2=i["snippet"]["publishedAt"]
    View_Count2=i["statistics"]["viewCount"]
    Like_Count2=i["statistics"]["likeCount"]
    #Dislike_Count2=i["statistics"]["dislikeCount"]
    Dislike_Count2=0
    Favorite_Count2=i["statistics"]["favoriteCount"]
    Comment_Count2=i["statistics"]["commentCount"]
    Duration2=i["contentDetails"]["duration"]
    #Thumbnail2=i["processingDetails"]["thumbnailsAvailability"]
    Thumbnail2=""
    Caption_Status2=i["contentDetails"]["caption"]

request5=youtube.commentThreads().list(
    part="snippet,replies",
    videoId="DYCgIJ4E4cg"
)
Comment_Id3=""
response5=request5.execute()
for i in response5['items']:
    Comment_Id3=i["id"]
request11=youtube.comments().list(
    part="snippet",
    id=Comment_Id3
)
response11=request11.execute()
for i in response11['items']:
    Comment_Text3=i["snippet"]["textOriginal"]
    Comment_Author3=i["snippet"]["authorDisplayName"]
    Comment_PublishedAt3=i["snippet"]["publishedAt"]
request6=youtube.commentThreads().list(
    part="snippet",
    videoId="DYCgIJ4E4cg"
)
Comment_Id4=""
response6=request6.execute()
for i in response6['items']:
    Comment_Id4=i["id"]
request12=youtube.comments().list(
    part="snippet",
    id=Comment_Id4
)
Playlist_name=""
response12=request12.execute()
for i in response12['items']:
    Comment_Text4=i["snippet"]["textOriginal"]
    Comment_Author4=i["snippet"]["authorDisplayName"]
    Comment_PublishedAt4=i["snippet"]["publishedAt"]
request8=youtube.playlists().list(
    part="snippet,contentDetails",
    channelId="UCjBukMyq--98YtJu1Z5O0xQ",
    maxResults=25

)
response8=request8.execute()
for i in response8['items']:
    Playlist_id=i["id"]
    Playlist_name=i["snippet"]["title"]
    Channel_id=i["snippet"]["channelId"]

#pprint(response)
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["Youtube_db"]
coll=db['Channel']
data2={
    "Channel_Name":{
        "Channel_Name":Channel_Name,
        "Channel_Id":Channel_id,
        "Subscription":Subs_count,
        "Channel_Views":Channel_views,
        "Channel_Description":Channel_Description,
        "Playlist_Id":Playlist_id
    },
    "Video_Id1":{
        "Video_Id":Video_Id,
        "Video_Name":Video_Name,
        "Video_Description":Video_Description,
        "Tags":Tags,
        "PublishedAt":PublishedAt,
        "ViewCount":View_Count,
        "LikeCount":Like_Count,
        "DislikeCount":Dislike_Count,
        "FavoriteCount":Favorite_Count,
        "CommentCount":Comment_Count,
        "Duration":Duration,
        "Thumbnail":Thumbnail,
        "CaptionStatus":Caption_Status,
        "Comments":{
            "CommentId1":{
                "CommentId":Comment_Id,
                "CommentText":Comment_Text,
                "CommentAuthor":Comment_Author,
                "Comment_PublishedAt":Comment_PublishedAt
            },
            "CommentId2":{
                "CommentId":Comment_Id1,
                "CommentText":Comment_Text1,
                "CommentAuthor":Comment_Author1,
                "Comment_PublishedAt":Comment_PublishedAt1
            }

        }

    },
    "Video_Id2":{
        "Video_Id":Video_Id2,
        "Video_Name":Video_Name2,
        "Video_Description":Video_Description2,
        "Tags":Tags2,
        "PublishedAt":PublishedAt2,
        "ViewCount":View_Count2,
        "LikeCount":Like_Count2,
        "DislikeCount":Dislike_Count2,
        "FavoriteCount":Favorite_Count2,
        "CommentCount":Comment_Count2,
        "Duration":Duration2,
        "Thumbnail":Thumbnail2,
        "CaptionStatus":Caption_Status2,
        "Comments":{
            "CommentId1":{
                "CommentId":Comment_Id3,
                "CommentText":Comment_Text3,
                "CommentAuthor":Comment_Author3,
                "Comment_PublishedAt":Comment_PublishedAt3
            },
            "CommentId2":{
                "CommentId":Comment_Id4,
                "CommentText":Comment_Text4,
                "CommentAuthor":Comment_Author4,
                "Comment_PublishedAt":Comment_PublishedAt4
            }

        }

    }
}
coll.insert_one(data2)
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Shanthini12345*",
database="youtube_api1"
)
mycursor=mydb.cursor()
#mycursor.execute("create table channel3(name1 varchar(50),id varchar(50),subs int, views int, desc1 varchar(5000), playlist_id varchar(50) )")
data1=(Channel_id,Channel_Name,Channel_type,Channel_views,Channel_Description,Channel_status)
mycursor.execute("insert into channel1 values (%s,%s,%s,%s,%s,%s)",data1)
data2=(Playlist_id,Channel_id,Playlist_name)
mycursor.execute("insert into playlist values (%s,%s,%s)",data2)
date1=pd.Timestamp(PublishedAt)
t=Duration.replace("PT","")
#print(t)
x=[]
for i in t:
    if i=="M":
        t=t.replace("M","")
        break
    else:
        x.append(i)
        print("x=",x)
        t=t.replace(i,"")
        print(t)
t=t.replace("S","")
print("t=",t)
x1="".join(x)
print("x1=",x1)
time1=int(x1)*60+int(t)

data3=(Video_Id,Playlist_id,Video_Name,Video_Description,date1,View_Count,Like_Count,Dislike_Count,Favorite_Count,Comment_Count,time1,str(Thumbnail),Caption_Status)
mycursor.execute("insert into video values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",data3)
date1=pd.Timestamp(PublishedAt2)
#time1=pd.Timestamp.fromisoformat(Duration2).second()
t=Duration2.replace("PT","")
x=[]
for i in t:
    if i=="M":
        t=t.replace("M","")
        break
    else:
        if x!='S':
            x.append(i)
        print("x=",x)
        t=t.replace(i,"")
        print(t)
t=t.replace("S","")
print("t=",t)
x1="".join(x)
x1=x1.replace("S","")
print("x1=",x1)
if t=="":
    t=0
time1=int(x1)*60+int(t)
data4=(Video_Id2,Playlist_id,Video_Name2,Video_Description2,date1,View_Count2,Like_Count2,Dislike_Count2,Favorite_Count2,Comment_Count2,time1,str(Thumbnail2),Caption_Status2)
mycursor.execute("insert into video values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",data4)
date1=pd.Timestamp(Comment_PublishedAt)
print(date1)
Comment_Id=str(Comment_Id)
Video_Id=str(Video_Id)
Comment_Text=str(Comment_Text)
Comment_Author=str(Comment_Author)
data5=(Comment_Id,Video_Id,Comment_Text,Comment_Author,date1)
mycursor.execute("insert into comment1 values (%s,%s,%s,%s,%s)",data5)
#date1=pd.Timestamp(Comment_PublishedAt1)
#data6=(Comment_Id1,Video_Id,Comment_Text1,Comment_Author1,date1)
#mycursor.execute("insert into comment1 values (%s,%s,%s,%s,%s)",data6)
#date1=pd.Timestamp(Comment_PublishedAt3)
#data7=(Comment_Id3,Video_Id2,Comment_Text3,Comment_Author3,date1)
#mycursor.execute("insert into comment1 values (%s,%s,%s,%s,%s)",data7)
date1=pd.Timestamp(Comment_PublishedAt4)
data8=(Comment_Id4,Video_Id2,Comment_Text4,Comment_Author4,date1)
mycursor.execute("insert into comment1 values (%s,%s,%s,%s,%s)",data8)
mydb.commit()
#mycursor.execute("select * from channel3")
print("Connection established")
#print(mydb)
#@st.cache_resource
#def init_connection():
 #  return mysql.connector.connect(**st.secrets["mysql"])
#conn=init_connection()
#conn=st.connection("my_sql_connection",type=SQLConnection)