from simulator import Simulator

def main():
	execs = 10
	aptSum = 0

	for i in range(execs):
		simulator = Simulator(bits=16, interval=[-20, 20], populationSize=100, interactions=20, crossoverRate=75, mutateRate=3)
		best = simulator.start()
		aptSum += best.fitnessValue
	
	
	print("Executando: {} vezes".format(execs))
	print("Média da melhor aptidão: {}".format(aptSum/execs))


main()

