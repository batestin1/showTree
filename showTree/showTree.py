
#############################################################################################################################
#   filename:showTree.py                                                       
#   created: 2023-02-23                                                              
#   import your librarys below                                                    
#############################################################################################################################
import os
from colorama import init, Fore, Style

class showTree:
    def __init__(self, root_path, color_dir=None, color_file=None, show_count=False):
        self.root_path = root_path
        self.color_dir = color_dir or Fore.RED
        self.color_file = color_file or Fore.WHITE
        self.show_count = show_count
        self.total_files = 0
        self.total_dirs = 0
        init() 

    def tree(self, padding=''):
        files = os.listdir(self.root_path)
        files.sort()
        for file_name in files:
            full_path = os.path.join(self.root_path, file_name)
            if os.path.isdir(full_path):
                print(padding + self.color_dir + '|____' + file_name + Style.RESET_ALL)
                self.total_dirs += 1
                showTree(full_path, self.color_dir, self.color_file, self.show_count).tree(padding + '|   ')
            else:
                print(padding + self.color_file + '|    ' + file_name + Style.RESET_ALL)
                self.total_files += 1

        if self.show_count:
            print(f"Total de Dir: {self.total_dirs}")
            print(f"Total de Files: {self.total_files}")

class Tips:
    def tips(self):
        print("Usage: python showTree.py [OPTIONS] PATH\n")
        print("OPTIONS:")
        print(" --color-dir=COLOR Set color for directories (eg red, blue, green)")
        print(" --color-file=COLOR Set color for files (eg red, blue, green)")
        print(" --no-count Do not display total directories and files\n")
        print("Example: python showTree.py --color-dir=blue /path/to/directory")