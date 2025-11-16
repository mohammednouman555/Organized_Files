import os
import shutil

# -------------------------------
# Automatic File Organizer Script
# -------------------------------

# Set the folder you want to organize
TARGET_FOLDER = r"C:\Users\admin\organized files"   # Change this path

# File type grouping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Compressed": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".sh", ".bat"]
}


def organize_files():
    """Organize files inside the target folder by their extensions."""

    # Make category folders if not exist
    for category in FILE_TYPES.keys():
        category_path = os.path.join(TARGET_FOLDER, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Loop through files in target folder
    for file_name in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file_name)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Extract file extension
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

        # Check file type and move
        moved = False
        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                shutil.move(file_path, os.path.join(TARGET_FOLDER, category, file_name))
                print(f"Moved: {file_name} → {category}")
                moved = True
                break

        # If extension not matched
        if not moved:
            other_path = os.path.join(TARGET_FOLDER, "Others")
            if not os.path.exists(other_path):
                os.makedirs(other_path)
            shutil.move(file_path, os.path.join(other_path, file_name))
            print(f"Moved: {file_name} → Others")


# Run the organizer
if __name__ == "__main__":
    print("Organizing files, please wait...")
    organize_files()
    print("Completed! Folder has been cleaned and structured successfully.")
