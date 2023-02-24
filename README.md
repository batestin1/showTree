
<h1 align="center">

<img src="https://img.shields.io/static/v1?label=showTree%20POR&message=bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center">showTree </p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> The showTree project is a Python library that displays the directory and file tree of a root directory in the console, with options to customize the colors of the directories and files, in addition to displaying the total number of directories and files.

The library has a main class called showTree, which accepts the root directory path as a mandatory parameter and additional options to customize colors and display the total number of directories and files. The library also includes a Help class, which prints out the usage mode and available options for the showTree class.

The library uses the os library to traverse the tree of directories and files, and the colorama library to customize the colors in the console. The project was set up to be distributed as a Python package on PyPI.

In short, the showTree library is a simple and useful tool for visualizing the structure of directories and files in a root directory in a custom way and with options to display the total number of directories and files. </p>

>> <h3> How install </h3>

```
pip3 install showTree

```

>> <h3> How Works </h3>

```

from showTree import showTree, Tips

tree = showTree(path, color_dir=None, color_file=None, show_count=False)

tree.tree() #show tree of files and dir
help = Tips() #get tips from the library
help.tips()

```
    