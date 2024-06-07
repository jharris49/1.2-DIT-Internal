import sqlite3, time, os

os.system("clear")

conn = sqlite3.connect("MusicData.db")

cursor = conn.cursor()

def get_all_tracks():
    cursor.execute("SELECT track_name FROM MusicData;")
    track_names = cursor.fetchall()
    for track_name in track_names:
        print(f"{track_name[0]}")
        time.sleep(0.05)

def get_all_streams_tracks():
    cursor.execute("SELECT track_name, streams FROM MusicData;")
    streams_tracks = cursor.fetchall()
    for streams_track in streams_tracks:
        print(f"{streams_track[0]} has {streams_track[1]} streams")
        time.sleep(0.05)
        
def get_artist_name():
    cursor.execute("SELECT artist(s)_name FROM MusicData;")
    artist_names = cursor.fetchall()
    for artist_name in artist_names:
        print(f"{artist_name[0]}")
        time.sleep(0.05)


print("This is a dataset containing 150 of the top songs from 2023")
time.sleep(2.2)
os.system("clear")

while True:
    query = int(input("1.Get all song names\n\n2.Get songs and their total streams\n\n3.Get artist names\n\n"))
    os.system("clear")
    if query == 1:
        get_all_tracks()
        break
    elif query == 2:
        get_all_streams_tracks()
        break
    elif query == 3:
        get_artist_name()
        break
    else:
        break

conn.commit()

conn.close()