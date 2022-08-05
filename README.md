# ClashOfCode-Scraper

A project used to scrape and analyse Coding Game's [Clash Of Code](https://www.codingame.com/multiplayer/clashofcode) game results.

## Requirements

* [Web Scraper extension](https://www.webscraper.io/)
* Python 3.9+

## Getting the data

Do the following steps to get the data from the games:
1. Open the Web Scrapper pluging in your browser's web development tools (Ctrl + Shift + i)
2. Create and import a new Sitemap
3. Copy the scraping code the from the Sitemap [file](/scraper/games-site-map.txt).
4. Add the game urls you want to scrap in the Sitemap metadata. (Sitemap clashOfCode -> Edit metadata -> Start URL)
5. Execute the web scraping. (Sitemap clashOfCode -> Scrape) N.B. : Set the request interval to 5000 ms.
6. Refresh the data and export as CSV. 
7. Import the CSV file to the [database folder](/scraper) of the project and rename it to "data.csv".

> N.B. : In order to be able to scrap the game results you should be logged in to your Coding Game account.

## Installation and DB creation

Execute the following Powershell script

```
.\install.ps1
```

## Running the API

Execute the following Powershell script

```
.\run.ps1
``` 

## Adding the university to the player table

In order to be able to know what university each player is in, execute the following steps:

1. Launch the API
2. Send a GET request to the ` /players ` end-point
3. Copy the json result and import it to the scrapper as a sitemap
4. Scrap the website
5. Export the data as CSV
6. Send a POST request to the ` /players ` end-point and specify in the body the CSV file in the form-data

This will add the university name in the players table if the scraper was able to retrieve that. 
