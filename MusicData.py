# "os" is used to clear the console among other things. 
# "time" is used to create delay so the user has time to read things and or knows that their input is being processed. 
import sqlite3, time, os

os.system("clear")

conn = sqlite3.connect("MusicData.db")

cursor = conn.cursor()

# Function that can be called upon if the user is unser of what to do.   
def help():
    print("Here is a list of all of the column names:")
    print("track_name, artist_name, artist_count,released_year, released_month, released_day, in_spotify_charts, streams, in_apple_charts, bpm, key, mode")
    ask_again()

# Function that lets the user search information using column names. 
def column_search():
    print("Column name must correctly be spelt")
    search = input("Please enter your desired column name, if you do not know the column names, enter help\n").lower().strip()
    if search == "help":
        help()
    cursor.execute("SELECT " + search + " FROM MusicData;")
    search = cursor.fetchall()
    print(search)

# Function that calls all tracks from the database and formats it. 
def get_all_tracks():
    cursor.execute("SELECT track_name FROM MusicData;")
    track_names = cursor.fetchall()
    for track_name in track_names:
        print(f"{track_name[0]}")
        time.sleep(0.05)
    ask_again()

# Function that gets track names and the streams associated with that track at teh time the data was taken. 
# This function also formatting this data.  
def get_all_streams_tracks():
    cursor.execute("SELECT track_name, streams FROM MusicData;")
    streams_tracks = cursor.fetchall()
    for streams_track in streams_tracks:
        print(f"{streams_track[0]} has {streams_track[1]} streams")
        time.sleep(0.05)
    ask_again()

# Function that returns all artists and formats it.         
def get_artist_name():
    cursor.execute("SELECT artist_name FROM MusicData")
    artist_names = cursor.fetchall()
    for artist_name in artist_names:
        print(f"{artist_name[0]}")
        time.sleep(0.05)
    ask_again()

# Function that akss the user if theyw ant to ask another query. 
def ask_again():
    time.sleep(2)
    while True:
        try:
            again = input("\nDo you want to ask another query?\n").upper()
            if again == "YES":
                print("\n")
                menu()
            elif again == "NO":
                break
            else:
                print("You entered invalid input, you have to answer by stating yes, or no.\n\n")
                time.sleep(3)
        except ValueError:
            continue

# Main menu function that gives the user options for querys they can ask. 
def menu():
    while True:
        try:
            query = int(input("1.Get all song names\n\n2.Get songs and their total streams\n\n3.Get artist names\n\n4.Search by column name\n\n5.HELP\n\n"))
            if query == 1:
                get_all_tracks()
                break
            elif query == 2:
                get_all_streams_tracks()
                break
            elif query == 3:
                get_artist_name()
                break
            elif query == 4:
                os.system("clear")
                column_search()
                break
            elif query == 5:
                help()
                break
        except ValueError:
            print("You entered invalid input")
            time.sleep(2)

# Explains what the program is
print("This is a dataset containing 60 of the top songs from 2023")
time.sleep(2.2)
os.system("clear")

menu()

conn.commit()

conn.close()