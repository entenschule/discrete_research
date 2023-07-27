# discrete research

This is an example project. Classes and functions from [discrete_helpers](https://github.com/entenschule/discrete_helpers/) should be imported and used here.


## first attempt

In [dh.py](dh.py) are imports from _discrete helpers_.

The import of the function `rev_colex_perms` works.<br>
(Its usage can be seen in [_test.py](_test.py).)

The class `Perm` can currently not be imported.<br>
It uses NetworkX and NumPy, which are not installed here.


## installation

``` 
me@my:~/learn_py/discrete_research$ sudo apt install python3.8-venv
me@my:~/learn_py/discrete_research$ python3 -m venv env
me@my:~/learn_py/discrete_research$ source env/bin/activate
(env) me@my:~/learn_py/discrete_research$ pip install -r requirements.txt
```

Select `env/bin/python` as Python interpreter for the project.
