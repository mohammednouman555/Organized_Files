import os
import shutil

def organize_files(target_folder):
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Music": [".mp3", ".wav", ".aac"],
        "Compressed": [".zip", ".rar", ".7z"],
        "Programs": [".exe", ".msi"],
        "Scripts": [".py", ".js", ".sh", ".bat"]
    }

    # Create category folders
    for category in FILE_TYPES.keys():
        category_path = os.path.join(target_folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Organize files
    for file_name in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file_name)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

        moved = False
        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                shutil.move(file_path, os.path.join(target_folder, category, file_name))
                print(f"Moved: {file_name} → {category}")
                moved = True
                break

        if not moved:
            other_path = os.path.join(target_folder, "Others")
            if not os.path.exists(other_path):
                os.makedirs(other_path)
            shutil.move(file_path, os.path.join(other_path, file_name))
            print(f"Moved: {file_name} → Others")


if __name__ == "__main__":
    folder = input("Enter the folder path you want to organize: ")

    if not os.path.isdir(folder):
        print("Invalid folder path!")
    else:
        print("Organizing files... Please wait.")
        organize_files(folder)
        print("Completed!")
