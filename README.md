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
