# Author: Zach Rinehart
# Date: July 28, 2025
#
# The purpose of this script is to demonstrate basic ability to fetch automotive data from a webpage


from requests_html import HTMLSession
import json

def main():
    # scrape_pages('https://www.truecar.com/used-cars-for-sale/listings/toyota/year-2023/location-silver-spring-md/?excludeExpandedDelivery=true&searchRadius=100')
    
    # some testing fields
    # makes = ['audi', 'rivian', 'bmw', 'toyota']
    # makes = get_makes()
    # locations = ['washington-dc', 'philadelphia-pa', 'new-york-ny', 
                #  'richmond-va', 'norfolk-va', 'raleigh-nc', 
                #  'atlanta-ga', 'boston-ma']
    # locations = ['atlanta-ga', 'boston-ma']
    # locations = ['miami-fl', 'orlando-fl']
    
    # scrape_all(locations, makes, 2018, 2024)


    # testing JSON
    filters = ''
    with open('/home/dawson/Code/Scrapy/AutoScraper/test_and_xplor/autoscraper_requests/crawlers/filters.json', 'r') as file:
        filters = json.loads(file.read())

    # DEBUG
    print(filters)
    for location in filters['locations']:
        print(location)
    for make in filters['makes']:
        print(make)
    print('minimum year:', filters['min_year'], '\nmaximum year:', filters['max_year'])
    
def get_makes():
    return ['acura', 'alfa-romeo', 'audi', 'bmw', 
            'buick', 'cadillac', 'chevrolet', 
            'chrysler', 'dodge', 'fiat', 'ford',
            'genesis', 'gmc', 'honda', 'hyundai', 
            'infiniti', 'jaguar', 'jeep', 'kia', 
            'land-rover', 'lexus', 'lincoln', 'lucid'
            'maserati', 'mazda', 'mercedes-benz', 
            'mini', 'mitsubishi', 'nissan', 'polestar', 
            'ram', 'rivian', 'subaru', 'tesla', 'toyota',
            'vinfast', 'volkswagen', 'volvo']


# page scraping logic
def scrape_page(url, debug=False):
    
    if debug == True:
        print("Scraping url", url)  # DEBUG

    session = HTMLSession()
    r = session.get(url)

    listings_html = r.html.find('[data-test="allVehicleListings"] ul li')
    listings_list = []

    for listing_html in listings_html:
        make = listing_html.find('[data-test=vehicleCardConditionYearMake]', first=True)
        name = listing_html.find('[data-test=vehicleCardTrim]', first=True)
        price = listing_html.find('[data-test=vehicleCardPricingPrice]', first=True)
        price_rating = listing_html.find('[data-test=vehicleCardPriceRating]', first=True)
        mileage = listing_html.find('[data-test=vehicleMileage]', first=True)

        # add this data to the list
        if make is not None and name is not None and price is not None and price_rating is not None and mileage is not None:
            listings_list.append([make.text, name.text, price.text, price_rating.text, mileage.text])
    
    return listings_list

# scrape_page multiple times with pagination
def scrape_pages(base_url:str):
    data = []

    # find maximum page number
    session = HTMLSession()
    r = session.get(base_url)
    pages = r.html.find('[data-test=paginationLink]')
    
    try:
        max_page_num = int(pages[-1].text)  # the apparent wraparound index for accessing the final page num
        print('Pages stop at', max_page_num)
    except IndexError:
        print("FYI, it seems this is only one page long or it doesn't exist")
        max_page_num = 1


    # loop over the pages
    for page_num in range(1, max_page_num+1):
        try:
            url = base_url + '&page=' + str(page_num)
            data.append(scrape_page(url))
            print("Finished page", page_num)
            page_num += 1
        except:
            print("Error in page looping!")
            break

    return data

# write the data to a file
def write_data(name:str, data:list):
    with open(name+'.csv', 'w+') as file:
        for page in data:
            for record in page:
                for item in record:
                    file.writelines(item + ', ')
                file.write('\n')

def scrape_all(locations:list, makes:list, year_min:int, year_max:int):
    for location in locations:
        for make in makes:
            for year in range(year_min, year_max+1):
                print("Scraping at", location, "for make", make, "of year", year)
                
                url = 'https://www.truecar.com/used-cars-for-sale/listings/'+make+'/year-'+str(year)+'/location-'+location+'/?excludeExpandedDelivery=true&searchRadius=100'
                # print(url)  # DEBUG
                data = scrape_pages(url)
                
                # store the data under a specific filename
                filename = make+'-'+str(year)+'-'+location
                write_data(filename, data)

if __name__ == "__main__":
    main()