# "os" is used to clear the console among other things. 
# "time" is used to create delay so the user has time to read things and or knows that their input is being processed. 
import sqlite3, time, os

os.system("clear")

conn = sqlite3.connect("MusicData.db")

cursor = conn.cursor()

# Function that can be called upon if the user is unser of what to do.   
def help():
    print("\nWhen inputting columns there must only be spaces between the column names. You can only input three columns at once.")
    print("If there is a gap in the data output the data is missing. This is normal in most instances.")
    ask_again()

# List of all of the column names from the dataset. 
column_names = ["song_id","track_name","artist_name","artist_count","released_year","released_month","released_day", "in_spotify_charts", "streams", "in_apple_charts","bpm", "key", "mode"]

# Function that lets the user search information using column names. 
def column_search():
    print("These are the names of the columns:")
    print(str(column_names) + "\n")
    while True:
        search = input("Please enter your desired column name\s, enter a space between each column name. If you experiance a problem enter help\n").lower()
        if search == "help":
            help()
        # Splits all words in user input into a list. 
        selected_columns = search.split()
        # Creates a variable containing how many words are in the list. 
        selected_columns_len = len(selected_columns)
        # Checks 
        for column in range(selected_columns_len):
            if selected_columns[column] in column_names:
                continue
            else:
                print("\nLooks like one of your inputted columns names does not exist or is spelt wrong")
                column_search()
        # Checks if there is only one word in the list
        if selected_columns_len == 1:
            cursor.execute("SELECT " + selected_columns[0] + " FROM MusicData;")
            search = cursor.fetchall()
            for row in search:
                print(f"{row[0]}")
                time.sleep(0.05)
            ask_again()
        elif selected_columns_len > 1 and selected_columns_len <= 3:
            # Loop that goes around as many times as the amount of columns in the users input. 
            for i in range(selected_columns_len):
                # Checks if this is first time around loop and saves the first word in the list to query. 
                if i == 0:
                    query = selected_columns[i]
                else:
                    # Saves whats in query with the next word from the users input as well as a comma. 
                    query = query + "," + selected_columns[i]
                i += 1 
            # Concatonates query and "SELECT" and "FROM MusicData" so that one SQL query can be used.
            query_syntax = "SELECT " + query + " FROM MusicData;"
            cursor.execute(query_syntax)
            search = cursor.fetchall()
            # Checks the length of the variable and acts accordingly
            if selected_columns_len == 3:
                for row in search:
                    row_content = str(row[0])
                    row_content = row_content.ljust(50)
                    row_content_2 = str(row[1])
                    row_content_2 = row_content_2.ljust(50)
                    print(row_content + row_content_2 + str(row[2]))
            else:
                #  Repeats as many times as tuples in search. 
                for row in search:
                    row_content = str(row[0])
                    row_content = row_content.ljust(45)
                    row_content_2 = str(row[1])
                    row_content_2 = row_content_2.ljust(50)
                    print(row_content + row_content_2 )
            ask_again()
        else:
            print("You entered more than possible to fit on the terminal, you can only select 3 columns, please try again.")
            column_search()
   
# Function that calls all tracks from the database and formats it. 
def get_all_tracks():
    cursor.execute("SELECT track_name FROM MusicData;")
    track_names = cursor.fetchall()
    for track_name in track_names:
        print(f"{track_name[0]}")
        time.sleep(0.05)
    ask_again()

# Function that gets track names and the streams associated with that track at the time the data was taken. 
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
            again = input("\nDo you want to ask another query?(yes/no)\n").upper()
            if again == "YES":
                print("\n")
                menu()
            elif again == "NO":
                exit()
            else:
                print("You entered invalid input, you have to answer by stating yes, or no.\n\n")
                time.sleep(3)
        except ValueError:
            continue

# Main menu function that gives the user options for querys they can ask. 
def menu():
    while True:
        try:
            query = int(input("1.Get all song names\n\n2.Get songs and their total streams\n\n3.Get artist names\n\n4.Search by column name\n\n5.Help\n\n6.Clear console\n\n"))
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
            elif query == 6:
                os.system("clear")
                menu()
        except ValueError:
            print("You entered invalid input")
            time.sleep(2)

# Explains what the program is
print("This is a dataset containing 59 of the top songs from 2023")
time.sleep(5)
os.system("clear")

menu()

conn.commit()

conn.close()