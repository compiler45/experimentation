import sys
from notebook import Notebook


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                        "1": self.make_new_entry,
                        "2": self.edit_entry,
                        "3": self.delete_entry,
                        "4": self.list_all_entries,
                        "5": self.list_books_for_author,
                        "6": self.quit,
                       }

    def run(self):
        while True:
            menu = ("Hi, please choose from one of the options below:\n\n" 
                    "1: Make a new entry for an author \n"
                    "2: Edit an entry \n"
                    "3: Delete an entry \n"
                    "4: List all entries.\n"
                    "5: List entries for an author\n"
                    "6: quit")
            print(menu)
            option = input("Option: ")
            action = self.choices.get(option)
            if action:
                action()

    def make_new_entry(self):
        author_name = input("Please enter the name of the author for which you would like to make a new entry: ")
        if not author_name:
            print("No name entered.")
        else:
            added = self.notebook.add_entry(author_name)
            if not added:
                print("An entry already exists for {}.\n".format(author_name))
            else:
                print("Entry for {} successfully created.\n".format(author_name))

    def show_edit_book_menu(self, entry):
        print("Would you like to add a new book, remove a book, or edit a book name? \n" 
               "1: Add a new book \n" 
               "2: Remove a book \n" 
               "3: Edit a book's name \n")
        option = input("Option: ")
        if not option:
            print("No option chosen.")
        else:
            if option == "1":
                book_name = input("Please enter the name of the book to be added: ")
                entry.add_book(book_name)
            elif option == "2":
                book_name = input("Please enter the name of the book to be removed: ")
                entry.remove_book(book_name)
            elif option == "3":
                old_book_name = input("Please enter the name of the book to be changed: ")
                new_book_name = input("Please enter the new name of the book: ")
                entry.edit_book(old_book_name, new_book_name)
            else:
                print("Invalid option.")

    def edit_entry(self):
        author_name = input("Please enter the name of the author whose entry you would like to edit: ")
        if not author_name:
            print("No name entered.")
        else:
            entry = self.notebook.get_entry_for_author(author_name)
            if not entry:
                print("No entry exists for {}".format(author_name))
            else:
                self.show_edit_book_menu(entry)

    def list_all_entries(self):
        self.notebook.list_authors()

    def list_books_for_author(self):
        author_name = input("Please enter the name of the author whose books you would like to see.")
        self.notebook.list_books_for_author(author_name)

    def delete_entry(self):
        author_name = input("Please enter the name of the author whose entry you want to delete.")
        if not author_name:
            print("No name entered.\n")
        else:
            deleted = self.notebook.delete_entry(author_name)
            if deleted:
                print("Entry for {} successfully deleted.\n".format(author_name))
            else:
                print("No entry for {}.\n".format(author_name))

    def quit(self):
        sys.exit(0)


if __name__ == '__main__':
    menu = Menu()
    menu.run()
