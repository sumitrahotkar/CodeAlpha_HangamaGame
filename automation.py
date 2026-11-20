
import os
import shutil

source_folder = "My_Photos"
destination_folder = "JPG_Files"

if not os.path.exists(source_folder):
    print("Source folder not found!")

else:
    os.makedirs(destination_folder, exist_ok=True)

    for file in os.listdir(source_folder):

        if file.lower().endswith(".jpg"):
            source = os.path.join(source_folder, file)
            destination = os.path.join(destination_folder, file)

            shutil.move(source, destination)

            print(file, "moved successfully!")

    print("File organization completed!")
