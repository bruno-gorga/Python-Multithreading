import requests
import time
import csv
import random
import regex as re
import concurrent.futures

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

MAX_THREADS = 10

def extract_movie_details(movie_link):
    response = BeautifulSoup(requests.get(movie_link, headers=headers).content, 'html.parser')
    movie_soup = response

    if movie_soup is not None:
        title = None 
        data = None 


        movie_data = movie_soup.find('div', attrs={'class':'sc-e226b0e3-3 jJsEuz'})
        if movie_data is not None: 
            title = movie_data.find('h1').get_text()
            date = movie_data.find('a', attrs={'class':'ipc-link ipc-link--baseAlt ipc-link--inherit-color'}).get_text()
            rating = movie_data.find('span', attrs={'class': 'sc-bde20123-1 iZlgcd'}).get_text() if movie_data.find('span', attrs={'class': 'sc-bde20123-1 iZlgcd'}) else None
            

            with open('./movies.csv', mode='a') as f:
              movie_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
              if all([title, date, rating]):
                print(title, date, rating)
                movie_writer.writerow([title, date, rating])
                


def extract_movies(soup):
    movies_table = soup.find_all('a', href=True)
    titles = re.findall(r'/title/\w+', str(movies_table))
    movie_links = ['https://imdb.com' + title for title in titles]
    for i in range(len(movie_links)//2):
        if movie_links[i] == movie_links[i+1]:
            movie_links.remove(movie_links[i+1])

    threads = min(MAX_THREADS, len(movie_links))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(extract_movie_details, movie_links)


    


def main():
    start_time = time.time()

    # IMDB Most Popular Movies - 100 movies
    popular_movies_url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
    response = requests.get(popular_movies_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Main function to extract the 100 movies from IMDB Most Popular Movies
    extract_movies(soup)

    end_time = time.time()
    print("Total time taken: ", end_time - start_time)


if __name__ == '__main__':
    main()
