import re
import os
import sys
import datetime

global no_category
global wrong_value
wrong_value = "Error occur. Not correct value."
no_category = "Category doesn't exist"

class CategoryManager:

    def __init__(self):
        self.file_name = "CategoriesList.txt"

    def check_file(self):
        """Return list of categories"""
        if os.path.isfile(self.file_name):
            text = open(self.file_name, "r+")
            r_categories = text.read()
            categories = re.split(r'[,\s]*', r_categories)
            text.close()
            return categories
        else:
            print("File not found.")

    def categories(self):
        category = self.check_file()
        return category

    def add_category(self):
        """Add category to CategoriesList"""
        while True:
            category_name = raw_input( "Enter a new category" )
            if category_name in self.check_file():
                print("Category already exist")
            else:
                cat = open(self.file_name,'a')
                cat.write("\n")
                cat.write(category_name)
                cat.close()
                print("Category is added")
                break

    def remove_category(self):
        """Remove category from CategoriesList"""
        while True:
            category_name = raw_input("Enter category to remove")
            if category_name not in self.check_file():
                print(no_category)
            else:
                f = open(self.file_name, "r+")
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != category_name + '\n' and i != category_name:
                        f.write(i)
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
                print(wrong_value)


class ExpenseManager:

    def menu(self):
        text_menu = """ 
                        Press 1 if you want to add expense
                        Press 2 if you want to remove expense
                        Press 3 if you want to see expenses by a month
                        Press 4 if you want to show expenses by a category
                        Press 5 if you want to exit expense manager
                        """
        while True:
            choose = raw_input( text_menu )
            try:
                if int(choose) == 1:
                    self.add_expense()
                elif int(choose) == 2:
                    self.remove_expense_date()
                elif int(choose) == 3:
                    txt = self.print_expenses_by_month()
                    print(txt)
                elif int(choose) == 4:
                    txt = self.print_expenses_by_category()
                    print(txt)
                elif int(choose) == 5:
                    print("Exit")
                    break
                else:
                    print(wrong_value)
            except(TypeError,ValueError):
                print(wrong_value)

    def add_expense(self):
        """Add new expense to file as a year"""
        year, month, day = self.date_expense()
        name, amount = self.detail_expense()
        file_name = str(year) + '.txt'
        try:
            add_e = open(file_name, 'a')
            add_e.write("\n")
            content_of_expense = year,month, day, name, amount
            str_content = str(content_of_expense)
            add_e.write(str_content)
            add_e.close()
        except (IOError, TypeError,ValueError):
            print("File not found.")

    def remove_expense_date(self):
        """Remove an expense from file as a year"""
        while True:
            year, month, day = self.date_expense()
            name, amount = self.detail_expense()
            content_of_expense = year, month, day, name, amount
            str_content = str(content_of_expense)
            file_name = str(year) + '.txt'
            if os.path.isfile(file_name):
                f = open(file_name, "r")
                lines = f.readlines()
                f.close()
                f = open(file_name, "w")
                for i in lines:
                    if i != str_content + '\n' and i != str_content:
                        f.write(i)
                f.close()
                break
            else:
                print("File not found.")

    def print_expenses_by_month(self):
        """Show expenses in year by a month"""
        f = file_object.open_file()
        month = raw_input("Enter a month")
        s_month = ' '+month
        find = ""
        for line in f:
            r_line = line.replace("(", " ")
            rr_line = r_line.replace(")", " ")
            n_line = rr_line.replace("\n", " ")
            list_line = n_line.split(",")
            for i, n in enumerate(list_line):
                if i == 1:
                    a = (''.join(map(str, n)))
                    if a == s_month:
                        find += line
        return find

    def print_expenses_by_category(self):
        """Show expenses in year by a category"""
        f = file_object.open_file()
        category = self.check_category()
        new_list = []
        for line in f:
            if category in line:
                new_list.append(line)
        return ' '.join(map(str, new_list))

    def date_expense(self):
        """Return year, month, day"""
        while True:
            year = int(raw_input("Enter a year"))
            month = int( raw_input("Enter a month"))
            day = int( raw_input("Enter a day"))
            if year >= 2016 and year <= 2050:
                datetime.datetime(year=year, month=month, day=day)
                file_name = str(year) + '.txt'
                if os.path.isfile(file_name):
                    break
                else:
                    txt = open(file_name, "w")
                    txt.close()
            else:
                print(wrong_value)
        return year, month, day

    def detail_expense(self):
        """Return name and amount of expense """
        name = self.check_category()
        amount = float(raw_input("Enter an amount of expense"))
        return name, amount

    def check_category(self):
        """Return name of category"""
        name = raw_input("Enter a name of category")
        if name not in category_object.check_file():
            print(no_category)
        else:
            return name

class Menu:

    def menu_content(self):
        while True:
            print("""
                    1.Press 1 If you want to Manage of Category
                    2.Press 2 If you want to Manage to expense 
                    3.Press 3 Exit from Manager
                    """)
            choose = raw_input("Enter a number")
            try:
                if int(choose) == 1:
                    category_object.menu()
                elif int(choose) == 2:
                    expense_object.menu()
                elif int(choose) == 3:
                    print("Exit")
                    sys.exit()
                else:
                    print(wrong_value)
            except(ValueError, TypeError):
                print(wrong_value)

class FileManager():

    def open_file(self):
        """Return content of file"""
        year = int(raw_input("Enter a year"))
        file_name = str(year) + '.txt'
        if os.path.isfile(file_name):
            f = open(file_name, "r+")
            return f
        else:
            print("File not found.")


category_object = CategoryManager()
expense_object = ExpenseManager()
file_object = FileManager()
menu_object = Menu()
menu_object.menu_content()




