import os, shutil

source_folder = input(r"Enter your directory path: ")

if not os.path.exists(source_folder):
    print("Source folder does not exist.")
else:
    destination_folder = rf"{source_folder}\Organized"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(path=source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension[1:]
            type_folder = os.path.join(destination_folder, file_extension)
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            destination_path = os.path.join(type_folder, filename)
            shutil.move(source_path, destination_path)

    print("Files organized successfully!")
