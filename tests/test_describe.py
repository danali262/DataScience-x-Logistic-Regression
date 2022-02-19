import unittest


# uncomment in case the import describe doesn't work
# import sys, os.path

# bin_path = os.path.dirname(os.path.realpath(__file__))
# lib_path = os.path.abspath(os.path.join(bin_path, '..', 'srcs'))
# sys.path.insert(0, lib_path)

class TestDescribeScript(unittest.TestCase):

    # def SetUp(self):

    def test_input(self):
        with self.assertRaises(SystemExit):

    # def tearDown(self) -> None:


if __name__ = "__main__":
    unittest.main()