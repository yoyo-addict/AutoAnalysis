# Author: Zach Rinehart
# Date: August 13, 2025
#
# The purpose of this script is to demonstrate basic ability to fetch automotive data from a webpage


from requests_html import HTMLSession
import json
import os
import re

def main():

    filters = ''
    with open('./filters.json', 'r') as file:
        filters = json.loads(file.read())
    
    scrape_all(filters['locations'], filters['makes'], filters['min_year'], filters['max_year'])

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

def norm_nums(mil:str, test=False):
    matches = re.findall('\$?(\d*)?,?(\d+)', mil)  # always gonna be a tupple of 2 in a list
    norm_str = ''

    # construct it
    for match in matches:
        for segment in match:
            norm_str = norm_str + segment

    # note that if I need to debug this later I'll have to print out matches from the findall function

    return norm_str

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
            listings_list.append([make.text, name.text, norm_nums(price.text), price_rating.text, norm_nums(mileage.text)])
    
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
        url = base_url + '&page=' + str(page_num)
        data.append(scrape_page(url))   # debug mode?
        print("Finished page", page_num)
        page_num += 1

    return data

# # add record creation function here
# def create_record(year_make, model, price, rating, mileage):
#     return f"{year_make}, {model}, {price}, {rating}, {mileage}"

# write the data to a file
def write_data(name:str, data:list):
    with open(name+'.csv', 'w+') as file:
        file.write("Year/Make, Model, Price, Rating, Mileage\n")
        for page in data:
            for record in page:
                # for item in record:
                #     file.writelines(item + ', ')
                file.write(f"{record[0]}, {record[1]}, {record[2]}, {record[3]}, {record[4]}\n")
                # file.write('\n')

# the big one
def scrape_all(locations:list, makes:list, year_min:int, year_max:int):

    # set working directory to drop data
    print(os.getcwd())
    os.chdir("data")
    

    for location in locations:
        for make in makes:
            # create new directory for the data
            newdir = f"{location}/{make}"
            os.makedirs(newdir, exist_ok=True)
            os.chdir(newdir)

            # loop over the years and pages
            for year in range(year_min, year_max+1):
                print("Scraping at", location, "for make", make, "of year", year)
                
                url = 'https://www.truecar.com/used-cars-for-sale/listings/'+make+'/year-'+str(year)+'/location-'+location+'/?excludeExpandedDelivery=true&searchRadius=100'
                data = scrape_pages(url)
                
                # store the data under a specific filename
                filename = make+'-'+str(year)+'-'+location
                write_data(filename, data)
            
            os.chdir("../../")

if __name__ == "__main__":
    main()