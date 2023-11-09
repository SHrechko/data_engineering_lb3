import glob
import json
import csv
from flatten_json import flatten


def main():
    root_directory = 'data'

    json_paths = [file for file in glob.glob(
        root_directory + '/**/*.json', recursive=True)]

    for json_path in json_paths:
        with open(json_path, "r") as json_file:
            my_json = json.load(json_file)
            
            flattened_json = []
            if type(my_json) is list:
                for item in my_json:
                    if type(item) is dict:
                        flattened_json.append(flatten(item))
            elif type(my_json) is dict:
                flattened_json = [flatten(my_json)]

            with open(json_path[:-4]+'csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)

                header = flattened_json[0].keys() if flattened_json else []
                csv_writer.writerow(header)

                for item in flattened_json:
                    csv_writer.writerow(item.values())


if __name__ == "__main__":
    main()
