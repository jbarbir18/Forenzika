import sqlite3
import datetime
import os
import json
import pdfkit
import urllib.parse


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

        years = duration.days % 365 // 365
        months = (duration.days % 365) // 30
        days = (duration.days % 365) % 30
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        seconds = duration.seconds % 60

        fileAge = f"Age of file is: {years}y {months}m {days}d {hours}h {minutes}m"
        return fileAge
    else:
        return "Error while calculating age of file"


def calculate_top_visits(filePath, topNum):
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()
    cursor.execute("SELECT url, visit_count FROM urls")
    history_entries = cursor.fetchall()
    connection.close()

    visit_counts = {}
    for entry in history_entries:
        url = entry[0]
        count = entry[1]
        visit_counts[url] = visit_counts.get(url, 0) + count
    
    sorted_visits = sorted(visit_counts.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    result.append(f"Top {topNum} Most Visited Pages:")
    for i, (url, count) in enumerate(sorted_visits[:topNum], start=1):
        result.append(f"{i}. {url}")
    
    if len(sorted_visits) < topNum:
        result.append(f"Less than {topNum} URLs found in browsing history.")
    
    return result


def calculate_page_visits(filePath, pageName):
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM urls")

    history_entries = cursor.fetchall()
    page_prompt_num = cursor.execute(f"SELECT * FROM urls WHERE url LIKE '%{pageName}%'")
    page_entries = cursor.fetchall()

    page_visits_count = len(page_entries)
    return page_visits_count


def find_recently_visited_pages(filePath, numPages):
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()
    cursor.execute("SELECT url, last_visit_time FROM urls ORDER BY last_visit_time DESC")
    history_entries = cursor.fetchall()
    connection.close()

    result = []
    result.append(f"Most Recent {numPages} Visited Pages:")
    for i, (url, _) in enumerate(history_entries[:numPages], start=1):
        result.append(f"{i}. {url}")
    
    if len(history_entries) < numPages:
        result.append(f"Less than {numPages} URLs found in browsing history.")
    
    return result


def identify_popular_domains(filePath, topNum):
    connection = sqlite3.connect(filePath)
    cursor = connection.cursor()
    cursor.execute("SELECT url, visit_count FROM urls")
    history_entries = cursor.fetchall()
    connection.close()

    domain_counts = {}
    for entry in history_entries:
        url = entry[0]
        count = entry[1]
        domain = urllib.parse.urlparse(url).netloc
        domain_counts[domain] = domain_counts.get(domain, 0) + count
    
    sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    result.append(f"Top {topNum} Most Popular Domains:")
    for i, (domain, count) in enumerate(sorted_domains[:topNum], start=1):
        result.append(f"{i}. {domain} - Visits: {count}")
    
    if len(sorted_domains) < topNum:
        result.append(f"Less than {topNum} domains found in browsing history.")
    
    return result









    






