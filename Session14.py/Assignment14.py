import json

#1. Use open() in write mode to create a file called my_playlist.txt and write the names of 5 songs you listened to this week, 
#   each on a new line.

my_playlist = ['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']

file = open("my_playlist.txt", "w")

for song in my_playlist:
    file.write(song+"\n")

file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

#2. Read the my_playlist.txt file you created and print each song name in uppercase using Python file handling.

file = open("my_playlist.txt", "r")

for song in file:
    print(song.upper(), end="")

file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

#3. Download a sample CSV file of IPL cricket match scores (or create your own with columns: Match, Team1, Team2, Winner), 
#   then write Python code to read the CSV and print the name of the winning team for each match.


file = open("ipl_matches.csv", "r")

file.readline()

for line in file:
    data = line.strip().split(",")
    print("Winning Team:", data[3])

file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

#4.Given a JSON file named user_profile.json containing details like username, followers, and bio (similar to an Instagram profile), use the
# json module to load the file and print the username and number of followers.

file = open("user_profile.json", "r")

data = json.load(file)

print("Username:", data["username"])
print("Followers:", data["followers"])

file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

#5.Use pathlib to check if a file called zomato_orders.json exists in your current directory, and print an appropriate message if it is 
#  found or not.<br><br><em><strong>Hint:</strong> Use Path('zomato_orders.json').exists() from the pathlib module.</em>

from pathlib import Path

file = Path("zomato_orders.json")

if file.exists():
    print("File found!")
else:
    print("File not found!")