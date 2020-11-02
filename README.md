# JupyterNotebookTest

# Summary
This repo is created to illustrate several methods for version control of Jupyter Notebooks. 

## Method 1
https://mg.readthedocs.io/git-jupyter.html  
which references: https://stackoverflow.com/questions/18734739/using-ipython-notebooks-under-version-control/20844506 

Notebook name: JupyterNotebookTest1 
Branches used: Main, rottentomato 

### Notes on Method 1
These solutions appear to be older, ~6-7 years, and after reviewing documenation, a little too cumbersome for me. Working with method 2 for a while and will determine best fit solution 

## Method 2
https://towardsdatascience.com/version-control-with-jupyter-notebook-b9630bc5996e 

Basically, you're not tracking .ipynb or checkout files. You convert to jupytertext FIRST and track all changes via converted .py files. Works nicely and you can include instructions for cloning/forking/etc a repo and converting BACK to ipynb for project continuation. 

Files used: 
Branches used: 
