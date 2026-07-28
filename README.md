# 📁 Mini File Manager (Python OOP)

**Jahid, Whatsapp: 8801309495010**

A simple command-line **Mini File Manager** built with Python using Object-Oriented Programming (OOP) concepts. This project demonstrates file handling, abstraction, inheritance, polymorphism, encapsulation, context managers, and Python dunder methods.

> **Note:** This project was developed as an educational OOP assignment. The implementation focuses on demonstrating OOP concepts rather than building a production-ready file manager.

---

## ✨ Features

- ✅ Create Text File
- ✅ Create CSV File
- ✅ Read File
- ✅ Write to File
- ✅ Delete File
- ✅ Copy File
- ✅ Move File
- ✅ List All Files
- ✅ Search File by Index

---

# 📚 OOP Concepts Used

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

---

# 🧩 Dunder Methods Implemented

| Method | Purpose |
|---------|---------|
| `__enter__()` | Context Manager |
| `__exit__()` | Context Manager Cleanup |
| `__iter__()` | Make Folder Iterable |
| `__next__()` | Iterate Through Files |
| `__getitem__()` | Access File by Index |
| `__call__()` | Callable Folder Object |
| `__repr__()` | Custom Representation |

---

# 📂 Project Structure

```
MiniFileManager/
│
├── main.py
├── README.md
└── generated files (.txt/.csv)
```

---

# 🏛 Class Diagram

```
                 +----------------+
                 |   Files (ABC)  |
                 +----------------+
                 | name           |
                 +----------------+
                 | create_file()  |
                 | read_file()    |
                 | write_file()   |
                 +-------▲--------+
                         |
         -------------------------------
         |                             |
+-------------------+        +-------------------+
|    TextFile       |        |     CSVFile       |
+-------------------+        +-------------------+

                +----------------+
                |    Folder      |
                +----------------+
                | files[]        |
                +----------------+

                +----------------+
                |  FileManager   |
                +----------------+
                | Create         |
                | Read           |
                | Write          |
                | Delete         |
                | Copy           |
                | Move           |
                | List           |
                +----------------+
```

---

# 🖥 Menu

```
1. Create File
2. Read File
3. Write File
4. Delete File
5. Copy File
6. Move File
7. List Files
8. Search File by Index
```

---

# 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/MiniFileManager.git
```

### Go to the project directory

```bash
cd MiniFileManager
```

### Run

```bash
python main.py
```

---

# 💡 Example

```
Enter choice = 1

File name = notes

text or csv = text

Created
```

```
Enter choice = 3

File name = notes

text or csv = text

Enter text here:

Hello World
```

```
Enter choice = 2

Hello World
```

---

# 📖 Technologies Used

- Python 3
- pathlib
- shutil
- abc (Abstract Base Class)

---

# 🎯 Learning Objectives

This project demonstrates:

- Abstract Base Classes (ABC)
- Context Managers
- File Handling
- Custom Dunder Methods
- Object-Oriented Programming
- Python Iterators
- Method Overriding
- Inheritance
- Polymorphism

---

# ⚠️ Limitations

This project is intended for learning purposes.

Some implementations are simplified to satisfy academic OOP requirements and may differ from how a real-world file manager would be designed.

---

# 👨‍💻 Author

**Jahid**

GitHub: https://github.com/pyShir

---

## ⭐ If you found this project useful, consider giving it a star!
