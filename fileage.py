import sqlite3
import datetime

# Specify the path to the Chrome history file
history_file_path = r'C:\Users\Josip\AppData\Local\Google\Chrome\User Data\Profile 1\History'

# Connect to the SQLite database file
connection = sqlite3.connect(history_file_path)
cursor = connection.cursor()

# Execute a query to retrieve the browsing history
cursor.execute("SELECT MIN(last_visit_time) FROM urls")

# Fetch the result
oldest_timestamp = cursor.fetchone()[0]

# Close the database connection
connection.close()

if oldest_timestamp is not None:
    # Convert the timestamp to a datetime object
    oldest_visit_time = datetime.datetime(1602, 1, 1) + datetime.timedelta(microseconds=oldest_timestamp)

    # Calculate the duration between the oldest record and the current time
    duration = datetime.datetime.now() - oldest_visit_time

    years = duration.days // 365
    months = (duration.days % 365) // 30
    days = (duration.days % 365) % 30
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = duration.seconds % 60

    print("Oldest Record Duration:")
    print("Years:", years)
    print("Months:", months)
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
else:
    print("No records found in the browsing history.")
