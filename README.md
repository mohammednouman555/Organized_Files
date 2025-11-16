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

```
## 🔧 Technologies Used

* Python 3
* `os` module
* `shutil` module

---
```
```
## 📌 Future Enhancements

* Windows `.exe` application version
* Graphical Interface (GUI)
* Logging and reporting
* Custom category creator
* Drag-and-drop support

---
```
```
## 📜 Author

**Mohammed Nouman**
* Computer Science Engineering Student
* Organized_Files Project – 2025
```
