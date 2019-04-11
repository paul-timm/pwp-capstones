class TomeRaterHelp():
    def Print(self):
        print('''User Class Fuctions:\n
        \n
        get_email returns the user's email\n
        \n
        change_email changes the user's email\n
        \n
        read_book adds a book and a rating to the user's book dictionary\n
        \n
        get_average_rating calculates the average rating doled out by the user\n
        \n
        \n
        Book Class Functions:\n
        \n
        get_title returns the books title\n
        \n
        get_isbn return the book's isbn\n
        \n
        set_isbn changes the book's isbn\n
        \n
        add_rating allows a user to rate a book\n
        \n
        get_average_rating calculates the average rating for that book\n
        \n
        \n
        TomeRater Class Functions:\n
        \n
        create_book creates a book from a title and isbn\n
        \n
        create_novel creates a novel requireing author, title, and isbn\n
        \n
        create_non_fiction creates a non_fiction requiring title, isbn,subject, and level\n
        \n
        add_book_to_user appends a book to a user's book/rating dictionary and updates how the total number of users that read that book\n
        \n
        add_user creates a user\n
        \n
        print_catalog prints all the books in the tome\n
        \n
        print_users prints all the users in the tome\n
        \n
        most_read_book calculates and returns the most read book\n
        \n
        highest_rated_book compares the average ratings of all the books\n
        \n
        most_positive_user compares the average ratings of all the users\n
        \n
        n_most_read_books compares how often the books have been read\n
        \n
        menus allows the user to do some operations interactively\n
        \n
              ''')
