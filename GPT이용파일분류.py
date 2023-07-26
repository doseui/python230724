import os
import shutil

def move_files_by_extension(src_folder, dest_folder, extensions):
    for root, _, files in os.walk(src_folder):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in extensions:
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, file)
                shutil.move(src_path, dest_path)

if __name__ == "__main__":
    # Specify the source and destination folders
    downloaded_folder = "C:/Users/student/Downloads"
    image_folder = os.path.join(downloaded_folder, "image")
    data_folder = os.path.join(downloaded_folder, "data")
    docs_folder = os.path.join(downloaded_folder, "docs")

    # Create destination folders if they don't exist
    for folder in [image_folder, data_folder, docs_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Specify the file extensions for each folder
    image_extensions = ['.jpg', '.jpeg']
    data_extensions = ['.csv', '.xlsx']
    docs_extensions = ['.pdf']

    # Move files to their respective folders
    move_files_by_extension(downloaded_folder, image_folder, image_extensions)
    move_files_by_extension(downloaded_folder, data_folder, data_extensions)
    move_files_by_extension(downloaded_folder, docs_folder, docs_extensions)

    print("Files have been moved successfully!")
