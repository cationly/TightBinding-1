#!/usr/bin/env python
import unittest
from tightbinding import TightBinding


class TightBinding_Unit(unittest.TestCase):

	def setUp(self):
		self.TB = TightBinding()

	def tearDown(self):
		pass

	def test_Size(self):
		self.TB = TightBinding()
		self.TB.setSize(2)
		self.assertEqual(self.TB.size(),2)
		self.assertEqual(self.TB.H.shape,(2,2))
		self.TB.setSize(3)
		self.assertEqual(self.TB.H.shape,(3,3))
		self.TB.setSize(20).setTransfer(0.2)
		self.assertEqual(self.TB.H.shape,(20,20))

	def test_Transfer(self):
		self.TB = TightBinding()
		self.TB.setSize(2).setTransfer(0.25)
		self.assertAlmostEqual(self.TB.H[1,0],0.25)
		self.assertAlmostEqual(self.TB.H[0,1],0.25)
		self.TB.setTransfer(0.4)
		self.assertAlmostEqual(self.TB.H[1,0],0.4)
		self.assertAlmostEqual(self.TB.H[0,1],0.4)
		self.TB.setSize(10).setTransfer(1.1)
		self.assertAlmostEqual(self.TB.H[1,0],1.1)

	def test_Eigen(self):
		self.TB = TightBinding()
		self.TB.setSize(2).setTransfer(0.1)
		self.assertAlmostEqual(self.TB.energy[0],-0.1)
		self.assertAlmostEqual(self.TB.energy[1],0.1)
		


if __name__=='__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TightBinding_Unit)
	unittest.TextTestRunner(verbosity=2).run(suite)
	

