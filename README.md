# Book Downloader

This Python script allows you to search for and download free open source PDF copies of books.

## How to Use

1. Install the `requests` module by running `pip install requests` in the command line.

2. Run the script using a Python interpreter.

3. Enter the title and author of the book when prompted.

4. The script will create a new directory with the author's name (replacing spaces with underscores) and download any available PDF copies of the book to that directory, using the book's title as the filename.

## Notes

- This script uses the Google Books API and the Open Library API to search for available copies of the book.

- If multiple ISBNs are found for the book, the script will use the first one in the list.

- If multiple formats are available for the book, the script will download the PDF version if it is available.

- If no PDF copies are available, the script will not download anything.

- If a book has multiple authors, enter the name of the first listed author when prompted.

- If the book title or author name contains spaces, use quotes (e.g., "The Great Gatsby" and "F. Scott Fitzgerald").

## How to Set Up a Google Books API Key

1. Go to the [Google Developers Console](https://console.developers.google.com/).

2. Create a new project.

3. In the sidebar, click on "APIs & Services" and then "Dashboard".

4. Click on "+ ENABLE APIS AND SERVICES" and search for "Google Books API". Select it and click on "Enable".

5. In the sidebar, click on "APIs & Services" and then "Credentials".

6. Click on "+ CREATE CREDENTIALS" and select "API key".

7. Copy the API key and use it in the script where it says `GOOGLE_BOOKS_API_KEY`.

## How to Set Up an Open Library API Key

1. Go to the [Open Library Developers](https://openlibrary.org/dev/docs/api/getting_started) page.

2. Create an account and obtain an API key.

3. Use the API key in the script where it says `OPEN_LIBRARY_API_KEY`.
