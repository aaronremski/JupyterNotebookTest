# JupyterNotebookTest

# Summary
This repo is created to illustrate several methods for version control of Jupyter Notebooks. 

## Method 1
https://mg.readthedocs.io/git-jupyter.html  
which references: https://stackoverflow.com/questions/18734739/using-ipython-notebooks-under-version-control/20844506 

Notebook name: JupyterNotebookTest1 
Branches used: Main, rottentomato 

### Notes on Method 1
These solutions appear to be quite old, ~6-7 years. I would think by now IPython & Git/Github have this worked out

## Method 2
https://towardsdatascience.com/version-control-with-jupyter-notebook-b9630bc5996e 

Basically, you're not tracking .ipynb or checkout files. You convert to jupytertext FIRST and track all changes via converted .py files. Works nicely and you can include instructions for cloning/forking/etc a repo and converting BACK to ipynb for project continuation. 

Files used: 
Branches used: 
