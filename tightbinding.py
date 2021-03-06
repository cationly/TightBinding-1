#!/usr/bin/env python
import numpy

class TightBinding:
	"""
	Tight-binding Hamiltonian.
	"""
	def __init__(self,size=2,transfer=0.1,periodic=False):
		"""
		"""
		self.__size = size
		self.__transfer = transfer
		self._isPeriodic = False
		self.H= None
		self.sortlist= None
		self.eigen= None
		self.orbital= None 
		self.buildHamiltonian()
		self.needsDiag = True
		 
	def __repr__(self):
		return self.H.__repr__()

	def energy(self,index):
		if index < 0 or index >= self.__size:
			raise ValueError("index is out of array bounds.")
		elif self.needsDiag:
			self.diagonalize()
		return self.eigen[self.sortlist[index]]

	def buildHamiltonian(self):
		self.H = numpy.zeros((self.__size,self.__size))
		for i in range(self.__size-1):
			self.H[i,i+1] = self.__transfer
			self.H[i+1,i] = self.__transfer	
		if self._isPeriodic:
			self.H[0,self.__size-1] = self.__transfer
			self.H[self.__size-1,0] = self.__transfer
		self.needsDiag = True

	def size(self):
		s = self.H.shape
		if s[0] == s[1]:
			return s[0]
		else:
			raise ValueError("The shape of the Hamiltonian is not square.")

	def diagonalize(self):
		self.eigen,self.orbitals = numpy.linalg.eig(self.H)
		self.sortlist = self.eigen.argsort()
		self.needsDiag = False

	def setSize(self,n):
		self.__size = n
		self.buildHamiltonian()
		return self

	def setTransfer(self,t):
		self.__transfer = t
		self.buildHamiltonian()	
		return self
	
	def setPeriodic(self):
		if not self._isPeriodic:
			self._isPeriodic = True
			# This Hamiltonian has changed
			#  build the new Hamiltonian
			self.buildHamiltonian()	
		# else
			# The Hamiltonian is unchanged so do nothing

	def unsetPeriodic(self):
		if self._isPeriodic:
			self._isPeriodic = False
			# The Hamiltonian has changed so rebuild
			self.buildHamiltonian()
		# else
			# do nothing


