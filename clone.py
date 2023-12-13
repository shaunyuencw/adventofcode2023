import shutil
import os
import requests
import yaml

def read_session_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data['session']

def download_file(session, url, output_file):
    try:
        response = requests.get(url, cookies={'session': session})
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Data saved to {output_file}.")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")

def clone_folder(template_path, new_folder):
    try:
        shutil.copytree(template_path, new_folder)
        print(f"Folder '{new_folder}' created successfully.")
        return True
    except FileExistsError:
        print(f"Folder '{new_folder}' already exists.")
        return False

def main():
    yaml_file = 'config.yaml'
    session = read_session_from_yaml(yaml_file)
 
    folder_name = input("What day is it: ")
    url = f'https://adventofcode.com/2023/day/{folder_name}/input'
    output_file = 'input.txt'

    if clone_folder('template', f"day{folder_name}"):
        os.chdir(folder_name)
        download_file(session, url, output_file)

if __name__ == "__main__":
    main()
