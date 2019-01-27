#### Setup

- `mkvirtualenv <env-name>`
- `pip install -r requirements.txt`
- `python setup.py install` <-- Important, otherwise module won't be found by `py.test`


#### Running Test

- `pytest -vv`


#### Testing in iPython or Python Console

##### Testing Depth of Object Keys (Problem 1 & 2)

```python

from bongotest.depthcheck import get_depths, print_depth

# A list of depth tuple(unordered), read the method docstring to know more
get_depths({'a': 1, 'b': 2, 'c': {'d': 10, 'e': {'f': 11}}})


# Prints the solution you expect from an object properly
print_depth({'a': 1, 'b': 2, 'c': {'d': 10, 'e': {'f': 11}}})
```

##### Testing Least Common Ancestor (Problem 3)

```python

from bongotest.datastructure import create_bst, get_node
from bongotest.lca import lca

# Create a bst first
bst = create_bst()

# Test lca for different nodes
print lca(bst[2], bst[4]).value

```
