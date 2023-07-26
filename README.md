# discrete research


## installation

``` 
me@my:~/learn_py/discrete_helpers$ sudo apt install python3.8-venv
me@my:~/learn_py/discrete_helpers$ python3 -m venv env
me@my:~/learn_py/discrete_helpers$ source env/bin/activate
(env) me@my:~/learn_py/discrete_helpers$ 
```

Then select `env/bin/python` as Python interpreter for the project.


## dependencies

``` 
pip install pytest
```

Compare [requirements.txt](requirements.txt).


# import helpers

In [dh.py](dh.py) are imports from _discrete helpers_.

The import of the function `rev_colex_perms` works.<br>
(Its usage can be seen in [_test.py](_test.py).)

The class `Perm` can currently not be imported.<br>
It uses NetworkX and NumPy, which are not installed here.
