import unittest
from foo import *

class TestTelefone(unittest.TestCase):

  def test_A_retorna_2(self):
    self.assertEqual(converte_telefone('A'), '2')

  def test_AA_retorna_22(self):
    self.assertEqual(converte_telefone('AA'), '22')

  def test_AD_retorna_23(self):
    self.assertEqual(converte_telefone('AD'), '23')
  def test_AEG_retorna_234(self):
    self.assertEqual(converte_telefone('AEG'),'234')

  def test_AI_retorna_222_333_444(self):
    self.assertEqual(converte_telefone('ABCDEFGHI'),'222333444')

  def test_10_retorna_10(self):
    self.assertEqual(converte_telefone('10'),'10')

  def test_exemplo_retorna_exemplo(self):
    self.assertEqual(converte_telefone('1-HOME-SWEET-HOME  MY-MISERABLE-JOB'),'1-4663-79338-4663  69-647372253-562')




unittest.main()