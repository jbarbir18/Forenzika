import helperFunctions
import json
import webbrowser
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
    json_file_path = 'C:/Users/Josip/Desktop/Forenzika/GUI/src/assets/data.txt'
    with open(json_file_path, 'w') as json_file:
        json.dump(global_object.__dict__, json_file, indent=4)

def display_menu():
    print("Menu:")
    print("1. Analyse history file")
    print("2. Export to JSON")
    print("3. Open analysis file")
    print("0. Exit")

def option_1(historyFilePath):
    print("Analysing history file...")
    user_data = UserData()
    # extract data from history file

    # calculate file age
    user_data.FileAge = helperFunctions.calculate_file_age(historyFilePath)

    # calculate top visited pages
    user_data.TopVisits = helperFunctions.calculate_top_visits(historyFilePath, 10)

    # calculate recent visited pages
    user_data.RecentVisits = helperFunctions.find_recently_visited_pages(historyFilePath, 10)

    # calculate most popular domains
    user_data.PopularDomains = helperFunctions.identify_popular_domains(historyFilePath, 10)

    # calculate specific page visits
    user_data.PageVisitsCount = helperFunctions.calculate_page_visits(historyFilePath, "youtube")

    return user_data


def option_2(historyFilePath, object):
    print("Exporting JSON object...")
    
    # export data as json to data.json file
    store_object_as_json(object)

def option_3(url):
    print("Opening...")
    webbrowser.open(url)



def main():
    user_data_main = UserData()
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-3): ")
        history_file_path = "History"
        url = "file:///C:/Users/Josip/Desktop/Forenzika/data.html"

        if choice == "1":
            user_data_main = option_1(history_file_path)
        elif choice == "2":
            option_2(history_file_path, user_data_main)
        elif choice == "3":
            option_3(url)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
