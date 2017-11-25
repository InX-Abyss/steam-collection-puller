from bs4 import BeautifulSoup
import requests


def find_all_ids(soup):
    i = soup.find_all("div", class_="collectionItem")
    print(i)
    return i


# We'll have the user assign their collection ID at some point during development. For now, it'll have to be added into
# this file prior to execution. The ID the user picks is being assigned to the variable: "collectionid"
collectionid = "1207668768"

# Here we are just creating the full unique URL from the base collection URL, and then plugging in the user added ID.
# The result of this functional string (f"") is then stored into "url" and printed for the user in the console.
url = f"http://steamcommunity.com/sharedfiles/filedetails/?id={collectionid}"
print(f"Pulling the mod ID's from the following URL: {url}")

# First we make a request, via the ".get()" function, to the URL and store the resulting response data into "page".
# We then continue by printing the response's status code (.status_code is an attribute), and then printing the HTML
# contents (.content) into the console for the user to review. "requests.get()" is the function that pulled this data.
# Requests is a library of functions, such as get(), for requesting web page response data.
page = requests.get(url)
print(f"Page was pulled with the following code: {page.status_code}")
print(f"Here is the raw HTML from the page:\n{page.contents}")

# Here we use the BeautifulSoup(html/xml/data, parser) function to create a BeautifulSoup parsable object, "soup",
# out of our "page" object. The "page" object has the .content attribute attached in order to pass the raw
# HTML contents only, and not the object's full data as a whole.
# BeautifulSoup is a library of tools for processing web page data via python.
soup = BeautifulSoup(page.content, 'html.parser')

# Here we will be executing our function "find_all_ids(soup)" in order to extract all the divs that have our desired
# IDs within them. Those IDs are then passed to another function
appIds = find_all_ids(soup)
