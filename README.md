# 2024-python-bootstrap
A opinionated template of a good python project layout and toolset, for 2024

- What should be the top level folder structure. 
- Where should you keep the source code. 
- What should you use for dependency management. 


## 2024 Python Boot Project 

- 2024-Python-Boot combined means Bootstrapping a Python Application. 
- It simply means You have to configure your application to the bare minimum to get your Application up and Running. 
- Python boot takes an 'Opinionated' view of what a basic Application should have.


## Create a github repo 

- Create a repo in github. https://github.com/kaunjovi/2024-python-bootstrap
- Clone it in the devbook. 
- Open it in codium

```
kaunjovi@devbook code % pwd 
/Users/kaunjovi/code
kaunjovi@devbook code % git clone git@github.com:kaunjovi/2024-python-bootstrap.git
Cloning into '2024-python-bootstrap'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
Receiving objects: 100% (5/5), 6.30 KiB | 6.30 MiB/s, done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
kaunjovi@devbook code % cd 2024-python-bootstrap 
kaunjovi@devbook 2024-python-bootstrap % codium .
kaunjovi@devbook 2024-python-bootstrap % 
```

## Check for Python 

```
kaunjovi@devbook python-poetry % where python3
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
/usr/local/bin/python3
/usr/bin/python3
```

```
kaunjovi@devbook ~ % python3 --version 
Python 3.12.1
kaunjovi@devbook ~ % pip --version 
pip 24.0 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
kaunjovi@devbook ~ % poetry --version 
Poetry (version 1.8.2)
``` 



# DO NOT go down the poetry path. 

- Simply could not make the 1.7.0 version work. 

```
kaunjovi@devbook 2024-python-bootstrap % poetry --version 
Poetry (version 1.7.0)
```

- It kept complaining about not finding python. 


## Install poetry

- https://python-poetry.org/docs/#installing-with-the-official-installer
- With official installer please 
- might face ssl certificate issue 
- https://stackoverflow.com/questions/68275857/urllib-error-urlerror-urlopen-error-ssl-certificate-verify-failed-certifica
- post installation you have to add poetry to path 
- (Add a directory to PATH in ZSH)[https://www.geeksforgeeks.org/add-a-directory-to-path-in-zsh/]
- https://stackoverflow.com/questions/11025980/how-to-add-usr-local-bin-in-path-on-mac
- .zshrc’ is typically used for interactive shell configurations and is loaded every time you start a new Zsh session. 
- ‘.zprofile’, on the other hand, is loaded when you start a login shell. 
- If you want to set your PATH system-wide, it’s often better to use ‘.zprofile’. 
- However, if you want to set PATH for interactive use only, use ‘.zshrc’.




### use poetry to initiate the project

- What all does it have? 

```
kaunjovi@devbook 2024-python-bootstrap % poetry init
```

## activate poetry shell and run a hello world. 

```
kaunjovi@devbook 2024-python-bootstrap % poetry shell
Spawning shell within /Users/kaunjovi/code/2024-python-bootstrap/.venv
Restored session: Mon Mar 18 01:26:51 IST 2024
kaunjovi@devbook 2024-python-bootstrap % emulate bash -c '. /Users/kaunjovi/code/2024-python-bootstrap/.venv/bin/activate'
(2024-python-bootstrap) kaunjovi@devbook 2024-python-bootstrap % python hello-world.py
Hello world
```


# How to name python files and folders. 

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- Guido’s key insights is that code is read much more often than it is written
- The naming conventions of Python’s library are a bit of a mess
- Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.
- Modules should have short, all-lowercase names. 
- Underscores can be used in the module name if it improves readability. 
- Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

- Function names should be lowercase, with words separated by underscores as necessary to improve readability.
- Variable names follow the same convention as function names.

- Huh. What is this? 
- Always use self for the first argument to instance methods.
- Always use cls for the first argument to class methods.

## Project structure for Python 

- [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
- If your module consists of only a single file, you can place it directly in the root of your repository
- Your module package is the core focus of the repository. It should not be tucked away 

```
sample.py
sample/__init__.py
sample/core.py
```

- [MIT license](https://choosealicense.com/licenses/mit/)

```
./LICENSE
```

- ./requirements.txt for the dependencies 

- ./test_sample.py or ./tests
- Use a simple (but explicit) path modification to resolve the package properly.
- Requiring a developer to run setup.py develop to test an actively changing codebase also requires them to have an isolated environment setup for each instance of the codebase.

- tests/context.py

```
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample
```

- and within each test 

```
from .context import sample
```

## Modules

## Packages

- https://docs.python-guide.org/writing/structure/#packages

- Any directory with an __init__.py file is considered a Python package.
- A file modu.py in the directory pack/ is imported with the statement import pack.modu.
- This statement will look for __init__.py file in pack and execute all of its top-level statements. 
- Then it will look for a file named pack/modu.py and execute all of its top-level statements. 
- After these operations, any variable, function, or class defined in modu.py is available in the pack.modu namespace.
- Leaving an __init__.py file empty is considered normal and even good practice, if the package’s modules and sub-packages do not need to share any code.

```
import pack.modu
import very.deep.module as mod 
```

## Testing 

- [Testing Your Code](https://docs.python-guide.org/writing/tests/)
- [py.test](https://docs.python-guide.org/writing/tests/#py-test)
- https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
- https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

## TODO

[] Run all tests on change of any relevant code. 
[] Provide a report on test coverage. 
[] Run a specific test. 
[] Look for any changes in the files, if any change, run all tests. 
