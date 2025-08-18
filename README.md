The goal of this project is for Zach to demonstrate familiarity and skill with handling data from a multitude of aspects, from raw, uncleaned data, to polished data, to insights, predictive models, and more.

DISCLAIMER: This software currently runs as of the first half of August 2025. It may not continue to run if Truecar updates their website in a way that is incompatible with the way I have built this scraper.

HOW TO RUN THIS SOFTWARE:
- Firstly, this program utilises the requests-html Python library. Just make sure that it's installed in whatever venv this program is running in. Heads up - I had a complication when installing it where it needed an additional library to be installed, but I was able to install the second package and get it to work without any issues. 
- This program has three essential components: 1) The main Python scraping script, 2) the filters.json file, and 3) the data directory, each of the latter two named as such respectively. The data from the scraper goes into the data directory, filtered by city and make. The filters.json file contains the filters pertaining to what is scraped, including the cities, makes, and vehicle years. Feel free to use the one already included as a template for yours.

WHAT IS SCRAPED?
- All cars listed within a 100-mile radius of each city in the filters-json file is scraped.
- Each record from each car contains the following data points:
  - Make/Year
  - Model, often with trim details
  - Listed price
  - Rated assessment of the price (e.g. good deal/bad deal, scraped directly from the website)
  - Mileage
 
Have fun scraping!
