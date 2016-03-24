# Ygritte
show text file lines

# How to use
Read `test.py` file.

## Example
```
from ygritte import Ygritte
yg = Ygritte()
yg.line('.', ['txt',])
yg.line('mixed', ['js', 'html', 'tex'])
yg.line('mixed', ['js', 'html', 'tex'], deep=1)
```

## LICENSE
This package itself is MIT License, but sample files's text named 's01e03.*' come from Wikipedia.
Read LICENSE file.