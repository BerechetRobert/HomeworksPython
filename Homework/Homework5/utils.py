import csv
import os
import uuid
import json


def read_csv(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        return list(csv_reader)


def generate_id(lst):
    for item in lst:
        item['Id'] = str(uuid.uuid1())


def horse_power_check(lst):
    slow_cars = [item for item in lst if int(item['Hp']) < 120]
    fast_cars = [item for item in lst if 120 <= int(item['Hp']) < 180]
    sport_cars = [item for item in lst if int(item['Hp']) >= 180]

    return slow_cars, fast_cars, sport_cars


def price_check(lst):
    cheap_cars = [item for item in lst if int(item['Price']) < 1000]
    medium_cars = [item for item in lst if 1000 > int(item['Price']) < 5000]
    expensive_cars = [item for item in lst if int(item['Price']) >= 5000]

    return cheap_cars, medium_cars, expensive_cars


def save_file_at_dir(dir_path, filename, file_content,):
    os.makedirs(dir_path, exist_ok=True)
    with open(f'{dir_path}/{filename}.json', 'w') as f:
        json.dump(file_content, f, ensure_ascii=False, indent=4)

