# Nomadlist-scraper

## Purpose

The `Nomadlist-scraper` aims to provide digital nomads, remote workers, and potential expats with cost of living information for cities around the world. It leverages asynchronous techniques for faster data collection compared to sequential scraping.

## Features

* Extracts costs of living categories from individual city pages on Nomad List.
* Handles potential errors during web scraping.
* Removes emojis from text data for cleaner output.
* Reads a list of cities from a text file.
* Saves the scraped data in JSON format for easy analysis.

## Usage

1. **Dependencies:**
   *  Python 3.x
   *  `requests` 
   *  `beautifulsoup4`

   Install dependencies with `pip install -r requirements.txt`

2. **City List:**
   * Create a text file (e.g., `cities.txt`) with city names, one city per line.

3. **Execution:**
   *  Run the script: `python main.py` 

4. **Output:**
    * The script will create a `city_data.json` file containing the scraped costs of living data.

## Example Data Structure (city_data.json)
```
[
    {
        "city": "bangkok",
        "data": {
            " Total score": "4.86/5 (Rank #1)3205 reviews",
            " Liked by members": "65% liked it  35% disliked it",
            " Quality of life score": "Good",
            " Family score": "Okay",
            " Community score": "Great",
            " Cost": " Affordable: $1,412 / mo",
            " Internet": " Fast: 91Mbps (avg)",
            " Fun": "Good",
            " Temperature (now)": " Too hot: 33°C91°F (feels 28°C82°F)",
            " Humidity (now)": " Too dry: 0%",
            " Air quality (now)": " 90 US AQI   Bad",
            " Air quality (annual)": " Good: 55 US AQI",
            " Safety": "Good",
            " Food safety*": "Good",
            " Lack of crime*": "Good",
            " Lack of racism*": "Bad",
            " Education level*": "Mediocre",
            " Power grid": "Great",
            " Vulnerability to climate change": "Okay",
            " Income level*": "Very low: $493 / mo",
            " English speaking*": "Bad",
            " People density": " Low density: 5k ppl/km ² (1 per 14x14m)",
            " Walkability": "Great",
            " Peace (no pol. conflict)": "Okay",
            " Traffic safety*": "Bad",
            " Hospitals": "Great",
            " Happiness*": "Good",
            " Nightlife": "Great",
            " Free WiFi in city": "Great",
            " Places to work from": "Great",
            " A/C or heating": "Great",
            " Friendly to foreigners": "Great",
            " Freedom of speech*": "Okay",
            " Female friendly": "Good",
            " LGBTQ+ friendly": "Good",
            " Startup Score": "Bad",
            " Continent": "Asia",
            " Country": "Thailand",
            " Average trip length": "8 days",
            " Internet speed (avg)": "91 Mbps",
            " Weather (now)": " 33°C 91°F +  Too dry (%) = feels 28°C 82°F",
            " Air quality (annual avg)": " 55 US AQI",
            " Power": "230V50Hz",
            " Best neighborhood to stay": "Historical Center",
            " Upcoming neighborhood": "Bangkok Yai",
            " Best taxi app*": "Grab",
            " Travel medical insurance": "Safetywing",
            " 100 THB in USD": "USD 2.79",
            " Suggested ATM take out:": "THB 10,000 = USD 279",
            " Tipping": "Yes, 5%",
            " Cashless": " Yes, cards OK almost everywhere",
            " Best coworking space": "Hubba",
            " Best alt. coworking space": "The Hive",
            " Best coffee place": "True Coffee @ Siam Paragon",
            " Best 24/7 coffee place": "Too Fast To Sleep SCB",
            " Tap water": " No, not drinkable",
            " Return rate": "18% of visitors return",
            " Visitors per year": "23,270,600 visitors",
            " Tourists now": "445,980 tourists",
            " Population": "5,800,000 people",
            " GDP per capita*": "$5,911 / year",
            " Population density": " busy: 14x14m (196m ²) per person",
            " Gender ratio (population)": " 45%  55%",
            " Gender ratio (young adults)": " 52%  48%",
            " Gender ratio (nomads)": " 83%  17%",
            " Religious government": "Non-religious",
            " Online electronics shop": "Lazada",
            " Best short-haul air carrier": "Air Asia",
            " Best int'l air carrier": "Emirates",
            " Best hospital": "Bangkok Hospital",
            " Cost of living for nomad": "$1,412 / month",
            " Cost of living for expat": "$1,046 / month",
            " Cost of living for family": "$2,602 / month",
            " Cost of living for local": "$743 / month",
            " Hotel (median price)": "$29 / night",
            " Airbnb (median price)": "$1,293 / month",
            " 1br studio rent in center": "$600 / month",
            " Airbnb (median price)": "$42 / night",
            " Coworking hot desk": "$190 / month",
            " Dinner": "$3",
            " Coca-Cola (0.3L)": "$1",
            " Beer in cafe (0.5L)": "$2",
            " Coffee in cafe": "$2",
            " International school": "$12,770 / year",
            " Mobile data (~10GB)": "$5 / month",
            " Taxi price (avg trip ~3km/2mi)": "$4 / trip"
        }
    },
    {
        "city": "kuala-lumpur",
        "data": {
            " Total score": "4.48/5 (Rank #3)1525 reviews",
            " Liked by members": "86% liked it  14% disliked it",
            " Quality of life score": "Good",
            " Family score": "Okay",
            " Community score": "Good",
            " Cost": " Affordable: $1,394 / mo",
            " Internet": " Super fast: 101Mbps (avg)",
            " Fun": "Bad",
            " Temperature (now)": " Perfect: 29°C85°F (feels 35°C95°F)",
            " Humidity (now)": " Sweaty: 81%",
            " Air quality (now)": " 65 US AQI   OK",
            " Air quality (annual)": " Great: 39 US AQI",
            " Safety": "Good",
            " Food safety*": "Good",
            " Lack of crime*": "Good",
            " Education level*": "Mediocre",
            " Power grid": "Great",
            " Vulnerability to climate change": "Good",
            " Income level*": "Low: $792 / mo",
            " English speaking*": "Okay",
            " People density": " Low density: 4k ppl/km ² (1 per 17x17m)",
            " Walkability": "Okay",
            " Peace (no pol. conflict)": "Good",
            " Traffic safety*": "Bad",
            " Hospitals": "Great",
            " Happiness*": "Good",
            " Nightlife": "Bad",
            " Free WiFi in city": "Good",
            " Places to work from": "Great",
            " A/C or heating": "Okay",
            " Friendly to foreigners": "Okay",
            " Freedom of speech*": "Okay",
            " Female friendly": "Bad",
            " LGBTQ+ friendly": "Bad",
            " Startup Score": "Okay",
            " Continent": "Asia",
            " Country": "Malaysia",
            " Average trip length": "7 days",
            " Internet speed (avg)": "101 Mbps",
            " Weather (now)": " 29°C 85°F +  Sweaty (81%) = feels 35°C 95°F",
            " Air quality (annual avg)": " 40 US AQI",
            " Power": "230V50Hz",
            " Best neighborhood to stay": "Petaling Selatan",
            " Upcoming neighborhood": "Bukit Nanas",
            " Best taxi app*": "Grab",
            " Travel medical insurance": "Safetywing",
            " 10 MYR in USD": "USD 2.11",
            " Suggested ATM take out:": "MYR 1,000 = USD 211",
            " Tipping": "No",
            " Cashless": " No, cash only (esp. for foreigners)",
            " Best coworking space": "PAPER + TOAST",
            " Best alt. coworking space": "Nook",
            " Tap water": " No, not drinkable",
            " Return rate": "17% of visitors return",
            " Visitors per year": "12,843,500 visitors",
            " Tourists now": "246,145 tourists",
            " Population": "1,800,000 people",
            " GDP per capita*": "$9,508 / year",
            " Population density": " not busy: 17x17m (289m ²) per person",
            " Gender ratio (population)": " 51%  49%",
            " Gender ratio (young adults)": " 51%  49%",
            " Gender ratio (nomads)": " 83%  17%",
            " Foreign land ownership allowed": "Yes",
            " Religious government": "Religious",
            " Online electronics shop": "Lazada",
            " Apartment listings": "Ibilik",
            " Best short-haul air carrier": "Air Asia",
            " Best int'l air carrier": "Malaysia",
            " Cost of living for nomad": "$1,394 / month",
            " Cost of living for expat": "$1,060 / month",
            " Cost of living for family": "$2,487 / month",
            " Cost of living for local": "$710 / month",
            " Hotel (median price)": "$31 / night",
            " 1br studio rent in center": "$489 / month",
            " Coworking hot desk": "$156 / month",
            " Dinner": "$3",
            " Coca-Cola (0.3L)": "$0",
            " Beer in cafe (0.5L)": "$4",
            " Coffee in cafe": "$3",
            " International school": "$8,078 / year",
            " Mobile data (~10GB)": "$10 / month",
            " Taxi price (avg trip ~3km/2mi)": "$4 / trip"
        }
    }
]
```

## Contributing

Contributions are welcome! Feel free to open issues for bugs or feature requests. To submit changes, follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License.  See [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) for details.

## Disclaimer

Nomad List data is subject to change. Please verify information before making important decisions.

Please respect the terms of service of the website [https://nomadlist.com/](https://nomadlist.com).
Avoid excessive scraping that could overload their servers.
