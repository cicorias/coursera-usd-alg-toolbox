from unittest import TestCase
from max_pairwise_product import max_pairwise_product



class MainTest(TestCase):
  def test_simple(self):
    input_str = '1 2 3'
    input_numbers = [int(x) for x in input_str.split()]

    actual = max_pairwise_product(input_numbers)

    self.assertEqual(6, actual, '123 should be 6')

  def test_simple1(self):
    input_str = '7 5 14 2 8 8 10 1 2 3'
    input_numbers = [int(x) for x in input_str.split()]

    actual = max_pairwise_product(input_numbers)

    self.assertEqual(140, actual, 'should be 140') 
