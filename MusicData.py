# "os" is used to clear the console among other things. 
# "time" is used to create delay so the user has time to read things and or knows that their input is being processed. 
import sqlite3, time, os

os.system("clear")

# Creates connection with db file.
conn = sqlite3.connect("MusicData.db")

# Creates a way for python to run SQL commands for the database.
cursor = conn.cursor()

# Function that can be called upon if the user is unser of what to do.   
def help():
    print("\nIf you want to exit the program enter 'no' when you are asked 'Do you want to enter another query'.")
    print("When inputting columns there must only be spaces between the column names. You can only input three columns at once.")
    print("If there is a gap in the data output the data is missing. This is normal in most instances.")
    print("If when searching for songs the output comes out with nothing it means that you either entered a song that is not on the database ")
    print("or, you misspelt the song name. You can access all of the song name and artist names from the menu.")
    print("When updating and deleting functions if you are using SQLite studio you may have to refresh your database to see the changes you have made.")
    ask_again()

# List of all of the column names from the dataset. 
column_names = ["song_id","track_name","artist_name","artist_count","released_year","released_month","released_day", "in_spotify_charts", "streams", "in_apple_charts","bpm", "key", "mode"]

# Function that lets the user search information using column names. 
def column_search():
    print("These are the names of the columns:")
    print(str(column_names) + "\n")
    while True:
        search = input("Please enter your desired column name\s, enter a space between each column name. You can only input 3 column names to search with.\nIf you want to exit or experiance a problem enter help.\n").lower()
        if search == "help":
            help()
        # Splits all words in user input into a list. 
        selected_columns = search.split()
        # Creates a variable containing how many words are in the list. 
        selected_columns_len = len(selected_columns)
        # Repeats as many times as the amount of column names inputted. 
        for column in range(selected_columns_len):
            # Checks if the first, second etc column is in the column names list. 
            if selected_columns[column] in column_names:
                continue
            else:
                print("\nLooks like one of your inputted columns names does not exist or is spelt wrong")
                column_search()
        # Formatting.
        print("")
        # Checks if there is only one word in the list
        if selected_columns_len == 1:
            cursor.execute("SELECT " + selected_columns[0] + " FROM MusicData;")
            search = cursor.fetchall()
            # Data formatting. Repeats as many times as tuples in search.
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
            # Concatonates query and "SELECT" and "FROM MusicData" so that one SQL query can be returned. 
            query_syntax = "SELECT " + query + " FROM MusicData;"
            cursor.execute(query_syntax)
            search = cursor.fetchall()
            # Checks the length of the variable and acts accordingly
            if selected_columns_len == 3:
                # Formatting
                for row in search:
                    row_content = str(row[0])
                    row_content = row_content.ljust(50)
                    row_content_2 = str(row[1])
                    row_content_2 = row_content_2.ljust(50)
                    print(row_content + row_content_2 + str(row[2]))
            else:
                # Formatting. Repeats as many times as tuples in search. 
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
   
# Function that gets all track names from the database and formats it. 
def get_all_tracks():
    cursor.execute("SELECT track_name FROM MusicData;")
    # Formatting.
    print("")
    track_names = cursor.fetchall()
    # Formatting. Repeats as many tuples in track_names. 
    for track_name in track_names:
        print(f"{track_name[0]}")
        time.sleep(0.05)
    ask_again()

# Function that gets track names and the streams associated with that track at the time the data was taken. 
# This function also formatting this data.  
def get_all_streams_tracks():
    cursor.execute("SELECT track_name, streams FROM MusicData;")
    streams_tracks = cursor.fetchall()
    # Formatting.
    print("")
    for streams_track in streams_tracks:
        print(f"{streams_track[0]} has {streams_track[1]} streams")
        time.sleep(0.05)
    ask_again()

# Function that returns all artists and formats it.         
def get_artist_name():
    cursor.execute("SELECT artist_name FROM MusicData")
    artist_names = cursor.fetchall()
    # Formatting.
    print("")
    for artist_name in artist_names:
        print(f"{artist_name[0]}")
        time.sleep(0.05)
    ask_again()

# Function that akss the user if theyw ant to ask another query. 
def ask_again():
    time.sleep(2)
    while True:
        # Error catching try and except. While loop above will repeat until valid input entered. 
        try:
            again = input("\nDo you want to ask another query?(yes/no)\n").upper()
            if again == "YES":
                print("\n")
                menu()
            elif again == "NO":
                exit("Thank you for using this program.")
            else:
                print("You entered invalid input, you have to answer by stating yes, or no.\n\n")
                time.sleep(3)
        except ValueError:
            continue

# Main menu function that gives the user options for querys they can ask. 
def menu():
    while True:
        try:
            query = int(input("1.Get all song names\n\n2.Get songs and their total streams\n\n3.Get artist names\n\n4.Search by column name\n\n5.Search by song name\n\n6.Search by artist name\n\n7.Update song streams\n\n8.Delete a song and its data\n\n9.Help and exit\n\n10.Clear terminal\n\n"))
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
                column_search()
                break
            elif query == 5:
                search_by_song_name()
                break
            elif query == 6:
                search_by_artist()
                break
            elif query == 7:
                update_streams()
                break
            elif query == 8:
                delete_data()
                break
            elif query == 9:
                help()
                break
            elif query == 10:
                os.system("clear")
                menu()
            else:
                print("You entered invalid input")
                time.sleep(2)
        except ValueError:
            print("You entered invalid input")
            time.sleep(2)

# Function that lets the user search through the database by artist name or characters in an artists name.
# It returns all data associated with the users inputted artist name or characters. 
def search_by_artist():
    while True:
        try:
            artist_search = input("\nPlease enter the artist you want to search for or the characters in an artists name you want to search for. If no data comes back you either entered an artist that is not in the database or misspelt something. Enter help if you need assistance or want to exit.\n\n")
            if artist_search == "help":
                help()
            break
        except ValueError:
             print("Looks like you entered invalid input, please try again.")
    # Adds the user input into a SQL statement and searches for artists names conataining their input. 
    cursor.execute("SELECT * FROM MusicData WHERE artist_name LIKE '%" + artist_search + "%';")
    artist_search = cursor.fetchall()
    #Checks if the length of the output is zero. If it is it prints an according error message. 
    if len(artist_search) == 0:
        print("Looks like you misspelt an artists name, entered one that does not exist, or entered a character that is not in an artists name.")
        time.sleep(2)
        search_by_artist()
    # Formatting. 
    for row in artist_search:
        print("")
        for i in range(len(column_names)):
            print(str(column_names[i]) + ": " + str(row[i]))
            time.sleep(0.07)
    ask_again()


# This function lets the user search through the database with their entered song name. It returns all data assosiated with that song. 
def search_by_song_name():
    while True:
        try:
            song_search = input("\nPlease enter the song you want to search for. If the song does not come up you either spelt it wrong or entered a song that is not in the database. Enter help if you need assistance or want to exit.\n\n")
            if song_search == "help":
                help()
            break
        except ValueError:
            print("Looks like you entered invalid input, please try again.")
    cursor.execute("SELECT * FROM MusicData WHERE track_name = '" + str(song_search) + "';") 
    song_search = cursor.fetchall()
    # Catches if what the user inputted is not in the database. 
    if len(song_search) == 0:
        print("Looks like you misspelt a song name or entered one that does not exist.")
        time.sleep(2)
        search_by_song_name()
    else:
        # Formatting
        print("")
        for row in song_search:
            for i in range(len(column_names)):
                print(str(column_names[i]) + ": " + str(row[i]))
                time.sleep(0.2)
        ask_again()

# The purpose of this function is to update the number of streams for a song in the database. 
# This function returns all data associated with the song and then gets the user to input how many streams and then executes and commits this.  
def update_streams():
    # Formatting
    print("")
    while True:
        try:
            song_update = input("Please enter the name of the song you want to update. If you experience a problem or want to exit enter help.\n") 
            # Checks if user inputs help and takes them to the help menu if so. 
            if song_update == "help":
                help()
            break
        except ValueError:
            print("Looks like you entered invalid input, please try again.")
    cursor.execute("SELECT * FROM MusicData WHERE track_name = '" + str(song_update) + "';") 
    song_search = cursor.fetchall()
    # Catches if what the user inputted is not in the database. 
    if len(song_search) == 0:
        print("Looks like you misspelt a song name or entered one that does not exist.")
        update_streams()
    else:
        print("")
        print("Here are the records currently associated with " + song_update)
        # Prints the records currently associated with the users inputted song. 
        for row in song_search:
            for i in range(len(column_names)):
                print(str(column_names[i]) + ": " + str(row[i]))
                time.sleep(0.2)
        while True:
            try:
                # Asks and saves the new amount of streams to a variable. 
                updated_streams = int(input("\nPlease enter the new value of streams here. If you want to exit please enter -1: "))
                # Checks if the user wants to exit.  
                if updated_streams == -1:
                    print("You are exiting to the menu now.\n")  
                    time.sleep(2)
                    menu()
                    break
                # Checks that the amount of streams inputted is possible.
                elif updated_streams > 1000000000000 or updated_streams < 0:
                    print("Number of streams is invalid. Please try again.")
                    continue
                else:
                    break
            except ValueError:
                print("You entered invalid input")
                continue
        # Executes a SQL update function using the inputted data and the song_id. 
        cursor.execute("UPDATE MusicData SET streams = " + str(updated_streams) + " WHERE song_id = " + str(row[0]) + ";")
        # Commits changes to SQL
        conn.commit()
        # Prints that the update was succesfull. 
        print(cursor.rowcount, "record succesfully updated")
        ask_again()



# The purpose of this function is to delete rows of data from the databse. 
# This function returns all data associated with the song and then gets the user to confirm if they want to delete it and then executes and commits this.  
def delete_data():
    # Formatting
    print("")
    while True:
        try:
            song_delete = input("Please enter the name of the song you want to delete. If you experience a problem or want exit enter help.\n") 
            # Checks if user inputs help and takes them to the help menu if so. 
            if song_delete == "help":
                help()
            break
        except ValueError:
            print("Looks like you entered invalid input, please try again.")
    cursor.execute("SELECT * FROM MusicData WHERE track_name = '" + str(song_delete) + "';") 
    song_search = cursor.fetchall()
    # Catches if what the user inputted is not in the database. 
    if len(song_search) == 0:
        print("Looks like you misspelt a song name or entered one that does not exist.")
        update_streams()
    else:
        print("")
        print("Here are the records currently associated with " + song_delete)
        # Prints the records currently associated with the users inputted song. 
        for row in song_search:
            for i in range(len(column_names)):
                print(str(column_names[i]) + ": " + str(row[i]))
                time.sleep(0.2)
        while True:
            try:
                # Asks if the user wants to delete the data.  
                confirm_delete = input("\nAre you sure you want to delete " + str(row[1]) + " and its data (yes/no): ").upper()
                # Checks the users input and acts accordingly.  
                if confirm_delete == "YES":
                    break
                elif confirm_delete == "NO":
                    print("Ok, you are being taken back to the menu now.\n")
                    time.sleep(2)
                    menu()
                    break
            except ValueError:
                print("You entered invalid input")
                continue
        # Executes the SQL delete statement the user wanted. 
        cursor.execute("DELETE FROM MusicData WHERE song_id = " + str(row[0]) + ";")
        # Commits changes to SQL
        conn.commit()
        # Prints that the delete was succesfull. 
        print(cursor.rowcount, "record succesfully deleted")
        ask_again()


# Explains what the program is and what is in it. 
print("This is a dataset containing some of the top songs from 2023")
time.sleep(5)
os.system("clear")

# Calls function which then starts the main program. 
menu()

conn.commit()

# Closes the connection to the database. 
conn.close()