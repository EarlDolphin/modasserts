#!/usr/bin/env python3
#Copyright (c) 2015, EarlDolphin
#All rights reserved.
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#* Redistributions of source code must retain the above copyright notice, this
#list of conditions and the following disclaimer.
#* Redistributions in binary form must reproduce the above copyright notice,
#this list of conditions and the following disclaimer in the documentation
#and/or other materials provided with the distribution.
#* Neither the name of modasserts nor the names of its
#contributors may be used to endorse or promote products derived from
#this software without specific prior written permission.
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
from modasserts import mod_asserts

def ensure_fails(testObj, *args, **kwargs):
  """
  Purpose: Test that a mod_asserts DidNotFailError is raised when a test given to assertFail does not fail
  Method: Call assertFail on a test (contained in the kwargs) and raise if a mod_asserts.DidNotRaiseError is not raised
  """
  try: testObj.assertFail(*args, **kwargs)
  except mod_asserts.DidNotFailError: pass # What we want
  except Exception as e: raise e
  else: raise AssertionError()

class TestTheTests(unittest.TestCase, mod_asserts):
  def setUp(self):
    self.func = (lambda x: 1/x)

  def test_pass1(self):
    self.assertFail(asrt=self.assertEqual, first=1, second=2)
  def test_pass2(self):
    self.assertFail(asrt=self.func, x=0)
  def test_pass3(self):
    self.assertFail(asrt=self.assertRaises, excClass=Exception, callableObj=self.func, x=5)
  def test_pass4(self):
    self.assertFail(self.assertEqual, first=1, second=2)
  def test_pass5(self):
    self.assertFail(self.func, x=0)
  def test_pass6(self):
    self.assertFail(self.assertRaises, excClass=Exception, callableObj=self.func, x=5)
  def test_pass7(self):
    self.assertFail(self.assertEqual, 1, 2)
  def test_pass8(self):
    self.assertFail(self.func, 0)
  def test_pass9(self):
    self.assertFail(self.assertRaises, Exception, self.func, 5)

  def test_fail1(self):
    ensure_fails(self, asrt=self.assertEqual, first=1, second=1)
  def test_fail2(self):
    ensure_fails(self, asrt=self.func, x=5)
  def test_fail3(self):
    ensure_fails(self, asrt=self.assertRaises, excClass=ZeroDivisionError, callableObj=self.func, x=0)
  def test_fail4(self):
    ensure_fails(self, self.assertEqual, first=1, second=1)
  def test_fail5(self):
    ensure_fails(self, asrt=self.func, x=5)
  def test_fail6(self):
    ensure_fails(self, asrt=self.assertRaises, excClass=ZeroDivisionError, callableObj=self.func, x=0)
  def test_fail7(self):
    ensure_fails(self, self.assertEqual, 1, 1)
  def test_fail8(self):
    ensure_fails(self, self.func, 5)
  def test_fail9(self):
    ensure_fails(self, self.assertRaises, ZeroDivisionError, self.func, 0)

if __name__ == '__main__':
  unittest.main()
