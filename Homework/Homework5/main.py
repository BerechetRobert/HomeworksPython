from utils import read_csv,horse_power_check,price_check,generate_id,save_file_at_dir

if __name__ == '__main__':
    csv_data = read_csv('input.csv')
    generated_ids = generate_id(csv_data)
    slow_cars, fast_cars, sport_cars = horse_power_check(csv_data)
    cheap_cars, medium_cars, expensive_cars = price_check(csv_data)

    dr_path = r"C:\Users\robyt\Desktop\pythonProject\Homework\Homework5\output_data"

    slow_cars_save = save_file_at_dir(dr_path, "slow_cars.json", slow_cars)
    fast_cars_save = save_file_at_dir(dr_path, "fast_cars.json", slow_cars)
    sport_cars_save = save_file_at_dir(dr_path, "sport_cars.json", slow_cars)
    cheap_cars_save = save_file_at_dir(dr_path, "cheap_cars.json", slow_cars)
    medium_cars_save = save_file_at_dir(dr_path, "medium_cars.json", slow_cars)
    expensive_cars_save = save_file_at_dir(dr_path, "expensive_cars.json", expensive_cars)


