# # import requests
# # from bs4 import BeautifulSoup
# #
# # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
# # url = 'https://qaamuus.net/qaamuus/'
# # r = requests.get(url, headers=headers)
# # soup = BeautifulSoup(r.text, 'html.parser')
# #
# # questions = soup.find_all('div', {'class': 'post-content box mark-links entry-content'})
# #
# # print(questions)
# ########################
#
#
#
# # # Import the necessary libraries
# # from bs4 import BeautifulSoup
# # import requests
# #
# # # Make a GET request to the website
# # r = requests.get("https://qaamuus.net/qaamuus/")
# #
# # # Parse the HTML content of the page
# # soup = BeautifulSoup(r.content, "html.parser")
# #
# # # Find the div with the class "post-content"
# # post_div = soup.find("div", {"class": "post-content"})
# #
# # # Extract the text from the div and remove the HTML tags
# # post_text = post_div.get_text()
# #
# # # Write the text to a file
# # with open("scraped_data.txt", "w") as file:
# #     file.write(post_text)
#
#
# # Import the necessary libraries
# from bs4 import BeautifulSoup
# import requests
#
# # Set the base URL of the website
# base_url = "https://qaamuus.net/qaamuus/?sortby=&rowstart="
#
# # Set the maximum number of pages to scrape
# max_pages = 1584
#
# # Loop through the pages
# for i in range(0, max_pages):
#     # Calculate the URL of the current page by adding the page number multiplied by 30 to the base URL
#     url = base_url + str(i * 30)
#
#     # Make a GET request to the website
#     r = requests.get(url)
#
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(r.content, "html.parser")
#
#     # Find the div with the class "post-content"
#     post_div = soup.find("div", {"class": "post-content"})
#
#     # Extract the text from the div and remove the HTML tags
#     post_text = post_div.get_text()
#
#     # Write the text to a file
#     with open("to_the_left.txt", "a", encoding="utf-8") as file:
#         file.write(post_text)

import requests
from bs4 import BeautifulSoup

# Set the base URL for the website
base_url = "https://qaamuus.net/qaamuus/?sortby=&rowstart="

# Set the starting page number and the number of pages to scrape
start_page = 0
num_pages = 1584

# Set the file name and path where you want to save the scraped data
file_name = "scraped_data.txt"
file_path = "F:\Programming\ogreniyorum" + file_name

# Open the file in write mode
with open(file_path, "w", encoding="utf-8") as file:
    # Loop through each page of the website
    for page in range(start_page, num_pages):
        # Construct the full URL for the page
        page_url = base_url + str(page * 30)

        # Send a GET request to the page URL
        response = requests.get(page_url)

        # Parse the HTML from the response
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the text data from the specified div class
        text_data = soup.find("div", class_="post-content box mark-links entry-content")

        # Remove the HTML tags from the text data
        clean_text = text_data.get_text()

        # Split the clean text into lines, removing any empty lines
        lines = [line for line in clean_text.split("\n") if line.strip() != ""]

        # Write the lines to the file, adding a blank line after each href
        for line in lines:
            file.write(line.strip())
            file.write("\n")
        file.write("\n")

