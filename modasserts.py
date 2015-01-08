#!/usr/bin/env python3
class myAsserts:
  def assertFail(self, asrt, *args, **kwargs):
    """
    Test a test to ensure it fails.
    <asrt> :unittest.TestCase.assert*
    """
    try: asrt(*args, **kwargs)
    except: pass
    else: raise AssertionError("Hey! This test was supposed to fail!")
