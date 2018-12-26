import unittest

class Animal(object):
    def run(self,key):
        self.key = key
        print("test run():",key)

    def names(self,name):
        self.name = name
        print("test names:",self.name)

class test(unittest.TestCase):
    a = Animal()
    def setUp(self):
        print("开始执行测试用例")
        pass
    def test_run(self):
        self.a.run(1)
        self.assertEqual(self.a.key,1)
        pass
    def test_names(self):
        self.a.names('mei')
        self.assertEqual(self.a.name,'yuan','测试失败')
        pass
    def tearDown(self):
        print("结束测试")
        pass

if __name__== '__main__':
    unittest.main()
