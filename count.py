import sqlite3

# Specify the path to the Chrome history file
history_file_path = r'C:\Users\Josip\AppData\Local\Google\Chrome\User Data\Profile 1\History'

# Connect to the SQLite database file
connection = sqlite3.connect(history_file_path)
cursor = connection.cursor()

# Execute a query to retrieve the browsing history
cursor.execute("SELECT * FROM urls")

# Fetch all the results
history_entries = cursor.fetchall()

youtube_prompt = cursor.execute("SELECT * FROM urls WHERE url LIKE '%youtube.com%'")
youtube_entries = cursor.fetchall()
youtube_visit_count = len(youtube_entries)

print(youtube_visit_count)


# Process and print the history entries
# for entry in history_entries:
#     url = entry[1]  # Column 1 contains the URL
#     title = entry[2]  # Column 2 contains the title (if available)
#     visit_count = entry[3]  # Column 3 contains the visit count
#     last_visit_time = entry[5]  # Column 5 contains the last visit time

#     print("URL:", url)
#     print("Title:", title)
#     print("Visit Count:", visit_count)
#     print("Last Visit Time:", last_visit_time)
#     print()

# Close the database connection
connection.close()
