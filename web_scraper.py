from bs4 import BeautifulSoup
import requests


class WebScraper:

    def __init__(self, url):

        # url of the page to scrape data
        self.url = url
        # count the total number of ads
        self.total = 0
        # Contains lists for the name, price, url and image of all the items
        self.all_listing_data = []


    # fetch the text of the page
    def _fetch_page(self, url):

        try: 
            response = requests.get(url)
            # raise and exception for 4xx and 5xx exception codes
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the page: {e}")
    

    # parse and return the html data of the page using BeautifulSoup
    def _parse_data(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')
        return soup
    

    # extracts the listings from the parsed data and adds them to self.all_listing_data
    def _extract_data(self, soup):

        # find and return all the divs in the page containing the class search-item (ads)
        listings = soup.find_all('div', class_='search-item')

        # extract data from each div/ad found
        for listing in listings:

            # get the title for the listing/ad
            title = listing.find('div', class_='title').text.strip()

            # get the price for the listing/ad
            price = listing.find('div', class_='price').text.strip()

            # get the url for the listing/ad
            url = 'https://www.kijiji.ca' + listing['data-vip-url']

            # get the thumbnail for the listing/ad
            thumbnail_attr = listing.find(attrs={'data-srcset': True})

            # returns 'No Image' for the thumbnail if it doesn't exist
            thumbnail = thumbnail_attr['data-srcset'] if thumbnail_attr else 'No Image'
            
            # make a list containing the name, price and url of the new ad
            new_item = [title, price, url, thumbnail]

            # appends the list with a new item if it already doesn't exist
            if new_item not in self.all_listing_data:
                self.all_listing_data.append(new_item)
                self.total += 1


    # finds the url of the next page
    def _next_page(self, soup):

        # finds the button that contains the next page href
        next_page = soup.find('a', title='Next')

        # if the 'Next' button does not exist, returns None, else returns the url of the next page
        if not next_page:
            return None
        else:
            next_page_url = f'https://kijiji.ca{next_page["href"]}'
            return next_page_url
    

    # go through all the pages of the query and extract listing data from each page
    def scrape_all_pages(self):
        page_url = self.url
        page_number = 1

        # continue extracting data from pages until the next page url becomes None (reach the last page)
        while True:
            print(f'Scraping page: {page_number}')
            
            # fetch, parse and extract the data from each page, and save it to self.all_listing_data
            page_content = self._fetch_page(page_url)
            soup = self._parse_data(page_content)
            self._extract_data(soup)
            page_url = self._next_page(soup)

            # break the loop if next page url is None (i.e. you reach the last page)
            if not page_url:
                break
            
            page_number += 1

        # return all the extracted ads from all the pages
        return self.all_listing_data