from simulator import Simulator

def main():
	print("OPA")
	simulator = Simulator(bits=16, interval=[-20, 20], populationSize=10, interactions=10, crossoverRate=60, mutateRate=1)
	simulator.start()

main()

