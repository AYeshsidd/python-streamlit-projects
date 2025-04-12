Library = [
{
    "name":"Nineteen Eighty-Four",
    "author":"George",
    "publication year":2004,
    "read-status": True,
    "price":"700$",
     "genre": "history"
    
}

,

{
    "name":"Adaptive markets",
    "author":"Andrew Lo",
    "publication year":2004,
    "read-status": True,
    "price":"1200$",
     "genre": "Finance"
}

,

{
    "name":"Game changer",
    "author":"Shahid Afridi",
    "publication year":2016,
    "read-status": True,
    "price":"1200$",
     "genre": "Cricket"
}

,

{
    "name":"Generative python",
    "author":"sir Zia",
    "publication year":2022,
    "read-status": True,
    "price":"300$",
     "genre": "programming"

}

,

{
    "name":"Learn Next-js-15",
    "author":"Ameen Alam",
    "publication year":2024,
    "read-status": True,
    "price":"400$",
     "genre": "programming frameworks"

}]

def display_Library():
    """
    This function displays the complete details of all books in the library with there keys and values.
    
    """
    
    print("\n📚 Your Personal Library 📚\n")
    for index, book in enumerate(Library, start=1):   #enum loops both, every dict and index
            print(f"📖 Book {index}:\n")
            print(f"🔹 Title:{book['name']}")
            print(f"   Author: {book['author']}")
            print(f"   Published in: {book['publication year']}")
            print(f"   Genre: {book['genre']}")
            print(f"   Price: {book['price']}")
            print(f"   Read-status: {book['read-status']} ")
            print("-" * 32)

 

def search_a_Book():
    """
    this function allows the user to search for a book by author name.

    first it takes an input from the user then compared it with the condition.
    the condition will search the author name in the library and then compare with the user's author name
    """
    search_author = input("Search a book by its Author name: ")
    found = False 
    
    for searching in Library:
        if searching["author"].lower()== search_author.lower():
            print(f"\n\t***📚 Book found!***\n")

            for key in searching:
             print(f"{key}: {searching[key]}")
    
            found = True
    if not found:
        print(f"🚫 Nothing by Author {search_author}. Please try searching with a different author name. ")

# print(search_a_Book.__doc__)
        

def Adding_a_Book():
   """
   From this function user can add any of the book in the library.
   first it takes input from the user about all the information of the book 
   and then add a book in the library and prints success msg in the end

   
   """
   print("\t*** Add a New Book*** ")
   add_Booktitle = input("Enter the book Title: ")
   add_authorName = input("Enter the author Name: ")
   add_publication = input("Enter the publication Year: ")
   add_Readstatus = input("Have you read this book? (yes/no):  ")
   print(True if add_Readstatus == "yes" else False if add_Readstatus == "no" else " ")

   new_book = {
        "name": add_Booktitle,
        "author": add_authorName,
        "publication year": add_publication,
        "read-status": add_Readstatus
        }
   
   Library.append(new_book)
   print(f"✅ The book '{add_Booktitle}' by {add_authorName} has been successfully added to your library.")

# Adding_a_Book()

def Remove_a_Book():
   prompt  = input("Enter the title of the book to remove: ").strip()
   found = False
  
   for finding_Title in Library:
      if finding_Title["name"].lower() == prompt.lower():
         Library.remove(finding_Title)
         print(f"🔴 Book '{finding_Title['name']}' has been Removed from libarary!")
         found = True
   
   if not found:
      print("❌ No book found with that title. Please check your input.")
   

   

   
def Main_menu():
   print("Welcome to the libarary management system 📗📕")
   print("What are you looking for ? ") 
   print("1. Search a Book")
   print("2. Add a New Book")
   print("3. Display all Books")
   print("4. Remove a Book")
   print("5. Exit")

   user_select = (input("please select an option "))
   if user_select == "1":
      (search_a_Book())
  
   elif user_select == "2": 
      print(Adding_a_Book())
   
   elif user_select == "3":
      print(display_Library())
    #    for books in Library:
    #        for key in books:
    #         print(f"{key}: {books[key]}")
  
   elif user_select == "4":
     print(Remove_a_Book())

   elif user_select == "5":
      print("\nExit!")
          

Main_menu()



