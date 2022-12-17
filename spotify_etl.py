import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "31mulglqhsuu24zwayd5kni57ufa" # your Spotify username 
TOKEN = "BQCUsJsveu3OO9Z-v3lEJtBUS6Whym66I-3Wnp0NeTTfOi8_D592aBHZ6SjYYf-cWnYd6lQzDEJOzu-0DgAun7rFaoqVoGY4UUHPqCXS6meYW5KSxzYcGZp8ZrMpSdlPRQTlGHQFzxTOVf6UcKj2aFzkYILLw4SeZyuiGZ1i8OwiAcSqBX6CvBKMEhbiulLgaNHNT6rzNJ1g" # your Spotify API token

# Generate your token here:  https://developer.spotify.com/console/get-recently-played/

if __name__ == "__main__":

# Extract part of the ETL process
    headers = {
        "Accept": "application/json",
        "Content_Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=5)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()
#print(data)

#interested fields  
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

  # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
      
# Prepare a dictionary in order to turn it into a pandas dataframe below       
    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }

    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])

    print(song_df)
