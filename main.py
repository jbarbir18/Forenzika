import helperFunctions

global_object = {
    "name": "John",
    "age": 30
}


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

def option4():
    print("Export User Data")
    print()
    fileName = input("Enter Name of Exported File")
    helperFunctions.export_user_data(global_object, fileName)

    temp = input("Enter Any Key to Continue")

def display_menu():
    print("Menu:")
    print("1. Calculate Age of File")
    print("2. Calculate Top Visits")
    print("3. Calculate Page Visits")
    print("4. Export User Data")
    print("0. Exit")

def main():
    # Specify the path to the Chrome history file
    history_file_path_raw = input("Enter file path to Chrome history file, example: 'C:\Users\User\... ")
    history_file_path = rf'{history_file_path_raw}'

    while True:
        display_menu()
        choice = input("Enter your choice (0-4): ")
        
        if choice == "1":
            option1(history_file_path)
        elif choice == "2":
            option2(history_file_path)
        elif choice == "3":
            option3(history_file_path)
        elif choice == "4":
            option4()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
