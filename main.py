import os
import yaml

def create_directory(path):
    try:
        os.makedirs(path)
        print(f"Created folder: {path}")
    except FileExistsError:
        print(f"Folder already exists: {path}")

def create_folder_structure(data):
    for folder_name in data.keys():
        create_directory(folder_name)
        if isinstance(data[folder_name], dict):
            os.chdir(folder_name)
            create_folder_structure(data[folder_name])
            os.chdir('..')

if __name__ == "__main__":
    # add your yaml file name
    yaml_file = "sample.yaml"

    try:
        with open(yaml_file, 'r') as file:
            folder_structure_data = yaml.safe_load(file)

        if folder_structure_data:
            create_folder_structure(folder_structure_data)
        else:
            print("Error: Empty YAML file.")

    except FileNotFoundError:
        print(f"Error: YAML file '{yaml_file}' not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
