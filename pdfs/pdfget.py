##################################
#
# Script to scrape PDF documents
#   from https://medlineplus.gov/languages/somali.html
#
#              by
#
#       Code Codert
#
##################################

# packages
import requests
from bs4 import BeautifulSoup
from urllib.request import unquote

# target URL
url = 'https://medlineplus.gov/languages/somali.html'

# make HTTP GET request to the target URL
print('HTTP GET: %s', url)
response = requests.get(url)

# parse content
content = BeautifulSoup(response.text, 'lxml')

# extract URLs referencing PDF documents
all_urls = content.find_all('a')

# loop over all URLs
for url in all_urls:
    # try URLs containing 'href' attribute
    try:
        # pick up only those URLs containing 'pdf'
        # within 'href' attribute
        if 'pdf' in url['href']:
            # init PDF url
            pdf_url = ''

            # append base URL if no 'https' available in URL
            if 'https' not in url['href']:
                pdf_url = 'https://medlineplus.gov/languages/somali.html' + url['href']

            # otherwise use bare URL
            else:
                pdf_url = url['href']

            # make HTTP GET request to fetch PDF bytes
            print('HTTP GET: %s', pdf_url)
            pdf_response = requests.get(pdf_url)

            # extract  PDF file name
            filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')

            # write PDF to local file
            with open(filename, 'wb') as f:
                # write PDF to local file
                f.write(pdf_response.content)



    # skip all the other URLs
    except:
        pass