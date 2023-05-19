import sqlite3
import datetime
import os
import json
import pdfkit

#Calculates the age of the oldest record in the file
def calculate_file_age(filePath):
    #Connect to the database
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()

    #Execute query
    cursor.execute("SELECT MIN(last_visit_time) FROM urls")
    oldest_timestamp = cursor.fetchone()[0]
    
    #Close db connection
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



def calculate_top_visits(filePath, topNum):
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()
    cursor.execute("SELECT url, visit_count FROM urls")
    history_entries = cursor.fetchall()
    connection.close()

    # Create a dictionary to store visit counts for each URL
    visit_counts = {}

    # Iterate through the history entries and update visit counts
    for entry in history_entries:
        url = entry[0]
        count = entry[1]
        visit_counts[url] = visit_counts.get(url, 0) + count
    
    sorted_visits = sorted(visit_counts.items(), key=lambda x: x[1], reverse=True)

    print(f"Top {topNum} Most Visited Pages:")
    for url, count in sorted_visits[:topNum]:
        print("URL:", url)
        print("Visit Count:", count)
        print()
    
    if len(sorted_visits) < topNum:
        print(f"Less than {topNum} URLs found in browsing history.")

def calculate_page_visits(filePath, pageName):
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM urls")

    # Fetch all the results - not working atm
    history_entries = cursor.fetchall()
    page_prompt_num = cursor.execute(f"SELECT * FROM urls WHERE url LIKE '%{pageName}%'")
    page_entries = cursor.fetchall()

    page_visits_count = len(page_entries)

def export_user_data(objectData, fileName):
    json_data = json.dumps(objectData, indent=4)
    temp_html_filename = "temp.html"

    with open(temp_html_filename, "w") as file:
        file.write(f"<pre>{json_data}</pre>")
    
    pdfkit.from_file(temp_html_filename, fileName)

    os.remove(temp_html_filename)






    






