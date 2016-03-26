# Ygritte
show text file lines

# How to use
Read `test.py` file.
- `Ygritte(directory, [extentions], recursive_level=0)`
- directory: target directory path, relative or absolute
- extenstion names to cound
- recursive level: defautl=0

## Example
```
from ygritte import Ygritte
yg = Ygritte()
yg.line('.', ['txt',])
yg.line('mixed', ['js', 'html', 'tex'])
yg.line('mixed', ['js', 'html', 'tex'], depth=1)
```

## LICENSE
This package itself is MIT License, but sample files's text named 's01e03.*' come from Wikipedia.
Read LICENSE file.