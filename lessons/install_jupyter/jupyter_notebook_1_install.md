# Jupyter Notebook:  Getting Started
The Jupyter notebook is an interactive computational environment, in which you can combine code, execution, rich text, mathematics, plots and rich media. 

---

### [Install the Notebook](http://jupyter.readthedocs.io/en/latest/install.html)
Installing Jupyter using Anaconda and conda:  
For new users, we highly recommend [installing Anaconda](https://www.continuum.io/downloads). Anaconda conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science.  (Prereq: Python is installed.)

Once anaconda is installed, you can launch the notebook by typing
```{bash}
$ jupyter notebook
```

### Upgrade all libraries/packages
We will now update all the packages/libraries installed by anaconda to ensure you have the latest version of everything!

```{bash}
$ conda update --all
```

### Run the Notebook at Terminal Prompt  
Note:  The notebook will open at the directory in which you launch the notebook on your terminal.  
```
$ jupyter notebook
```
>my example
```console
(base) MacBook-Pro-4:~ abdullahhanif$ jupyter notebook
[I 20:43:47.282 NotebookApp] Serving notebooks from local directory: /Users/abdullahhanif
[I 20:43:47.282 NotebookApp] The Jupyter Notebook is running at:
[I 20:43:47.282 NotebookApp] http://localhost:8888/?token=db691e2b0e7ebf588194e4fb47da9084f591fcfd2e78552a
[I 20:43:47.282 NotebookApp]  or http://127.0.0.1:8888/?token=db691e2b0e7ebf588194e4fb47da9084f591fcfd2e78552a
[I 20:43:47.282 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

### Shut Down the Juypter Notebook App
At terminal prompt:  
 * control + c
 * type:  `y`
 
>my example 
```console
^C[I 20:45:41.988 NotebookApp] interrupted
Serving notebooks from local directory: /Users/abdullahhanif
0 active kernels
The Jupyter Notebook is running at:
http://localhost:8888/?token=db691e2b0e7ebf588194e4fb47da9084f591fcfd2e78552a
 or http://127.0.0.1:8888/?token=db691e2b0e7ebf588194e4fb47da9084f591fcfd2e78552a
Shutdown this notebook server (y/[n])? y
[C 20:45:44.356 NotebookApp] Shutdown confirmed
[I 20:45:44.365 NotebookApp] Shutting down 0 kernels
(base) MacBook-Pro-4:~ abdullahhanif$ 
```

---

### Getting to Know Jupyter

You can try out Jupyter on a browser without installing it.  
https://try.jupyter.org/

