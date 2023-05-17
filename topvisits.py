import sqlite3

# Specify the path to the Chrome history file
history_file_path = r'C:\Users\Josip\AppData\Local\Google\Chrome\User Data\Profile 1\History'

# Connect to the SQLite database file
connection = sqlite3.connect(history_file_path)
cursor = connection.cursor()

# Execute a query to retrieve the browsing history
cursor.execute("SELECT url, visit_count FROM urls")

# Fetch all the results
history_entries = cursor.fetchall()

# Close the database connection
connection.close()

# Create a dictionary to store visit counts for each URL
visit_counts = {}

# Iterate through the history entries and update visit counts
for entry in history_entries:
    url = entry[0]
    count = entry[1]
    visit_counts[url] = visit_counts.get(url, 0) + count

# Sort the visit counts in descending order
sorted_visits = sorted(visit_counts.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 most visited URLs
print("Top 10 Most Visited Pages:")
for url, count in sorted_visits[:10]:
    print("URL:", url)
    print("Visit Count:", count)
    print()

# If there are fewer than 10 URLs, print all of them
if len(sorted_visits) < 10:
    print("Less than 10 URLs found in browsing history.")

