import os
REGION = 0
TOTAL_REVENUE = 11
TOTAL_PROFIT = 13


def load_data():
    sales = []
    with open("../sales.csv") as file:
        file.readline()
        convert_template = []
        first_line = file.readline().replace("\n", "").split(",")
        sales.append([])
        for item in first_line:
            if item.isdigit():
                convert_template.append(int)
                sales[0].append(int(item))
            elif item.find(".") != -1 and item.replace(".", "").isdigit():
                convert_template.append(float)
                sales[0].append(float(item))
            else:
                convert_template.append(str)
                sales[0].append(item)

        for line in file:
            new_line = []
            words = line.replace("\n", "").split(",")
            if len(words) == 14:
                for index in range(len(words)):
                    new_line.append(convert_template[index](words[index]))
                sales.append(new_line)
    return sales


sales = load_data()
print(f"Loaded {len(sales)} lines of data")


def get_total_revenue(sale_line):
    return sale_line[TOTAL_REVENUE]


func = lambda x, y, z: x + y + z
print(func(1, 2, 3))
print(f"Total revenue: {sum(map(lambda line: line[TOTAL_REVENUE], sales))}")


def group_by_region(sale_lines):
    region_dict = {}
    for item in sale_lines:
        if item[REGION] in region_dict:
            region_dict[item[REGION]].append(item)
        else:
            region_dict[item[REGION]] = [item]
    return region_dict


grouped_values = group_by_region(sales)
for value in grouped_values:
    print(f"{value}: \n Lines count: {len(grouped_values[value])}" +
          f" \n Total revenue: {sum(map(lambda x: x[TOTAL_REVENUE], grouped_values[value]))}" +
          f" \n Total profit: {sum(map(lambda x: x[TOTAL_PROFIT], grouped_values[value]))}")


def ensure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def save_sales_by_region(grouped_sales, path):
    ensure_path_exists(path)
    for region in grouped_sales:
        filename = os.path.join(path, region + "_sales_data.csv")
        with open(filename, 'w') as file:
            file.writelines(map(lambda x: ",".join(map(str, x)) + '\n', grouped_sales[region]))


save_sales_by_region(grouped_values, "../Sales by regions")


dir_files = os.scandir()
for item in dir_files:
    print(item.name, item.is_file(), os.path.getsize(item.name))


def search_in_folder(path):
    files = []

    def search_internal(internal_path):
        items = os.scandir(internal_path)
        for item in items:
            item_path = os.path.join(internal_path, item.name)
            if item.is_file():
                files.append((item_path, os.path.getsize(item_path)))
            else:
                search_internal(item_path)

    search_internal(path)
    return files


files = search_in_folder("../")
for file, size in files:
    print(f"{file}, size: {size}")
# r - read
# w - write
# a - append

