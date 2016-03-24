from fnmatch import fnmatch
import os

SEP = os.path.sep

class Ygritte(object):
    def line(self, folder, exts, deep=0):
        ''' get line number of files that extention is `ext` in a folder
        :param folder: directory
        :type folder: str
        :param exts: extensions
        :type exts: list
        :param deep: recursive level
        :type deep: int
        :return value: total line number
        :return type: int
        '''
        self.folder = os.path.abspath(folder)
        self.full_deep = len(self.folder.split(SEP))
        self.exts = exts
        self.deep = deep

        self.count = 0  # total line numbers

        if not isinstance(exts, list):
            raise TypeError('The type of {} must be list.'.format(exts))

        for ext in exts:
            self.a_dir(ext, self.folder)

        return self.count

    def a_dir(self, ext, _dir):
        ''' add line number of files in directory `_dir` recursively.
        :param ext: extention
        :type ext: str
        :param _dir: directory
        :type _dir: str
        :return: None
        '''
        for file in os.listdir(_dir):
            if fnmatch(os.path.join(_dir, file), '*.{}'.format(ext)):
                self.count += self.a_file(os.path.join(_dir, file))
            else:
                sub_dir = os.path.abspath(os.path.join(_dir, file))
                deep = len(sub_dir.split(SEP)) - 1
                if os.path.isdir(sub_dir) and deep - self.full_deep < self.deep:
                    self.a_dir(ext, sub_dir)

    def a_file(self, file):
        ''' count lines of `file`
        :param file: file path
        :type file: str
        :return: count of lines
        :return type: int
        '''
        with open(file) as f:
            return sum(1 for _ in f)

