import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

DINING_HALLS = {'South Quad':SOUTH_QUAD_URL, 'East Quad':EAST_QUAD_URL, 'North Quad':NORTH_QUAD_URL, 'Mojo':MOJO_URL, 
                'Markley':MARKLEY_URL, 'Bursley':BURSLEY_URL}

def main(meal_of_the_day, bursley):
    for key in DINING_HALLS:
        url = DINING_HALLS[key]