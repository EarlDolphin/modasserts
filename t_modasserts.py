#!/usr/bin/env python3
import unittest
from modasserts import myAsserts

def func(x): return 1/x

class TestTheTests(unittest.TestCase, myAsserts):
  def setup(self):
    pass

  def test_pass1(self):
    self.assertFail(asrt=self.assertEqual, first=1, second=2)
  def test_pass2(self):
    self.assertFail(asrt=func, x=0)
  def test_pass3(self):
    self.assertFail(asrt=self.assertRaises, excClass=Exception, callableObj=func, x=5)
  def test_pass4(self):
    self.assertFail(self.assertEqual, first=1, second=2)
  def test_pass5(self):
    self.assertFail(func, x=0)
  def test_pass6(self):
    self.assertFail(self.assertRaises, excClass=Exception, callableObj=func, x=5)
  def test_pass7(self):
    self.assertFail(self.assertEqual, 1, 2)
  def test_pass8(self):
    self.assertFail(func, 0)
  def test_pass9(self):
    self.assertFail(self.assertRaises, Exception, func, 5)

  def test_fail1(self):
    try: self.assertFail(asrt=self.assertEqual, first=1, second=1)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail2(self):
    try: self.assertFail(asrt=func, x=5)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail3(self):
    try: self.assertFail(asrt=self.assertRaises, excClass=ZeroDivisionError, callableObj=func, x=0)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail4(self):
    try: self.assertFail(self.assertEqual, first=1, second=1)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail5(self):
    try: self.assertFail(func, x=5)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail6(self):
    try: self.assertFail(self.assertRaises, excClass=ZeroDivisionError, callableObj=func, x=0)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail7(self):
    try: self.assertFail(self.assertEqual, 1, 1)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail8(self):
    try: self.assertFail(func, 5)
    except AssertionError: pass
    except Exception as e: raise e
  def test_fail9(self):
    try: self.assertFail(self.assertRaises, ZeroDivisionError, func, 0)
    except AssertionError: pass
    except Exception as e: raise e

if __name__ == '__main__':
  unittest.main()
