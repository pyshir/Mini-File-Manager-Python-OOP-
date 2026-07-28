from abc import ABC, abstractmethod
from pathlib import Path
import shutil

class Files(ABC):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        print('File is closed')

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def create_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass
    

class TextFile(Files):

    def __init__(self, name):
        super().__init__(name)

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            for i in f:
                print(i)

    def create_file(self, file): 
        with file as f:
            pass

    def write_file(self,file_name, input_text):
        with open(file_name, 'a') as f:
            f.write(input_text)


class CSVFile(Files):

    def __init__(self, name):
        super().__init__(name)

    def read_file(self, file):
            with open(file, 'r') as f:
                for i in f:
                    print(i)

    def create_file(self, file):
            with file as f:
                pass

    def write_file(self,file_name, input_text):
            with open(file_name, 'a') as f:
                f.write(input_text)



class Folder:

    def __init__(self):
        self.files = []

    def __add__(self, other):
        return self.files.append(other)

    def __len__(self):
        return len(self.files)

    def __iter__(self): # will use for menu 7. list file
        return self

    def __next__(self):
        count = 0
        while count < len(self):
            print(f'{count+1}. {self.files[count].name}')
            count += 1
        else:
            raise StopIteration

    def __getitem__(self, index):
        index = index - 1
        if index < len(self):
            return self.files[index].name
        
        print('Index out of range')
        return False

    def __call__(self, *args, **kwds):
        return True
        
    

class FileManager:

    def __repr__(self):
        csv = 'csv'
        text = 'text'
        x = f'\n***Invalid file type***\nOnly {csv!r} and {text!r} available\n'
        return x

    def get_file_type(self, name, file_type):
        if file_type == 'text':
            name = f'{name}.txt'
            file = TextFile(name)
            return file, name
        elif file_type == 'csv':
            name = f'{name}.csv'
            file = CSVFile(name)
            return file, name
        else:
            print(self)
            return False

    def check_file(self, file, folder):
        for i in folder.files:
            if i == file:
                return True
        return False


    def createFile(self, name, file_type, folder):
        if self.get_file_type(name, file_type):
            file, name = self.get_file_type(name, file_type)
            folder + file
            file.create_file(file)
            return True
                    
        return False
    

    def readFile(self, name, file_type, folder):
        if self.get_file_type(name, file_type):
            file, name = self.get_file_type(name, file_type)
            if self.check_file(file, folder):
                file.read_file(name)
                return True
                        
        print('File not Found')
        return False

    def writeFile(self, name, file_type, folder, input_text):
        if self.get_file_type(name, file_type):
            file, name = self.get_file_type(name, file_type)
            if self.check_file(file, folder):
                file.write_file(name,input_text)
                return True

        print('File not Found')
        return False

    def deleteFile(self, name, file_type, folder):
        if self.get_file_type(name, file_type):
            file, name = self.get_file_type(name, file_type)
            if self.check_file(file, folder):
                folder.files.remove(file)
                file = Path(name)
                file.unlink()
                return True
        
        return False

    def copyFile(self, name, file_type, folder, source_path, destination_path):
        if self.get_file_type(name, file_type):
            file, name =  self.get_file_type(name, file_type)
            if self.check_file(file, folder):
                folder + file
                shutil.copy2(source_path, destination_path)
                return True
        return False

    def moveFile(self, name, file_type, folder, source_path, destination_path):
            if self.get_file_type(name, file_type):
                file, name =  self.get_file_type(name, file_type)
                if self.check_file(file, folder):
                    folder.files.remove(file)
                    shutil.move(source_path, destination_path)
                    return True
            return False

    def listFile(self, folder):
        for i in folder:
            pass


def take_input():
    name = input('File name = ')
    file_type = input('text or csv = ')
    return name, file_type

if __name__ == '__main__':

    folder = Folder()
    file_manager = FileManager()

    while True:

        

        print("""
    1. Create File
    2. Read File
    3. Write File
    4. Delete File
    5. Copy File
    6. Move File
    7. List Files
    8. Search File by Index
    """)

        choice = input('Enter choice = ')

        if choice == '1':

            name, file_type = take_input()
            if file_manager.createFile(name, file_type, folder):
                print('Created')
            else:
                print('Failed')

        elif choice == '2':

            name, file_type = take_input()
            file_manager.readFile(name, file_type, folder)

        elif choice == '3':
            name, file_type = take_input()
            input_text = input('Enter text here: \n = ')
            if file_manager.writeFile(name, file_type, folder, input_text):
                print('Success')
            else:
                print('Failed')

        elif choice == '4':
            name, file_type = take_input()
            if file_manager.deleteFile(name, file_type, folder):
                print('Deleted')
            else:
                print('File not Found')

        elif choice == '5':
            name, file_type = take_input()
            source_path = Path(input('Enter source Path: = '))
            destination_path = Path(input('Enter destination Path: = '))
            if file_manager.copyFile(name, file_type, folder, source_path, destination_path):
                print('Copied')
            else:
                print('Can\'t copy')

        elif choice == '6':
            name, file_type = take_input()
            source_path = Path(input('Enter source Path: = '))
            destination_path = Path(input('Enter destination Path: = '))
            if file_manager.moveFile(name, file_type, folder, source_path, destination_path):
                print('Moved')
            else:
                print('Can\'t move')

        elif choice == '7':
            file_manager.listFile(folder)
            print(f'Total number of file is, {len(folder)}')

        elif choice == '8':
            file_index = int(input('File index: '))
            if folder():
                if folder[file_index]:
                    print(f'File found\n{folder[file_index]}')
                else:
                    print('File not found')
            else:
                print('Class not available')

        
