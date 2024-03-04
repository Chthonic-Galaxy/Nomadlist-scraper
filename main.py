import asyncio
from bs4 import BeautifulSoup
import json
import aiohttp
import emoji

def remove_emojis(text):
    """Removes emojis from a string. Adapt this if you need selective emoji handling."""
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.EMOJI_DATA]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text

async def parse_nomadlist_categories_async(url, session):
    """Parses Nomad List costs of living page and returns a clean dictionary."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}  # Change User-Agent if needed

    try:
        async with session.get(url, headers=headers, timeout=120) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')

            # Extract city name from the URL
            city = url.split('/')[-1]  

            categories = {}
            for row in soup.find_all('tr'):
                key_cell = row.find('td', class_='key')
                value_cell = row.find('td', class_='value')

                if key_cell and value_cell:
                    key = remove_emojis(key_cell.text.strip())  # Apply if needed 
                    value = remove_emojis(value_cell.text.strip())  # Apply if needed
                    categories[key] = value

            # Return data if categories were found
            if categories:
                return {'city': city, 'data': categories}
            else:
                return None 

    except (aiohttp.ClientError, TimeoutError) as e:
        print(f"Error parsing {url} (Network/Timeout): {e}")
    except BeautifulSoup.FeatureNotFound as e:
        print(f"Error parsing {url} (HTML structure): {e}")
    except Exception as e:
        print(f"Unexpected error parsing {url}: {e}")
    return None

def get_cities_from_file(filename):
    """Reads a list of cities from a .txt file, one city per line."""
    cities = []
    with open(filename, 'r') as file:
        for line in file:
            cities.append(line.strip())
    return cities

async def main():
    filename = r"cities.txt"  # Change path to cities.txt if needed
    cities = get_cities_from_file(filename)

    results = []
    connector = aiohttp.TCPConnector(limit=10)  # Control concurrency (Change value if need; Default = 10)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for city in cities:
            url = f'https://nomadlist.com/{city}'
            print(city)
            tasks.append(asyncio.create_task(parse_nomadlist_categories_async(url, session)))

            # Introduce a small delay if desired
            await asyncio.sleep(0.2) 

        for task in asyncio.as_completed(tasks):  
            city_data = await task
            if city_data: 
                results.append(city_data)

    with open(r"city_data.json", "w", encoding="utf-8") as outfile:  # Change file name if needed
        json.dump(results, outfile, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
