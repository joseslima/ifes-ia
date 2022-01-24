from random import randint
from math import *

class Subject:
	def __init__(self, bits, interval, mutateRate):
		self.binaryGene = []
		self.fitnessValue = 0
		self.bits = bits
		self.interval = interval
		self.mutateRate = mutateRate
		
		for i in range(self.bits):
			bit = randint(0, 1)
			self.binaryGene.append(bit)

		self.geneValue = self.getGeneValue()
		self.fitnessValue = self.getFitValue()
	
	def getGeneValue(self):
		stringBinaryGene = []
		for element in self.binaryGene:
			stringBinaryGene.append(str(element))

		return self.interval[0] + (((self.interval[1] - self.interval[0]) * int("".join(stringBinaryGene),2)) / (2**self.bits - 1))

	def getFitValue(self):
		return cos(self.geneValue) * self.geneValue + 2

	def crossover(self, i, partner):
		child = Subject(bits=self.bits, interval=self.interval, mutateRate=self.mutateRate)
