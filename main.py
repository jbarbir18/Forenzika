import helperFunctions
import json
##PATH TO LOCAL FILE : "C:\Users\Josip\AppData\Local\Google\Chrome\User Data\Profile 1\History"


class UserData:
    def __init__(self):
        self.FileAge = ""
        self.TopVisits = []
        self.PageVisitsPage = ""
        self.PageVisitsCount = 0

def store_object_as_json(global_object):
    json_file_path = 'data.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(global_object.__dict__, json_file, indent=4)


def option1(filePath):
    print("Calculate Age of File")
    print()
    helperFunctions.calculate_file_age(filePath)

    temp = input("Enter Any Key to Continue")
    

def option2(filePath):
    print("Calculate Top Visits")
    print()
    topNum = input("Enter top number of pages to display")
    helperFunctions.calculate_top_visits(filePath, topNum)

    temp = input("Enter Any Key to Continue")
   

def option3(filePath):
    print("Calculate Page Visits")
    print()
    pageName = input("Enter Page Name")
    helperFunctions.calculate_page_visits(filePath, pageName)

    temp = input("Enter Any Key to Continue")


def display_menu():
    print("Menu:")
    print("1. Calculate Age of File")
    print("2. Calculate Top Visits")
    print("3. Calculate Page Visits")
    print("0. Exit")

def main():
    # initialize variables
    user_data = UserData()
    history_file_path = "history"

    # extract data from history file

    # calculate file age
    user_data.FileAge = helperFunctions.calculate_file_age(history_file_path)

    # calculate top visited pages
    user_data.TopVisits = helperFunctions.calculate_top_visits(history_file_path, 10)

    # calculate specific page visits
    user_data.PageVisitsCount = helperFunctions.calculate_page_visits(history_file_path, "youtube")

    # export data as json to data.json file
    store_object_as_json(user_data)



    

if __name__ == "__main__":
    main()
