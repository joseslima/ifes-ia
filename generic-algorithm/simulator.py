from subject import Subject
from random import randint
from copy import copy
from math import *


class Simulator:
    population = []

    def __init__(self, bits, interval, populationSize, interactions, crossoverRate, mutateRate):
      self.bits = bits
      self.interval = interval
      self.populationSize = populationSize
      self.interactions = interactions
      self.crossoverRate = crossoverRate
      self.mutateRate = mutateRate
      self.populationSizeMaxIndex = populationSize - 1
      self.best = None

    def crossover(self, i, subject, partner):
      child = Subject(bits=subject.bits, interval=subject.interval, mutateRate=subject.mutateRate)

      child.binaryGene[:i] = subject.binaryGene.copy()
      child.binaryGene[i:] = partner[i:].copy()
      
      child.geneValue = subject.getGeneValue()
      child.fitnessValue = subject.getFitValue()
      return child
            
    def mutate(self, subject):
      for i in range(len(subject.binaryGene)):
        if(randint(1, 100) <= self.mutateRate):
          if (subject.binaryGene[i]):
            subject.binaryGene[i] = 0
          else:
            subject.binaryGene[i] = 1

          subject.geneValue = subject.getGeneValue()
          subject.fitnessValue = subject.getFitValue()
          
    def setBest(self):
      if (self.best == None):
        self.best = self.population[0]
            
      for subject in self.population:
        if (self.best.fitnessValue > subject.fitnessValue):
          self.best = copy(subject)

    def tournamentStage(self):
      result = []

      for i in range(self.populationSize):
        subject1 = self.population[randint(0, self.populationSizeMaxIndex)]
        subject2 = self.population[randint(0, self.populationSizeMaxIndex)]

        if(subject1.fitnessValue > subject2.fitnessValue):
            result.append(subject2)
        else:
          result.append(subject1)
      
      self.population = result

      self.setBest()


    def crossoverStage(self):
      for i in range(0, self.populationSize, 2):
        if(randint(1, 100) <= self.crossoverRate):
          value1 = randint(0, self.populationSizeMaxIndex)
          value2 = randint(0, self.populationSizeMaxIndex)

          toCrop = randint(1, (self.bits - 1))

          self.population[i] = self.crossover(toCrop,self.population[value1], self.population[value2].binaryGene)
          self.population[i+1] = self.crossover(toCrop, self.population[value2], self.population[value1].binaryGene)
      
      self.setBest()

    def mutationStage(self):
      for subject in self.population:
        self.mutate(subject)
  
      self.setBest()

    def elitismStage(self):
      worst = self.population[0]
      worstIndex = 0

      for i in range(len(self.population)):
        subject = self.population[i]
        if (subject.fitnessValue > worst.fitnessValue):
          worst = subject
          worstIndex = i

      self.population[worstIndex] = self.best

    
    def binary_array_to_decimal(self, binary_array):
      binary_string = "".join(str(e) for e in binary_array)
      return int(binary_string, 2)

    def print_population(self, population):
      i = 0
      for p in population:
        print("----------------------------------------------------------")
        print("| {:02d} | Apt: {} | Gene: {}".format(i, p.fitnessValue, p.geneValue))
        i += 1

    def print_phase_result(self, n, phase, population):
      print("================ [ FASE {}: {} ] ==================".format(n, phase))
      print_population(population)
      print("")

    def print_best_subject(self, population, generation):
      min = inf
      best_subject = None

      for subject in population:
          if subject.fitnessValue <= min:
              best_subject = subject
              min = subject.fitnessValue

      print("================ [ Melhor da geracao: {} ] ================".format(generation))
      print("| Apt: {} | Gene: {}".format(best_subject.fitnessValue, best_subject.geneValue))
      print("")

    def start(self):
      gen = 1

      for i in range(self.populationSize):
        self.population.append(Subject(bits=self.bits, interval=self.interval, mutateRate=self.mutateRate ))

      for interaction in range(self.interactions):
        self.tournamentStage()
        self.crossoverStage()
        self.mutationStage()
        self.elitismStage()
        print(gen)
        self.print_best_subject(self.population, gen)

        gen += 1
      #return
