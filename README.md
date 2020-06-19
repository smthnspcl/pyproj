## pyproj
tool to speed up development<br>
### features?
- [x] creates a project structure for you
- [ ] compiles your project
- [ ] pypi integration
### how to ..
#### ... use by cli
```shell script
usage: pyproj [-h] -n NEW [--no-mit] -a AUTHOR

optional arguments:
  -h, --help            show this help message and exit
  -n NEW, --new NEW     project name
  --no-mit
  -a AUTHOR, --author AUTHOR
                        author name
```
#### ... use by code
```python
from pyproj import Project
Project.new("testProject", True, "Pascal Eberlein")
```