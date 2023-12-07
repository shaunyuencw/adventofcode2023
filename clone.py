import shutil

def clone_folder(template_path, new_folder):
    try:
        shutil.copytree(template_path, new_folder)
        print(f"Folder '{new_folder}' created successfully.")
        return True
    except FileExistsError:
        print(f"Folder '{new_folder}' already exists.")
        return False

def main():
    folder_name = input("Enter the folder name: ")
    clone_folder('template', folder_name)

if __name__ == "__main__":
    main()
