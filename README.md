# JupyterNotebookTest

# Summary
This repo is used to test methods for version control of Jupyter Notebooks. 
<br/><br/>
## Method 1
https://mg.readthedocs.io/git-jupyter.html  
which references: https://stackoverflow.com/questions/18734739/using-ipython-notebooks-under-version-control/20844506<br />
<br/>
Files: JupyterNotebookTest1.ipynb<br/>
Branches: **main, rottentomato**<br/>
<br/>
**_Notes on Method 1_**<br/>
These solutions appear to be older, ~6-7 years, and after reviewing documenation, a little too cumbersome for me. Working with method 2 for a while and will determine best fit solution 
<br/>
## Method 2
### [Jupytext](https://jupytext.readthedocs.io/en/latest/index.html)<br/>

Nice How-to:<br/>
https://towardsdatascience.com/version-control-with-jupyter-notebook-b9630bc5996e 

<br/>
Basically, you're not tracking .ipynb or checkout files. You convert to jupytertext FIRST and track all changes via converted .py files. Works nicely and you can include instructions for cloning/forking/etc a repo and converting BACK to ipynb for project continuation. <br/>
<br/>
Establishing a link between the notebook and the .py file is easy. Here are 2 ways to do so:

1. 
![screenshot](/jupytext_ss.jpg?raw=true "Jupytext screenshot")

2. command line: >jupytext --to py notebook.ipynb 
[Additional commands](https://jupytext.readthedocs.io/en/latest/using-cli.html)


Branches: **main, v1.1**<br/>

