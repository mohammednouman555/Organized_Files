# Automatic File Organizer – Python Utility Tool

This is a Python-based file management utility that automatically organizes all files inside a selected folder into categorized sub-folders such as **Images**, **Documents**, **Videos**, **Music**, **Programs**, **Scripts**, **Compressed**, and **Others**.

The tool helps keep folders clean, improves workflow, and reduces manual effort in managing downloads or messy directories.

---

## 🚀 Features

* Organizes any selected folder (not limited to Downloads)
* Automatically creates category folders if missing
* Moves files based on their extensions
* Handles all common formats for documents, images, videos, scripts, etc.
* Places unidentified files in an `Others` folder
* Lightweight, fast, and very easy to use
* Fully customizable file-type categories

---

## 🖥️ How It Works

1.  Run the Python script.
2.  Enter the path of the folder you want to organize.
3.  The tool scans the folder.
4.  It automatically sorts files into proper sub-folders.
5.  Finally, it displays a summary of moved files.

---

## 📂 Example

### Folder Before

```bash
Downloads/
├── photo.jpg
├── resume.pdf
├── video.mp4
├── script.py
├── notes.txt
├── setup.exe
└── image2.png
Folder After
Bash

Downloads/
├── Images/
│   ├── photo.jpg
│   └── image2.png
├── Documents/
│   ├── resume.pdf
│   └── notes.txt
├── Videos/
│   └── video.mp4
├── Programs/
│   └── setup.exe
├── Scripts/
│   └── script.py
├── Music/
├── Compressed/
└── Others/
🧩 Code
Main script file: file_organizer_select_folder.py
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
---

## 🔧 Technologies Used

* Python 3
* `os` module
* `shutil` module

---

## 📌 Future Enhancements

* Windows `.exe` application version
* Graphical Interface (GUI)
* Logging and reporting
* Custom category creator
* Drag-and-drop support

---

## 📜 Author

**Mohammed Nouman**
* Computer Science Engineering Student
* Organized_Files Project – 2025

