from TomeRaterHelp import *
Tome_Help=TomeRaterHelp()

class User(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email=address
        print("your email adress is now {}".format(self.email))

    def __repr__(self):
        return "User = {}, email = {}, books read = {}".format(self.name,self.email,self.books)

    def __eq__(self, other_user):
        if self.name==other_user.name and self.email==other_user.email:
            other_user=self
            print("the users are the same")
        else:
            print("the users are not the same")

    def read_book(self,book,rating=None):
        self.books[book]=rating

    def get_average_rating(self):
        total=0
        count=0
        for key in self.books:
            if self.books[key]!=None:
                total+=self.books[key]
                count+=1
        average_rating=total/count
        return average_rating
    



class Book(object):
    def __init__(self,title,isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self,new_isbn):
        self.isbn=new_isbn
        print("The books isbn number has been updated to {}".format(self.isbn))
        
    def add_rating(self,rating):
        if rating in [0,1,2,3,4,5]:
            self.ratings.append(rating)
            print("Rating added")
        else:
            print("Invalid Rating")

    def __eq__(self,other_book):
        if self.title==other_book.title and self.isbn==other_book.isbn:
            other_book=self
            print("The books are the same")
        else:
            print("The books are not the same")
            
    def get_average_rating(self):
        total=0
        for rating in self.ratings:
            total+=rating
        average_rating=total/len(self.ratings)
        return average_rating
    
    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "This Book is {}".format(self.title)

    
class Fiction(Book):
    def __init__(self,title,isbn,author):
        Book.__init__(self,title,isbn)
        self.author=author
        
    def get_author(self,author):
        return self.author
    
    def __repr__(self):
        return "This Fiction Book is {} by {}".format(self.title,self.author)



class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn):
        Book.__init__(self,title,isbn)
        self.subject=subject
        self.level=level
        
    def get_subject(self,subject):
        return self.subject
    
    def get_level(self,level):
        return self.level
    
    def __repr__(self):
        return "This Non-Fiction Book is {}, a {} manual on {}".format(self.title,self.level,self.subject)

    
    
    
class TomeRater():
    def __init__(self):
        self.users={}
        self.books={}
        
    def create_book(self,title,isbn):
        return Book(title,isbn)
    
    def create_novel(self,title,author,isbn):
        return Fiction(title,author,isbn)
    
    def create_non_fiction(self,title,subject,level,isbn):
        return Non_Fiction(title,subject,level,isbn)
    
    def add_book_to_user(self,book,email,rating=None):
        if book in self.books:
            print("{} already in Tome".format(book))
            self.books[book]=self.books[book]+1
        else:
            self.books[book]=1
        if self.users[email] != None:
            self.users[email].read_book(book,rating)
            book.add_rating(rating)
        else:
            print("no user with email {}!".format(email))
            
    def add_user(self,name,email,user_books=None):
        new=User(name,email)
        self.users[email]=new
        if user_books != None:
            for i in user_books:
                self.add_book_to_user(i,email)
                
    def print_catalog(self):
        keys = list(self.books.keys())
        for i in keys:
            print(i)
            
    def print_users(self):
        for key in self.users:
            print(self.users[key])
            
    def most_read_book(self):
        count=0
        for book in self.books:
            if self.books[book]>count:
                count=self.books[book]
                most_read=book
        return most_read
    
    def highest_rated_book(self):
        highest_rating=0
        keys = list(self.books.keys())
        for i in keys:
            if i.get_average_rating()>highest_rating:
                highest_rating=i.get_average_rating()
                high_rated_book=i
        return high_rated_book
    
    def most_positive_user(self):
        positive_rating=0
        for key in self.users:
            if self.users[key].get_average_rating()!=None:
                if self.users[key].get_average_rating()>positive_rating:
                    positive_rating=self.users[key].get_average_rating()
                    positive_user=self.users[key]
        return positive_user

    def n_most_read_books(self,n):
        booklist=[]
        while len(booklist)<n:
            count=0
            for book in self.books:
                if self.books[book]>=count and (book not in booklist):
                    count=self.books[book]
                    most_read=book
            booklist.append(most_read)
        return booklist

    def menus(self):
        boolean=True
        while boolean:
            menu=input('''This is the main_menu, enter 'e' to exit menu, enter 'b' for book_menu, enter 'h' for help on TomeRater capabilities''')
            if menu=='b':
                self.book_menu()
            elif menu=='h':
                Tome_Help.Print()
            elif menu=='e':
                print('menu exited')
                boolean=False

    def delete_book(self,book_to_delete):
        keys = list(self.books.keys())
        title_key_dict={}
        special_key=None
        for key in keys:
            title_key_dict[key.get_title()]=key
        print title_key_dict
        print(title_key_dict[book_to_delete])
        del self.books[title_key_dict[book_to_delete]]
        print("{} was deleted".format(book_to_delete))
        print("The updated catalog is...\n")
        self.print_catalog()

    def book_menu(self):
        book_action=input('''This is the book_menu, enter 'c' to create a book, 'd' to delete a book, 'm' for main_menu''')
        if book_action=='c':
            title=input('input a title')
            isbn=input('input an isbn')
            email=input('input your existing user email')
            newbie=self.create_book(title,isbn)
            self.add_book_to_user(newbie,email,None)
            print("The updated catalog is...\n")
            self.print_catalog()
        elif book_action=='d':
            book_to_delete=input('what title do you want to delete?')
            self.delete_book(book_to_delete)
        elif book_action=='m':
            self.menus()
        return




################################    























