import json
import csv


#read file and parse Library
myLibrary = open('Library.json','r')
myData = myLibrary.read()
myLibrary.close()
obj = json.loads(myData)

#read file and parse Backup
myBackup = open('Backup.json','r')
myData2 = myBackup.read()
myBackup.close()
objBackup = json.loads(myData2)

# read file and parse Backup
loanAdmin = open('Loan Administration.json','r')
myData3 = loanAdmin.read()
loanAdmin.close()
objLaonAdmin = json.loads(myData3)




#The Class Diagram should at least cover classes such as Book, Author, BookItem (a
#paper copy of a book), Subscriber, Librarian, Person, Catalog, LoanAdministration, LoanItem.

class PublicLibrary:
    def __init__(self):
        self.catalog = Catalog()
        self.loanadministration = LoanAdministration()
 
class BackUp:

    def backUp(self):
        with open('Backup.json', 'w') as f:
            json.dump(obj, f, indent=len(obj[0]))
            f.close()
        
    def restore(self):
        with open('Library.json', 'w') as f:
            json.dump(objBackup, f, indent=len(obj[0]))
            f.close()


class LoanAdministration:

    def loanAdministration(self, lobb, value):
        global loancalc
        loancalc = 0
        if value == "loan":
            user = input("Type in your username: ")
            
            b = 0
            
            with open('Names.csv','r',encoding="UTF-8") as names_f:
                reader = csv.DictReader(names_f)
                for line in reader:
                    if user == line['Username']:
                        cat.searchFunction(lobb)
                        print("Available books: "+ str(obj[loancalc]['copies']))
                        inp = input("Are you sure you want to loan this book?\nType \"yes\" or \"no\": ")
                        if inp.lower() == "yes":
                            
                            if obj[loancalc]['copies'] <= 0:
                                print ("Sorry, this book is out of stock.")
                            else:
                                obj[loancalc]['copies']=obj[loancalc]['copies']-1
                                obj[loancalc]['Loaned']=obj[loancalc]['Loaned']+1
                                with open('Library.json', 'w') as f:
                                    json.dump(obj, f, indent=len(obj[0])+1)
                                    f.close()
                                    a=0
                                    c = False
                                    for _ in objLaonAdmin:
                                        if objLaonAdmin[a]['ISBN'] == obj[loancalc]['ISBN']:
                                            c = True
                                            d = a
                                        a+=1 
                                    if c == True:
                                        objLaonAdmin[d]['LOANEDTO'].append(user)
                                        
                                        with open('Loan Administration.json', 'w') as f:
                                            json.dump(objLaonAdmin, f, indent=len(objLaonAdmin[0]))
                                            f.close()
                                        
                                    else:
                                            objLaonAdmin.append({
                                            "ISBN"       : obj[loancalc]['ISBN'],
                                            "BOOKNAME"   : obj[loancalc]['title'],
                                            "AUTHOR"     : obj[loancalc]['author'],
                                            "LOANEDTO"   : [user]
                                                                                            
                                            })
                                            with open('Loan Administration.json', 'w') as f:
                                                json.dump(objLaonAdmin, f, indent=len(obj[0]))
                                                f.close()
                                            
                                            
                                print("You loaned this book!")
                                b=1

                if b == 0:
                    print ("This user doesn't exist.")
                
        else:
            user = input("Type in your username: ")
            
            g=False
            with open('Names.csv','r',encoding="UTF-8") as names_f:
                reader = csv.DictReader(names_f)
                for line in reader:
                    if user == line['Username']:
                        cat.searchFunction(lobb)
                                                
                        for e in range(len(objLaonAdmin)):
                            for f in range(len(objLaonAdmin[e]['LOANEDTO'])):
                                if str(objLaonAdmin[e]['LOANEDTO'][f]) == user:
                                    g=True
                                    temp1 = e
                                    temp2 = f
                                    print(temp1)
                                    print(temp2)

                        if g == True:
                            print("Available books: "+ str(obj[loancalc]['copies']))
                            inp = input("Are you sure you want to bring back this book?\nType \"yes\" or \"no\": ")
                            if inp.lower() == "yes":
                                obj[loancalc]['copies']=obj[loancalc]['copies']+1
                                obj[loancalc]['Loaned']=obj[loancalc]['Loaned']-1
                                with open('Library.json', 'w') as f:
                                    json.dump(obj, f, indent=len(obj[0])+1)
                                    f.close()
                                del objLaonAdmin[temp1]['LOANEDTO'][temp2]
                                with open('Loan Administration.json', 'w') as f:
                                    json.dump(objLaonAdmin, f, indent=len(objLaonAdmin[0])+1)
                                    f.close()
                                print("You brought back this book!")
                                b=1

                        else: print("This user never loaned this book.")
                 
                
    

class Catalog:

    def addBook(self, author, country, imageLink, language, link, pages, title, year, copies):

        obj.append({
        "author":author ,
        "country":country ,
        "imageLink":imageLink ,
        "language":language ,
        "link":link ,
        "pages":pages ,
        "title":title ,
        "year":year,
        "ISBN": obj[ -1 ]["ISBN"] + 1,
        "loaned": 0,
        "copies":copies
        
        })

        # write list to file
        with open('Library.json', 'w') as f:
            json.dump(obj, f, indent=len(obj[0]))
            f.close()

    def updateDictionary(self, category,item):
        a=0
        if item.isnumeric():
            item = int(item)
        
            
        for _ in obj:
            obj[a].update({category:item})


            with open('Library.json', 'w') as f:
                    json.dump(obj, f, indent = len(obj[0])+1)
                    f.close()
            a+=1

    def searchFunction(self, search):
        global loancalc
        a = 0

        searchList = []
        search = search.lower()
        for _ in obj:
            if search in obj[a]['author'].lower():
                searchList.append(obj[a])
            elif search in obj[a]['country'].lower():
                searchList.append(obj[a])
            elif search in obj[a]['imageLink'].lower():
                searchList.append(obj[a])
            elif search in obj[a]['language'].lower():
                searchList.append(obj[a])
            elif search in obj[a]['link'].lower():
                searchList.append(obj[a])
            elif search.isnumeric() and int(search) == obj[a]['pages']:
                searchList.append(obj[a])
            elif search in obj[a]['title'].lower():
                searchList.append(obj[a])
                loancalc = a
            elif search.isnumeric() and int(search) == obj[a]['year']:
                searchList.append(obj[a])
            elif search.isnumeric() and int(search) == obj[a]['ISBN']:
                searchList.append(obj[a])  
            a=a+1
        if searchList == []:
            return("Sorry, this title does not exist in our library.")
        else: return searchList


class Librarian:

    def checkBook(self, check):
        global loancalc
        a = 0

        searchList = []
        check = check.lower()
        for _ in objLaonAdmin:
            if check.isnumeric() and int(check) == objLaonAdmin[a]['ISBN']:
                searchList.append(objLaonAdmin[a])
            elif check in objLaonAdmin[a]['BOOKNAME'].lower():
                searchList.append(objLaonAdmin[a])

            a=a+1
        if searchList == []:
            return("Sorry, this title has never been loaned out.")
        else: return searchList


class Subscriber:

    def addCustomer(self, Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, Username, TelephoneNumber):
        file = open("Names.csv")
        numline = len(file.readlines())
        file.close()
        with open('Names.csv', 'a', newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([numline,Gender,NameSet,GivenName,Surname,StreetAddress,ZipCode,City,EmailAddress, Username, TelephoneNumber])


cat = Catalog()
lib = Librarian()
sub = Subscriber()
loan = LoanAdministration()
backup = BackUp()

program = ""
while program.lower() != "quit":

    with open('Names.csv','r',encoding="UTF-8") as names_f:
        reader = csv.DictReader(names_f)
        print (reader)
    
    program = input("\nHello! Welcome to the Library Application. Type \"quit\" if you want to quit the program.\n\nType the number you are:\n\n1. Subscriber\n2. Librarian\n3. publishing company\n")
    
    if program == "1" or program == "3":
        program = input("What would you like to do?\n1. Search for a book and availability\n2. Create an account\n3. Loan a book\n4. Bring back a book\n" )
        if program.lower() == "search book" or program == "1":
            search = input("Search for a book: ") 
            resultFound = cat.searchFunction(search)
            print (resultFound)

        elif program.lower() == "create account" or program == "2":
            Gender = input("Gender: ")
            if Gender == "":
                Gender = "Unknown"
            NameSet = input("Nameset: ")
            if NameSet == "":
                NameSet = "Unknown"
            GivenName = input("GivenName: ")
            if GivenName == "":
                GivenName = "Unknown"
            Surname = input("Surname: ")
            if Surname == "":
                Surname = "Unknown"
            StreetAddress = input("StreetAddress: ")
            if StreetAddress == "":
                StreetAddress = ""
            ZipCode = input("ZipCode: ")
            if ZipCode == "":
                ZipCode = "unknown"
            City = input("City: ")
            if City == "":
                CIty = "Unknown"
            EmailAddress = input("EmailAddress: ")
            if EmailAddress == "":
                EmailAddress = "unknown"
            UserName = input("Username: ")
            if UserName == "":
                UserName = "unknown"
            TelephoneNumber = input("telephonenumber: ")
            if TelephoneNumber == "":
                TelephoneNumber = "unknown"

            sub.addCustomer(Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, UserName, TelephoneNumber)

        elif program.lower() == "loan book" or program.lower() == "bring back book" or program == "3" or program == "4":
            if program.lower() == "loan book" or program == "3":
                lobb = input("Enter the book you want to loan: ")
                loan.loanAdministration(lobb, "loan")
            elif program.lower() == "bring back book" or program == "4":
                lobb = input("Enter the book you want to bring back: ")
                loan.loanAdministration(lobb, "bringback")

    elif program == "2":
        libpass = input("Type password to enter:\n")
        if libpass == "1234":
            program = input("What would you like to do?\n1. Search for a book and availability\n2. Create a customer account\n3. Loan a book\n4. Bring back a book\n5. Add a book\n6. Update dictionary\n7. Make a Backup\n8. Restore Backup\n9. Check a book laon\n")

            if program.lower() == "search book" or program == "1":
                search = input("Search Book: ") 
                resultFound = cat.searchFunction(search)
                print (resultFound)

            elif program.lower() == "add book" or program == "5":
                author = input("Author: ")
                if author == "":
                    author = "Unknown"
                country = input("Country: ")
                if country == "":
                    country = "Unknown"
                imageLink = input("Image Link: ")
                if imageLink == "":
                    imageLink = "Unknown"
                language = input("Language: ")
                if language == "":
                    language = "Unknown"
                link = input("Link: ")
                if link == "":
                    link = "Unknown"
                pages = input("Pages: ")
                if pages == "":
                    pages = 0
                title = input("Book Title: ")
                if title == "":
                    title = "Unknown"
                year = input("Year: ")
                if year == "":
                    year = 0
                copies = input("Copies: ")
                if copies == "":
                    copies = 0
            
                cat.addBook(author, country, imageLink, language, link, int(pages), title, int(year), int(copies))
                print("Your book has been added to the library.")
            elif program.lower() == "create customer" or program == "2":
                Gender = input("Gender: ")
                if Gender == "":
                    Gender = "Unknown"
                NameSet = input("Nameset: ")
                if NameSet == "":
                    NameSet = "Unknown"
                GivenName = input("GivenName: ")
                if GivenName == "":
                    GivenName = "Unknown"
                Surname = input("Surname: ")
                if Surname == "":
                    Surname = "Unknown"
                StreetAddress = input("StreetAddress: ")
                if StreetAddress == "":
                    StreetAddress = ""
                ZipCode = input("ZipCode: ")
                if ZipCode == "":
                    ZipCode = "unknown"
                City = input("City: ")
                if City == "":
                    CIty = "Unknown"
                EmailAddress = input("EmailAddress: ")
                if EmailAddress == "":
                    EmailAddress = "unknown"
                UserName = input("Username: ")
                if UserName == "":
                    UserName = "unknown"
                TelephoneNumber = input("telephonenumber: ")
                if TelephoneNumber == "":
                    TelephoneNumber = "unknown"

                sub.addCustomer(Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, UserName, TelephoneNumber)

            elif program.lower() == "update dictionary" or program == "6":
                category = input("Type the category: ")
                if category =="":
                    category = "Unknown"
                item = input("Type in the item of the category: ")
                if item == "":
                    item = "Unknown"
                cat.updateDictionary(category, item)
            
            elif program.lower() == "loan book" or program.lower() == "bring back book" or program == "3" or program == "4":
                if program.lower() == "loan book" or program == "3":
                    lobb = input("Enter the book you want to loan: ")
                    loan.loanAdministration(lobb, "loan")
                elif program.lower() == "bring back book" or program == "4":
                    lobb = input("Enter the book you want to bring back: ")
                    loan.loanAdministration(lobb, "bringback")
            elif program.lower() == "backup" or program == "7":
                passw = input("Type the password to enter: ")
                if passw == "1234":
                    warning = input("Are you sure you want to backup the Library? This will erease the previous backup.\n Type \"Yes\" or \"No\".\n")
                    if warning.lower() == "yes":
                        backup.backUp()
                    print("Backup succesful.")
                else: print("Wrong password")
            elif program.lower() == "restore" or program == "8":
                passw = input("Type the password to enter: ")
                if passw == "1234":
                    warning2 = input("Are you sure you want to restore the backup? This can not be undone.\n Type \"Yes\" or \"No\".\n")
                    if warning2.lower() == "yes":
                        backup.restore()
                    print("Restore succesful.")
            elif program.lower == "check book" or program == "9":
                check = input("Search on ISBN or Book name:\n") 
                resultFound = lib.checkBook(check)
                print (resultFound)
            elif program.lower() == "quit":
                print("You quit the program.")
            else: print("Sorry, this isn't a valid command.")
        else:
            print("Wrong password.")
