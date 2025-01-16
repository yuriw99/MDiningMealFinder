from bs4 import BeautifulSoup
from selenium import webdriver

favorite_foods = [
    'Chicken Biryani',
    'Spring Rolls',
    'Fried Rice',
    'Chicken Noodle Soup',
    'Beef Noodle Soup',
    'Chicken Pasta',
    'Salmon',
    'Wide Egg Noodles',
    'Ramen',
    'Pho',
    'Roasted Broccoli',
    'Spinach Saute',
    'Scrambled Tofu',
    'Veggie Patty',
    'Lamb Gyro Meat',
    'Rice Noodle',
    'Clam Chowder',
    'Cauliflower',
    'Tempura Chicken',
    'Mashed Potatoes',
    'Macaroni',
    'Beef Brisket',
    'Mushroom Bisque',
    'Chicken Gyro',
    'Broccoli Bake',
    'Garlic Bread',
    'Savory Baked Tofu'
]

SOUTH_QUAD_URL = 'https://dining.umich.edu/menus-locations/dining-halls/south-quad/'
EAST_QUAD_URL = 'https://dining.umich.edu/menus-locations/dining-halls/east-quad/'
NORTH_QUAD_URL = 'https://dining.umich.edu/menus-locations/dining-halls/north-quad/'
MOJO_URL = 'https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/'
MARKLEY_URL = 'https://dining.umich.edu/menus-locations/dining-halls/markley/'
BURSLEY_URL = 'https://dining.umich.edu/menus-locations/dining-halls/bursley/'

dining_halls = {'South Quad':SOUTH_QUAD_URL, 'East Quad':EAST_QUAD_URL, 'North Quad':NORTH_QUAD_URL, 'Mojo':MOJO_URL, 
                'Markley':MARKLEY_URL, 'Bursley':BURSLEY_URL}

def main(meal_of_the_day):
    driver = webdriver.Chrome()
    for key in dining_halls:
        dining_url = dining_halls[key]
        driver.get(dining_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        menus = soup.find_all('div', class_='courses')
        correct_menu = None
        if len(menus) == 3:
            if meal_of_the_day == 'Breakfast':
                correct_menu = menus[0]
            elif meal_of_the_day == 'Lunch':
                correct_menu = menus[1]
            else:
                correct_menu = menus[2]
        if len(menus) == 2:
            if meal_of_the_day == 'Brunch' or meal_of_the_day == 'Lunch':
                correct_menu = menus[0]
            else:
                correct_menu = menus[1]
        if len(menus) == 1:
            if meal_of_the_day == 'Brunch' or meal_of_the_day == 'Lunch':
                correct_menu = menus[0]
            else:
                print(key, "only has one meal")
                print(" ")
                continue
        if len(menus) == 0:
            print(key, "is closed")
            print(" ")
            continue

        menu_text = correct_menu.get_text(strip=True)
        count = 0
        print(key)
        for food in favorite_foods:
            if food in menu_text:
                print(food)
                count += 1
        print("Total amount of favorite foods:", count)
        print(" ")

main("Dinner")      