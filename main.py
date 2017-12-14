import sys
import fileinput
from datetime import tzinfo, timedelta, datetime

class TZ(tzinfo):
    #funtion to manage format of data
    def utcoffset(self, dt):
        return timedelta(minutes=-399)

class CategoryManager:

    def __init__(self):
        self.file_name = "CategoriesList.txt"

    def check_file(self):
        #check if file exists
        try:
            text = open(self.file_name, "r+")
            print("Opened correctly.")
            r_categories = text.read()
            categories = r_categories.split( "\n" )
            text.close()
            return categories
        except (IOError):
            print("File not found.")
            sys.exit()

    def categories(self):
        pass

    def add_category(self):
        while True:
            category_name = raw_input("Enter a new category")
            if category_name in self.check_file():
                print("Category already exist")
                continue
            else:
                #append file if category is added
                cat = open(self.file_name,'a')
                cat.write("\n")
                cat.write(category_name)
                cat.close()
                print("Category is added")

    def remove_category(self):
        while True:
            category_name = raw_input("Enter category to remove")
            if category_name in self.check_file():
                for line in fileinput.input(self.file_name,inplace = True):
                    line = line.rstrip()
                    if category_name in line:
                        line.replace(category_name," ")
                    #print(line)
                print("Category is removed")
            else:
                print("Category doesn't exist")
                continue

    def menu(self):
        text_menu = """ 
                Press 1 if you want to add category
                Press 2 if you want to remove category
                Press 3 if you want to see categories
                Press 4 if you want to exit from edit
                """
        while True:
            choose = raw_input(text_menu)
            if choose.isdigit():
                if int(choose) == 1:
                    self.check_file()
                    self.add_category()
                elif int(choose) == 2:
                    self.remove_category()
                elif float(choose) == 3:
                    print(self.categories)
                elif float(choose) == 4:
                    print("Exit")
                    break
                else:
                    print("Not correct value, try again")
            else:
                print("Not correct value, try again")
                continue



class ExpenseManager:

    def expense(self):
        #function to return details of expense
        while True:
            name = raw_input("Enter name of category")
            if name not in self.categories:
                print("Category doesn't exists")
                continue
            else:
                amount = float("Enter an amount")
                day_expense = int(raw_input( "Enter a day"))
                month_expense = int(raw_input( "Enter a month"))
                year_expense = int(raw_input( "Enter a year"))
                date_expense = datetime( year_expense,month_expense,day_expense, tzinfo=TZ()).isoformat(' ')
                return name, amount,date_expense

category_object = CategoryManager()
category_object.check_file()

class Menu:

    def menu_content(self):
        while True:
            print("""
                    1.Press 1 If you want to Manage of Category
                    2.Press 2 If you want to Manage to expense 
                    3.Press 3 Exit from Manager
                    """)
            choose = raw_input("Enter a number")
            if choose.isdigit():
                if int(choose) == 1:
                    category_object.menu()
                elif int(choose) == 2:
                    pass
                elif float(choose) == 3:
                    print("Exit")
                    sys.exit()
                else:
                    print("Not correct value, try again")
            else:
                print("Not correct value, try again")
                continue

menu_object = Menu()
menu_object.menu_content()




