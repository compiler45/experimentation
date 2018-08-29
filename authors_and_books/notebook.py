next_id = 1


class Entry:
    def __init__(self, author_name):
        self.author_name = author_name
        self.books = []
        global next_id
        self.id = next_id
        self.num_books = 0

        next_id += 1

    def add_book(self, book_name):
        if book_name not in self.books:
            self.books.append(book_name)
            self.num_books += 1
            return True

        return False

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            return True

        return False

    def edit_book(self, old_book_name, new_book_name):
        if old_book_name in self.books:
            index = self.books.index(old_book_name)
            self.books[index] = new_book_name
            return True

        return False


class Notebook:
    def __init__(self):
        self.num_entries = 0
        self.entries = []

    def add_entry(self, author_name):
        #  All entries must have unique authors
        entry = self.get_entry_for_author(author_name)
        if not entry:
            new_entry = Entry(author_name=author_name)
            self.entries.append(new_entry)
            self.num_entries += 1
            return True

        return False

    def delete_entry(self, author_name):
        entry = self.get_entry_for_author(author_name)
        if entry:
            self.entries.remove(entry)
            self.num_entries -= 1
            return True

        return False

    def get_entry_for_author(self, author_name):
        for entry in self.entries:
            if entry.author_name == author_name:
                return entry

        return None

    def list_authors(self):
        print("All available authors: \n")
        for entry in self.entries:
            print("{}\n".format(entry.author_name))

    def list_books_for_author(self, author_name):
        entry = self.get_entry_for_author(author_name)
        if not entry:
            print("Sorry, there is no entry for {}.".format(author_name))
        else:
            print("Books by {}:".format(author_name))
            for book in entry.books:
                print("{}".format(book))

    def give_num_entries(self):
        print("There {are} {number} author{s} in this little notebook!".format(are=('is' if self.num_entries == 1
                                                                               else 'are'),
                                                                               number=self.num_entries,
                                                                               s=('' if self.num_entries == 1
                                                                               else 's')))
