# Python Multithreading exercise
This project's aim is to show the difference in performance between using just one thread and using multiple threads to execute the same instructions in Python language. In this case it is a web scraping of the 100 Most Popular Movies on IMDB.

GIL (Global Interpreter Lock) is a particular CPython implementation. It is a mutex that allows just one thread to take control of the Python interpreter, so that only one thread can be in a state of execution at a time. Nevertheless, for tasks that involve Input/Output operations (I/O-bound tasks), like network requests, the GIL is released to be used by other threads during the web request a specific thread is executing. In that way, even with GIL in action, other threads can be used in an efficient manner to improve performance of the I/O-bound tasks.

Here we use BeautifulSoup library to help us with the scraping and concurrent.futures to allow the setup of the multithreading execution of the code.

We have two main functions: one responsible for extracting the link of each of the IMDB Top 100 Movies individual pages (def extract_movies (soup)) and the other for extracting the respective data of said movies, namely name, year of release and rate.

Time library is used to measure the time needed to execute the instructions and generate a csv file with the scraped data.

In addition, for comparison purposes, there is also a code for the same instructions but without the multithreading feature implemented. As far as testing goes, it is visible that multithreading played a big role in improving the performance of the process.

