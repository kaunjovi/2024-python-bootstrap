# 2024-python-bootstrap
A opinionated template of a good python project layout and toolset, for 2024

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

