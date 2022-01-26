Explicação do Algoritmo

Algoritmos genéticos são algoritmos de otimização que simulam um processo comum na natureza, que é a evolução de uma população ao decorrer de um tempo. Na computação, a população é uma representação abstrata.
O algoritmo começa sua execução com a criação de uma população de indivíduos inicial, onde cada indivíduo é criado aleatoriamente  com diversidade suficiente para o algoritmo fazer combinações de características no decorrer da sua execução. Devem ser avaliadas as características de cada indivíduo através de algum critério, determinado pelo o que é chamada de função de aptidão ou “fitness”. A partir daí, a população passa por diversas fases, onde ocorrerão mudanças nos indivíduos e na população em geral, sendo elas:

Fase de seleção:
Nessa fase são escolhidos os melhores indivíduos de melhor qualidade, a partir da função de aptidão.

Fase de cruzamento:
Nessa fase ocorrem cruzamentos entre os indivíduos, misturando suas características (genes). 

Fase de mutação:
São selecionados indivíduos da população e seus genes são modificados.

Alguns algoritmos genéticos também utilizam do elitismo, onde o melhor indivíduo do começo da população é copiado e levado para nova população, com intenção de garantir que a população não só piore ao longo de sua evolução.

Ao final da execução das fases, é considerado o fim de uma geração. Esse processo é repetido diversas vezes, geração por geração, até que uma solução ideal seja encontrada, ou que um número predefinido de passos seja executado, ou que o algoritmo não consiga mais evoluir a sua população.

Problema

Especificação: Utilize um algoritmo genético binário para minimizar a função descrita abaixo. Minimize a função:



• Assumir que x∈[−20,+20] ; 
• Codificar x como vetor binário; 
• Utilize 16 bits para codificar cada indivíduo (x). Gere cada indivíduo aleatoriamente (bit a bit);
 • Criar uma população inicial com 10 indivíduos; 
• Usar seleção por torneio (n = 2); 
• Aplicar Crossover com taxa de 60% (Crossover de 1 ponto uniforme). Gere um randômico (r) entre [0,1], se r⩽0,60 → aplique a crossover; 
• Aplicar Mutação com taxa de 1%. Gere um randômico (r) entre [0,1], se r⩽0,01 → aplique a mutação; Isso deve ser feito a cada bit do indivíduo; 
• Usar 10 gerações e 20 gerações;
 • Utilizar elitismo;

Solução:

A solução do problema foi desenvolver um algoritmo em python que executa cada fase do algoritmo genético de forma sequencial em um loop, repetidas vezes, alterando a população inicial.

O código foi organizado da seguinte forma:

main.py

É a função principal, que inicializa toda a execução do algoritmo.

Simulator.py

É a classe responsável por fazer a simulação da evolução de uma população de indivíduos utilizando  o algoritmo genético. Essa classe recebe como entrada no seu construtor alguns atributos que serão utilizados como configuração da simulação.

Atributos:
bits: vetor binário de 16 casas.:
populationSize: tamanho da população inicial
interactions: número de vezes em que as etapas da simulação serão executadas (gerações)
crossoverRate: chance de cruzamento
mutateRate: chance de mutação


Subject.py

É a classe que representa um indivíduo da população.

Atributos:
binaryGene: Vetor binário que representa o gene do individuo
geneValue: Valor decimal do gene
fitinessValue: Aptidão do individuo

Execução:







Na função main é executada a simulação 10 vezes com o intuito de pegar a média do melhor resultado de aptidão. Nessa função é instanciada a classe Simulator, com os atributos de configuração


```
 
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
 
 

```


No simulador, o método start() inicia a execução de uma simulação. Inicialmente é criada uma população inicial, e depois é executado um loop baseado no atributo “interactions”. Em cada iteração do loop  cada fase da simulação é executada sequencialmente, sendo elas a fase de torneio, a fase de cruzamento, a fase de mutação e a fase de elitismo.

```
   def start(self):
     self.interaction = 0
 
     for i in range(self.populationSize):
       self.population.append(Subject(bits=self.bits, interval=self.interval, mutateRate=self.mutateRate ))
    
     for interaction in range(self.interactions):
       self.interaction = interaction + 1
       self.tournamentStage()
       self.crossoverStage()
       self.mutationStage()
       self.elitismStage()
      
       print("Melhor da geração: {}".format(self.interactions))
       print("Aptidão:{}".format(self.best.fitnessValue))
       print("Gene:{}".format(self.best.geneValue))
       print("")
 
     return self.best

```


Na fase de torneio são selecionados alguns indivíduos em pares aleatoriamente para competir entre si. Os indivíduos que tiverem o melhor valor de aptidão são adicionados em uma lista que será a nova população.

```
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

```

Na fase de cruzamento, os melhores da população selecionados na fase de torneio tem seus genes cruzados. Os indivíduos também são selecionados em duplas de forma aleatória. Após o cruzamento, os dois indivíduos são substituídos pelos seus filhos na população.


```
   def crossoverStage(self):
     for i in range(0, self.populationSize, 2):
       if(randint(1, 100) <= self.crossoverRate):
         value1 = randint(0, self.populationSizeMaxIndex)
         value2 = randint(0, self.populationSizeMaxIndex)
 
         toCrop = randint(1, (self.bits - 1))
 
         self.population[i] = self.crossover(toCrop,self.population[value1], self.population[value2].binaryGene)
         self.population[i+1] = self.crossover(toCrop, self.population[value2], self.population[value1].binaryGene)
    
     self.setBest()

```
Na fase de mutação os indivíduos da população são selecionados e existe a possibilidade, de forma aleatória, de ocorrer uma mudança em um dos bits de seu gene.

```
   def mutationStage(self):
     for subject in self.population:
       self.mutate(subject)
      self.setBest()
 

```
```
   def mutate(self, subject):
     for i in range(len(subject.binaryGene)):
       if(randint(1, 100) <= self.mutateRate):
         if (subject.binaryGene[i]):
           subject.binaryGene[i] = 0
         else:
           subject.binaryGene[i] = 1
 
         subject.geneValue = subject.getGeneValue()
         subject.fitnessValue = subject.getFitValue()

```

Por último, na fase de elitismo, o melhor indivíduo da população inicial é copiado e substitui o indivíduo de pior valor de aptidão da população modificada após as fases da geração. 

```
   def elitismStage(self):
     worst = self.population[0]
     worstIndex = 0
 
     for i in range(len(self.population)):
       subject = self.population[i]
       if (subject.fitnessValue > worst.fitnessValue):
         worst = subject
         worstIndex = i
 
     self.population[worstIndex] = self.best

```

Em cada iteração do loop de gerações é impresso o resultado da geração atual, mostrando o indivíduo com o gene que possui a melhor aptidão



No final da execução é impresso o resultado final, com o cálculo da média do melhor valor de aptidão após a execução de 10 simulações.



Resultados obtidos:

Entrada:

populationSize: 10
interactions: 10
crossoverRate:60
mutateRate:1

Executando as 10 simulações através dos valores que foram sugeridos no trabalho, observou-se valores bastante inconstantes, variando entre  -7 e -16.87, sendo que poucas vezes o resultado chegou a -16.87.

Executando: 10 vezes
Média: -12.40987040291858


Ao alterar os valores, aumentando o número da população, observou-se um aumento na média após a execução das 10 simulações.

Entrada:

populationSize: 50
interactions: 10
crossoverRate:60
mutateRate:1

Resultado:

Executando: 10 vezes
Média: -16.215683949677306


Entrada:

populationSize: 100
interactions: 20
crossoverRate:70
mutateRate:3

Resultado:

Executando: 10 vezes
Média: -16.85411013645299
