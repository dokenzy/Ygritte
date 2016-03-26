import os
import unittest

from ygritte import Ygritte


class TestYgritte(unittest.TestCase):
    def setUp(self):
        self.yg = Ygritte()

    def test_count_files_ext_current_dir(self):
        count = self.yg.line('.', ['txt',])
        self.assertEqual(17, count)

    def test_count_files_ext_specific_dir(self):
        count = self.yg.line('python', ['py',])
        self.assertEqual(17, count)

    def test_count_files_ext_specific_dir(self):
        _dir = os.path.dirname(os.path.abspath(__file__))
        count = self.yg.line(os.path.join(_dir, 'python'), ['py',])
        self.assertEqual(17, count)

    def test_count_files_exts(self):
        count = self.yg.line('mixed', ['js', 'html', 'tex'])
        self.assertEqual(70, count)

    def test_count_files_ext_recursive(self):
        count = self.yg.line('python', ['py',], depth=1)
        self.assertEqual(34, count)

    def test_count_files_exts_recursive(self):
        count = self.yg.line('mixed', ['js', 'html', 'tex'], depth=2)
        self.assertEqual(103, count)

    def test_count_files_exts_recursive_depth1(self):
        count = self.yg.line('deep', ['py', 'js', 'html', 'tex'], depth=1)
        self.assertEqual(54, count)

    def test_count_files_exts_recursive_depth1(self):
        count = self.yg.line('deep', ['py', 'js', 'html', 'tex'], depth=2)
        self.assertEqual(87, count)

    def test_count_files_exts_recursive_depth1(self):
        count = self.yg.line('deep', ['html', 'js'], depth=2)
        self.assertEqual(27, count)

    def test_count_files_exts_recursive_depth1(self):
        count = self.yg.line('deep', ['py', 'js', 'html', 'tex'], depth=3)
        self.assertEqual(104, count)

    def test_count_files_exts_recursive_depth(self):
        count = self.yg.line('deep', ['py', 'js', 'html', 'tex'], depth=4)
        self.assertEqual(121, count)

    def test_raise_type_error(self):
        self.assertRaises(TypeError, lambda: self.yg.line('mixed', 1))
        self.assertRaises(TypeError, lambda: self.yg.line('mixed', 's03e01.txt'))
        self.assertRaises(TypeError, lambda: self.yg.line('mixed', True))
        self.assertRaises(TypeError, lambda: self.yg.line('mixed', ('js',)))
