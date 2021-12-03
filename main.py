# coding=utf-8
import sys
from AStar import *

def main():
    if len(sys.argv) == 6:

        inputMap = open(sys.argv[1], 'r')

        map = []
    
        for line in inputMap:
            mapLine = []
            for node in line:
                if( node != "\n" and node != " "):
                    mapLine.append(node)
            map.append(mapLine)

        
        startNode = tuple([int(sys.argv[2]), int(sys.argv[3])])
        goal = tuple([int(sys.argv[4]), int(sys.argv[5])])


        print("Mapa de Entrada:")
        ## IMPRIMIR MAPA
        
        star = AStar(map)

        path = star.getPath(startNode, goal)
        
        print("Mapa com o melhor caminho:")
        ##Imprimir mapa com o melhor caminho

    else:
        print("Inputs inválidos")

main()
