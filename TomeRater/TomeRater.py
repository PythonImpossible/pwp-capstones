class User(object):
    name = ""
    email = ""
    books = {}
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email(self):
        return self.email

    def change_email(self, address):
    # check if the new email is different from current email
        if address == self.email:
            print("Email not changed")
        else:
            self.email = address
            print("Email updated")

    def __repr__(self):
    # creates a string to be used when printing object
        rep_string = "User " + self.name + ", email: " + self.email
        return rep_string

    def __eq__(self, other_user):
    # checks if other user has the same name and email
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        if (rating):
            self.books[book] = rating
        else:
            self.books[book] = None

    def get_average_rating(self):
        sum = 0
        count = 0
        
        for item in self.books.values():
            sum += item
            count+=1
        if (count > 0):
            return sum / count
        else:
            return 0

class Book(object):
    title = ""
    isbn = 0
    ratings = []

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        if isbn == self.isbn:
            print ("ISBN not changed")
        else:
            self.isbn = isbn
            print("ISBN updated")

    def add_rating(self, rating):
        if rating:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def get_average_rating(self):
        sum = 0
        count = 0
        for item in self.ratings:
            sum += item
            count+=1
        if count > 0:
            return sum / count
        else:
            return 0

class Fiction(Book):
    author = ""
    
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        rep_string = self.title + " by " + self.author
        return rep_string

class Non_Fiction(Book):
    subject = ""
    level = ""
    
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        rep_string = self.title + " a " + self.level + " manual on " + self.subject
        return rep_string

class TomeRater():

    def __init__(self):
        self.user = {}
        self.books = {}
        self.isbn = {}

 #   def __repr__(self):
 #       user_list = []
 #       book_list = []

 #       for users in self.user.values():
 #           user_list.append(users)
 #       for book in self.books:
 #           book_list.append(book.title)
 #       return (user_list, book_list)

    def create_book(self, title, isbn):
        dup_isbn = False

        for book in self.isbn:
            if book.title != title and book.isbn == isbn:
                print("Error: Duplicate ISBN " + str(isbn) + " found! ISBN belongs to " + book.title)
                dup_isbn = True
                break
            else:
                continue

        if dup_isbn == True:
            return None
        else:
            new_book = Book(title, isbn)
            self.isbn[new_book] = isbn
            return new_book        

    def create_novel(self, title, author, isbn):
        dup_isbn = False

        for book in self.isbn:
            if book.title != title and book.isbn == isbn:
                print("Error: Duplicate ISBN " + str(isbn) + " found! ISBN belongs to " + book.title)
                dup_isbn = True
                break
            else:
                continue

        if dup_isbn == True:
            return None
        else:
            new_novel = Fiction(title, isbn , author)
            self.isbn[new_novel] = isbn
            return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        dup_isbn = False

        for book in self.isbn:
            if book.title != title and book.isbn == isbn:
                print("Error: Duplicate ISBN " + str(isbn) + " found! ISBN belongs to " + book.title)
                dup_isbn = True
                break
            else:
                continue

        if dup_isbn == True:
            return None
        else:
            new_non_fiction = Non_Fiction(title, isbn, subject, level)
            self.isbn[new_non_fiction] = isbn
            return new_non_fiction

    def add_book_to_user(self, book,email,rating=None):
        found_user = False
        local_user = None
        for user_email in self.user:
            if user_email == email:
                found_user = True
                break
        if found_user == False:
            print("No user with email " + email + "!")
        else:
            local_user = self.user[email]
            local_user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self,name,email,user_books=None):
        if '@' in email:
            if ".com" in email or ".edu" in email or ".org" in email:
                if email in self.user:
                    print("User already exists! User not added.")
                else:
                    local_user = User(name,email)
                    self.user[email] = local_user
                    if user_books:
                        for book in user_books:
                            self.add_book_to_user(book, email)
            else:
                print("Invalid e-mail format (unexpected domain)! User not added.")
        else:
            print("Invalid e-mail format (missing '@')! User not added.")

    def print_catalog(self):
        for book in self.books:
            print(book.title)

    def print_users(self):
        for email in self.user:
            print(self.user[email])

    def get_most_read_book(self):
        max_read = -1
        most_read = None
        
        for book in self.books:
            if self.books[book] > max_read:
                max_read = self.books[book]
                most_read = book
            else:
                continue
        if max_read != -1:
            return most_read
        else:
            return None

    def highest_rated_book(self):
        max_rating = -1
        highest_rated = ""

        for book in self.books:
            if book.get_average_rating() > max_rating:
                max_rating = book.get_average_rating()
                highest_rated = book.title
            else:
                continue
        if max_rating != -1:
            return highest_rated
        else:
            return None

    def most_positive_user(self):
        max_rating = -1
        positive_user = None

        for user in self.user.values():
            if user.get_average_rating() > max_rating:
                max_rating = user.get_average_rating()
                positive_user = user
            else:
                continue
        if max_rating != -1:
            return positive_user
        else:
            return None
