import helperFunctions
import json
##PATH TO LOCAL FILE : "C:\Users\Josip\AppData\Local\Google\Chrome\User Data\Profile 1\History"


class UserData:
    def __init__(self):
        self.FileAge = ""
        self.TopVisits = []
        self.RecentVisits = []
        self.PopularDomains = []
        self.PageVisitsPage = "youtube"
        self.PageVisitsCount = 0

def store_object_as_json(global_object):
    json_file_path = 'data.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(global_object.__dict__, json_file, indent=4)

def main():
    # initialize variables
    user_data = UserData()
    history_file_path = "History"

    # extract data from history file

    # calculate file age
    user_data.FileAge = helperFunctions.calculate_file_age(history_file_path)

    # calculate top visited pages
    user_data.TopVisits = helperFunctions.calculate_top_visits(history_file_path, 10)

    # calculate recent visited pages
    user_data.RecentVisits = helperFunctions.find_recently_visited_pages(history_file_path, 10)

    # calculate most popular domains
    user_data.PopularDomains = helperFunctions.identify_popular_domains(history_file_path, 10)

    # calculate specific page visits
    user_data.PageVisitsCount = helperFunctions.calculate_page_visits(history_file_path, "youtube")
    
    # export data as json to data.json file
    store_object_as_json(user_data)
   

if __name__ == "__main__":
    main()
