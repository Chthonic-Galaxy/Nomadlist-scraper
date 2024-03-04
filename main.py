import requests
from bs4 import BeautifulSoup
import re
import json

def remove_emojis(text):
    """Removes emojis from a string"""
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U0001F1E0-\U0001F1FF"
                           u"\U00002500-\U00002BEF"
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"
                           u"\u3030"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def parse_nomadlist_categories(url):
    """Parses Nomad List costs of living page and returns a clean dictionary."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'} # Replace the user-agent with other (if need)
    response = requests.get(url, headers=headers)

    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        categories = {}
        for row in soup.find_all('tr'):
            key_cell = row.find('td', class_='key')
            value_cell = row.find('td', class_='value')

            if key_cell and value_cell:
                key = remove_emojis(key_cell.text.strip())
                value = remove_emojis(value_cell.text.strip())
                categories[key] = value
        return categories
    except Exception as e:
        print(f"Error parsing {url}: {e}")
        return {}

def get_cities_from_file(filename):
    """Reads a list of cities from a .txt file, one city per line."""
    cities = []
    with open(filename, 'r') as file:
        for line in file:
            cities.append(line.strip())
    return cities


if __name__ == "__main__":
    filename = "test_list.txt"
    cities = get_cities_from_file(filename)

    results = []
    for city in cities:
        url = f'https://nomadlist.com/{city}'
#        print(city) # print cities
        categories = parse_nomadlist_categories(url) 
        results.append({
            "city": city,
            "data": categories
        })

    with open("city_data.json", "w") as outfile:
        json.dump(results, outfile, indent=4)