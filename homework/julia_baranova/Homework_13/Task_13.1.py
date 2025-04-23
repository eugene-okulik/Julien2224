import os
from datetime import datetime, timedelta


def do_smth_with_dates_from_file(file_path):
    data_dict = {}
    with open(file_path, 'r') as data_file:
        for line in data_file:
            parts = line.split()
            number = int(parts[0].rstrip('.'))
            dt_string = f"{parts[1]} {parts[2]}"
            date_time = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S.%f")
            if number == 1:
                result = (date_time + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S.%f")
            elif number == 2:
                result = date_time.strftime("%A")
            elif number == 3:
                result = (datetime.today() - date_time).days
            data_dict[number] = result
    return data_dict


base_path = os.path.dirname(__file__)
path_back_1 = os.path.dirname(base_path)
path_back_2 = os.path.dirname(path_back_1)

final_file_path = os.path.join(path_back_2, 'eugene_okulik', 'hw_13', 'data.txt')

r = do_smth_with_dates_from_file(final_file_path)
print(r)
