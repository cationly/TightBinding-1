#!/usr/bin/env python
import numpy

class TightBinding:
	"""
	Tight-binding Hamiltonian.
	The design of this class is composition.
	"""

	def __init__(self):
		"""
		"""
		self._size = 2
		self._transfer = 0.1
		self.H = None
		self.energy = None
		self.orbital= None 
		self.buildHamiltonian()
		 

	def __repr__(self):
		return self.H.__repr__()

	def buildHamiltonian(self):
		self.H = numpy.zeros((self._size,self._size))
		for i in range(self._size-1):
			self.H[i,i+1] = self._transfer
			self.H[i+1,i] = self._transfer	

	def size(self):
		s = self.H.shape
		if s[0] == s[1]:
			return s[0]
		else:
			raise ValueError("The shape of the Hamiltonian is not square.")

	def setSize(self,n):
		self._size = n
		self.buildHamiltonian()
		return self

	def setTransfer(self,t):
		self._transfer = t
		self.buildHamiltonian()	
		return self
	
