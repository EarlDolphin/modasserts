#!/usr/bin/env python3
class myAsserts:
  def assertFail(self, asrt, *args, **kwargs):
    try: asrt(*args, **kwargs)
    except: pass
    else: raise AssertionError("Hey! This test was supposed to fail!")
