import os
import requests

# Get user input for directory and book title and author
save_dir = input("Enter the directory to save the book in: ")
book_title = input("Enter the title of the book: ")
book_author = input("Enter the name of the author: ")

# Create a new directory with the author's name
author_dir = book_author.replace(" ", "_")
if not os.path.exists(os.path.join(save_dir, author_dir)):
    os.mkdir(os.path.join(save_dir, author_dir))

# Search for the book using the Google Books API
google_books_url = "https://www.googleapis.com/books/v1/volumes?q=intitle:{}+inauthor:{}&maxResults=1".format(book_title, book_author)
response = requests.get(google_books_url)
if response.status_code == 200:
    json_data = response.json()
    if json_data["totalItems"] > 0:
        book_info = json_data["items"][0]["volumeInfo"]
        isbn_list = book_info.get("industryIdentifiers")
        if isbn_list is not None:
            isbn_list = [isbn["identifier"] for isbn in isbn_list]

            # Search for available copies of the book using the Open Library API
            for isbn in isbn_list:
                open_library_url = "https://openlibrary.org/api/books?bibkeys=ISBN:{}&format=json&jscmd=data".format(isbn)
                response = requests.get(open_library_url)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data:
                        book_info = json_data["ISBN:{}".format(isbn)]
                        formats = book_info.get("formats")
                        if formats is not None:
                            pdf_url = formats.get("pdf")
                            if pdf_url is not None:
                                # Download the PDF and save it to the author's directory
                                pdf_response = requests.get(pdf_url)
                                pdf_path = os.path.join(save_dir, author_dir, "{}.pdf".format(book_title))
                                with open(pdf_path, "wb") as f:
                                    f.write(pdf_response.content)
                                print("Downloaded {} to {}".format(book_title, author_dir))
                                break
        else:
            print("No ISBN found for the book.")
    else:
        print("No results found for the book.")
else:
    print("Error searching for the book.")
