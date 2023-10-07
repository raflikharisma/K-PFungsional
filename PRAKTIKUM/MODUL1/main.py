
db_book = {}
db_loaned = {}

def adminListMenu():
    print('\n')
    print('Welcome admin!!')
    print('What you want to do?')
    print('1. Add new book')
    print('2. Delete book')
    print('3. Show Booklist')
    print('4. Exit')

def userListMenu():
    print('\n')
    print('Welcome student!')
    print('What you want to do?')
    print('1. Loaning book')
    print('2. Return book')
    print('3. Show Booklist')
    print('4. Exit')
     

def bookList():
    if not db_book:
        print('Library Empty')
    else:
        print('\n')
        print('List Buku')
        for outerDict, innerDict in db_book.items():
            print('\n')
            print('Kode Buku : ',outerDict)
            for key, values in innerDict.items():
                print(key," : ", values)


def adminAddBook():
    book_id = input('Input book ID : ')
    if book_id in db_book:
        print('Code not available')
        adminAddBook()
    else:          
        book_title = input('Input title : ')
        book_author = input('Input book author : ')
        book_pages = input('Input book pages : ')
        
        inner_dict = {
            'Book Title': book_title,
            'Book Author': book_author,
            'Pages' : book_pages
        }
    
        db_book[book_id] = inner_dict
        print('successfully added book : "{}", Book ID "{}"'.format(book_author, book_id))
        choice = input('You want to add more book? (y/n): ')
        
        if choice == 'y' or choice == 'Y':
            adminAddBook()
        else:
            adminMenu()

def adminDeleteBook():
    book_id = input('Input book ID : ')
    if book_id not in db_book:
        print('Code error')
    elif book_id in db_book:
        choice = input('You sure want to delete this book? (y/n): ')
        if choice == 'y' or choice == 'Y':
            print(f'Book "{book_id}" Successfully Deleted')
            del db_book[book_id]
            delChoice = input('Go back to main menu? (y/n): ')
            if delChoice == 'y' or delChoice == 'Y':
                adminMenu()
            else:
                adminDeleteBook()
    else:
        print('Empty')
        
        
    bookList()    
       
                
def loaningBook():
    book_id = input('Input book ID you want to loan : ')
    if not db_book:
        print('Library Empty')
        userMenu()
    elif book_id not in db_book:
        print('There is no result for {}', format(book_id))
        loaningBook()
    elif book_id in db_book:
        print(f'Successfully Loaned The Book, Code : {book_id}')
        db_loaned[book_id] = db_book[book_id]
        del db_book[book_id]
        choice = input('Go back to main menu? (y/n): ')
        if choice == 'y' or choice == 'Y':
            userMenu()
        else:
            loaningBook()    

def returningBook():
    book_id = input('Input book ID for returning')
    if book_id in db_loaned:
        print(f"The book id you loaned : {book_id}, Title : {db_loaned[book_id]['Book Title']}, author : {db_loaned[book_id]['Book Author']}. Successfully Returned ")
        db_book[book_id] = db_loaned[book_id]
        del db_loaned[book_id]
        choose = input('go back to main menu? (y/n)')
        if choose == 'y' or choose == 'Y':
            userMenu()
        else:
            returningBook()
    else:
        print('There is no result for {}', format(book_id))
        returningBook()
        


def adminMenu():
    adminListMenu()
    choose = input('Input your choose : ')
    if choose == '1':
        adminAddBook()
    elif choose == '2':
        adminDeleteBook()
    elif choose == '3':
        bookList()
        adminMenu()   
    elif choose == '4':
        main()     
        
def userMenu():
    userListMenu()
    choose = input('Input your choose : ')
    if choose == '1':
        bookList()  
        loaningBook()
    elif choose == '2':
        returningBook()
    elif choose == '3':
        bookList()   
        userMenu()
    elif choose == '4':
        main()    
        
        
def main():
   print('Welcome coy') 
   print('1. Login as admin')
   print('2. Login as student')
   print('3. Exit') 
   choose = input('Choose Your Input : ')
   if choose == '1':
       adminMenu()
   elif choose == '2':
       userMenu()
   else: 
       exit() 


if __name__ == "__main__":
    main()

















