# discrete research

This is an example project. Classes and functions from [discrete_helpers](https://github.com/entenschule/discrete_helpers/) should be imported and used here.


## installation

``` 
me@my:~/learn_py/discrete_research$ sudo apt install python3.8-venv
me@my:~/learn_py/discrete_research$ python3 -m venv env
me@my:~/learn_py/discrete_research$ source env/bin/activate
(env) me@my:~/learn_py/discrete_research$ pip install -r requirements.txt
```

Select `env/bin/python` as Python interpreter for the project.


## install library

```
(env) tilman@t570:~/learn_py/discrete_research$ pip install  /home/tilman/learn_py/discrete_helpers/dist/discretehelpers-0.0.1-py3-none-any.whl
Processing /home/tilman/learn_py/discrete_helpers/dist/discretehelpers-0.0.1-py3-none-any.whl
Collecting networkx
  Using cached networkx-3.1-py3-none-any.whl (2.1 MB)
Collecting numpy
  Using cached numpy-1.24.4-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.3 MB)
Installing collected packages: networkx, numpy, discretehelpers
Successfully installed discretehelpers-0.0.1 networkx-3.1 numpy-1.24.4
```

The requirements NumPy and NetworkX were automatically installed.

`pip freeze` now returns three more lines:

``` 
discretehelpers==0.0.1
networkx==3.1
numpy==1.24.4
```


## testing

There is currently [one test file](_test.py). It can be executed by typing `pytest` in the console.

### failing run buttons in PyCharm

PyCharm has run buttons next to the tests.<br>
The execute something like this:<br>
`python -m unittest _test.test_perm_concat`<br>
That fails with an error:<br>
```
TypeError: calling <function test_perm_concat at 0x7f99763c3b80> returned None, not a test
```