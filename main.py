import re
import sys
import matplotlib.pyplot as plt

class CategoryManager:

    def __init__(self):
        self.file_name = "CategoriesList.txt"

    def check_file(self):
        #check if file exists
        try:
            text = open(self.file_name, "r+")
            r_categories = text.read()
            categories = re.split(r'[,\s]*',r_categories)
            text.close()
            return categories
        except (IOError):
            print("File not found.")

    def categories(self):
        category = self.check_file()
        return category

    def add_category(self):
        while True:
            category_name = raw_input( "Enter a new category" )
            if category_name in self.check_file():
                print("Category already exist")
            else:
                #append file if category is added
                cat = open(self.file_name,'a')
                cat.write("\n")
                cat.write(category_name)
                cat.close()
                print("Category is added")
                break

    def remove_category(self):
        while True:
            category_name = raw_input("Enter category to remove")
            if category_name not in self.check_file():
                print("Category doesn't exist")
            else:
                f = open( self.file_name, "r+" )
                d = f.readlines()
                f.seek( 0 )
                for i in d:
                    if i != category_name + '\n' and i != category_name:
                        f.write( i )
                f.truncate()
                f.close()
                print("Category is removed")
                break

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
                elif int(choose) == 3:
                    for category in self.check_file():
                        print(category)
                elif int(choose) == 4:
                    print("Exit from editor")
                    break
                else:
                    print("Not correct value, try again")
            else:
                print("Not correct value, try again")

class ExpenseManager:

    def menu(self):
        text_menu = """ 
                        Press 1 if you want to add expense
                        Press 2 if you want to remove expense
                        Press 3 if you want to see expenses form date to date
                        Press 4 if you want to show expenses by a category
                        Press 5 if you want to exit expense manager
                        """
        while True:
            choose = raw_input( text_menu )
            if choose.isdigit():
                if int( choose ) == 1:
                    self.check_file()
                    self.add_expense()
                elif int( choose ) == 2:
                    pass
                elif int( choose ) == 3:
                    pass
                elif int( choose ) == 4:
                    pass
                elif int( choose ) == 4:
                    print("Exit")
                    False
                else:
                    print("Not correct value, try again")
            else:
                print("Not correct value, try again")

    def check_file(self):
        pass

    def add_expense(self):
        year, month, day = self.date_expense()
        name, amount = self.detail_expense()
        file_name = str( year ) + 'txt'
        try:
            add_e = open( file_name, 'a' )
            add_e.write( "\n" )
            content_of_expense = year, month, day, name, amount
            str_content = str(content_of_expense)
            add_e.write(str_content)
            add_e.close()
        except (IOError):
            print("File not found.")

    def remove_expense(self):
        self.check_file()

    def print_expenses(self):
        pass

    def date_expense(self):
        #function to return date of expenses
        year = int(raw_input( "Enter a year"))
        month = int( raw_input( "Enter a month" ) )
        day = int( raw_input( "Enter a day" ) )
        file_name = str(year)+'txt'
        try:
            txt  = open(file_name, "r")
            txt.close()
        except (IOError):
            open( file_name, "w" )
            file_name.close()
        return year,month,day

    def detail_expense(self):
        #function to return details of expense
        while True:
            name = raw_input("Enter a name of category")
            if name not in category_object.check_file():
                print("Category doesn't exist")
            else:
                amount = raw_input( "Enter an amount of expense" )
                return name, amount



category_object = CategoryManager()
expense_object = ExpenseManager()

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
                    expense_object.menu()
                elif int(choose) == 3:
                    print("Exit")
                    sys.exit()
                else:
                    print("Not correct value, try again")
            else:
                print("Not correct value, try again")


class FileManager():
    pass



file_object = FileManager()

menu_object = Menu()
menu_object.menu_content()




