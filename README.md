## pyproj
tool to speed up development<br>
### features?
* [x] creates a project structure for you
* [x] compiles your project
* [x] pypi integration
> implies you have already created your pypirc
### how to ..
#### ... install
```shell script
pip3 install git+https://github.com/smthnspcl/pyproj
```

#### ... use by cli
```shell script
usage: pyproj [-h] -n NEW [--no-mit] -a AUTHOR

optional arguments:
  -h, --help            show this help message and exit
  -n NEW, --new NEW     project name
  --no-mit
  -a AUTHOR, --author AUTHOR
                        author name

eg.: pyproj -n "test" -a "Pascal Eberlein"
```
#### ... use by code
```python
from pyproj import Project
Project.new("testProject", True, "Pascal Eberlein")
```