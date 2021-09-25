from selenium import webdriver


PATH = 'C:/Program Files (x86)/chromedriver'
option = webdriver.ChromeOptions()
option.headless = True
driver = webdriver.Chrome(PATH, options=option)

driver.get('https://www.bayut.sa/en/western-region/apartments-for-rent-in-makkah/?residence_type=family')

prices = driver.find_elements_by_class_name('f343d9ce')
frequencies = driver.find_elements_by_class_name('e76c7aca')
locations = driver.find_elements_by_class_name('_7afabd84')
bedrooms = driver.find_elements_by_css_selector('span.b6a29bc0[aria-label="Beds"]')
bathrooms = driver.find_elements_by_css_selector('span.b6a29bc0[aria-label="Baths"]')
areas = driver.find_elements_by_css_selector('span.b6a29bc0[aria-label="Area"]')
links = driver.find_elements_by_class_name('_287661cb') #link.get_attribute('href')

x = 0

for index, price in enumerate(prices):
    location = locations[index].text
    number_of_bedrooms = int(bedrooms[index].text)
    number_of_bathrooms = int(bathrooms[index].text)
    if 'Al Nasim' in location and number_of_bedrooms > 2 and number_of_bathrooms >= 2:
        x += 1
        price = price.text.split(',')
        price = int(price[0] + price[1])
        frequency = frequencies[index].text
        area = int(areas[index].text.split(' ')[0])
        link = links[index].get_attribute('href')

        print(f'apartement {x}')
        print(f'Rent: {price} {frequency}')
        print(f'Location: {location}')
        print(f'Number of bedrooms: {number_of_bedrooms}')
        print(f'Numbe rof bathrooms: {number_of_bathrooms}')
        print(f'Area: {area} Sq. M')

        show = input('Would you like to see it on the website? [yes/no]')
        
        if show.lower() == 'yes':
            second = webdriver.Chrome(PATH)
            second.get(link)
        else:
            continue


driver.close()