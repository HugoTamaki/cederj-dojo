import unittest
from foo2 import *

class TestCaixaEletronico(unittest.TestCase):

  def test_A(self):
    self.assertEqual(troco(100), '1 nota de R$100')
  def test_B(self):
    self.assertEqual(troco(50), '1 nota de R$50')
  def test_C(self):
    self.assertEqual(troco(20), '1 nota de R$20')
  def test_D(self):
    self.assertEqual(troco(10), '1 nota de R$10')
  def test_E(self):
    self.assertEqual(troco(30), '1 nota de R$10 e 1 nota de R$20')
def test_E(self):
    self.assertEqual(troco(80), '1 nota de R$50 e 1 nota de R$20 e 1 nota de R$10')













unittest.main()