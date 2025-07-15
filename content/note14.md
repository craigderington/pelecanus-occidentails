Title: Python Automation Tricks with Shutil
Date: 2025-07-12 09:45
Modified: 2025-07-12 09:45
Category: Python
Tags: python, programming, standard library, shutil, directory, operations, automation
Slug: python-automation-tricks-with-shutil
Authors: Craig Derington
Summary: Manage your virtual environments with uv and pipx


#### Python Automation Tricks with Shutil
Python’s shutil library is a hidden gem for automating file and directory operations, often overlooked for its simplicity and power. It’s perfect for streamlining repetitive tasks like copying, moving, or cleaning up files, embodying Python’s clean, elegant ethos. Here’s a quick guide to shutil tricks for automation, with examples.

#### Why Shutil?
shutil (shell utilities) provides high-level file operations, surpassing os for tasks like copying directories or zipping files. It’s cross-platform and intuitive, ideal for automation scripts.

#### Key Tricks
1. Copy Files and Directories
Copy a file or entire directory (including contents) effortlessly:

```
import shutil

# Copy a single file
shutil.copy("source.txt", "destination.txt")

# Copy a directory and its contents
shutil.copytree("src_folder", "dst_folder", dirs_exist_ok=True)
```

2. Move Files
Move files or directories, overwriting if needed:

```
shutil.move("old_location.txt", "new_location.txt")
```

3. Delete Directories
Remove a directory and all its contents (like rm -rf):

```
shutil.rmtree("temp_folder", ignore_errors=True)
```

4. Create Zip Archives
Zip a directory for backups or sharing:

```
shutil.make_archive("backup", "zip", "my_folder")
```

5. Disk Usage
Check disk space before operations:

```
total, used, free = shutil.disk_usage("/")
print(f"Free space: {free // (2**30)} GB")
```

#### Automation Example: Organize Files
Here’s a script to organize files by extension into folders:

```
import shutil
import os

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            ext = os.path.splitext(filename)[1][1:].lower()
            if ext:
                dest_dir = os.path.join(directory, ext.upper())
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(filename, os.path.join(dest_dir, filename))

organize_files("downloads")
```

This moves files like doc.pdf to a PDF folder, image.jpg to JPG, etc.


#### Bonus: List Comprehension with Shutil
Combine shutil with list comprehensions for concise automation. Example: Copy all .py files to a backup folder:

```
import shutil
import glob

backup_dir = "backup_python"
os.makedirs(backup_dir, exist_ok=True)
[shutil.copy(f, backup_dir) for f in glob.glob("*.py")]
```

#### Why It’s Cool
shutil simplifies file operations with minimal code, making automation scripts clean and maintainable. It’s perfect for quick tasks like organizing downloads, backing up projects, or checking disk space. Its intuitive methods reduce boilerplate, aligning with Python’s philosophy of simplicity.


#### Pro Tip
Pair shutil with pathlib for modern path handling:

```
from pathlib import Path
shutil.copy(Path("source.txt"), Path("dest.txt"))
```

This keeps your automation scripts robust and readable.

Embrace shutil for file-handling automation—it’s the unsung hero of Python’s standard library, saving you from manual file chaos.

[shutil](https://docs.python.org/3/library/shutil.html)