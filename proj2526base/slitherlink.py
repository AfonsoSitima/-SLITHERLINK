#!/usr/bin/env python3
# slitherlink.py: Template para implementação do projeto de Inteligência Artificial 2025/2026.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

import random, copy
from sys import stdin
from collections import defaultdict

import utils
from utils import *

from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)

UNKNOWN   = 0
ACTIVE    = 1
FORBIDDEN = 2

class SlitherlinkState:
    state_id = 0


    def __init__(self, board):
        self.board = board
        self.id = SlitherlinkState.state_id
        SlitherlinkState.state_id += 1
    
    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe

class Board:
    """Representação interna de um tabuleiro de Slitherlink."""
    #não sei se podemos fazer isto
    def __init__(self, rows:int, columns:int, cells:dict):
        self.rows = rows
        self.columns = columns
        self.cells = cells   
        #talvez criar parametro arestas
        self.h_edges= [[UNKNOWN for _ in range(self.columns)] for _ in range(self.rows + 1)]
        self.v_edges = [[UNKNOWN for _ in range(self.columns + 1)] for _ in range(self.rows)]

        #METER AQUI UMAS EDGES PARA FAZER TESTE


    def adjacent_cell(self, cell:tuple) -> list:
        """Devolve uma lista das células que fazem
        fronteira com a célula enviada no argumento"""
        
        #TODO
        #as diagonais são adjacentes ? 
        adjacent_cells = []
        row, col = cell
        
        if row > 0:
            adjacent_cells.append((row - 1, col))
        if row < self.rows - 1:
            adjacent_cells.append((row + 1, col))
        
        if col > 0:
            adjacent_cells.append((row, col - 1))
        if col < self.columns - 1:
            adjacent_cells.append((row, col + 1))



        return adjacent_cells

        """ 
        def change_state(self):
        #só para teste
            self.v_edges[0][0] = ACTIVE
            self.h_edges[0][0] = ACTIVE

            self.v_edges[0][1] = FORBIDDEN
            self.h_edges[0][0] = FORBIDDEN
         """


    def get_cell_edges(self, row:int, column:int) -> list:
        """Devolve os arestas da célula enviada no argumento"""
        #TODO
        edges = []

        #funcional me princípio
        ##ordem correta 
        # [cima, lado dir, baixo, lado esq]
        edges.append(self.h_edges[row][column])
        edges.append(self.v_edges[row][column + 1])

        edges.append(self.h_edges[row + 1][column])
        edges.append(self.v_edges[row][column])
        print(edges)
        return edges
        

        

    def get_active_edges(self, row:int, column:int) -> list:
        """Devolve o número de arestas ativas"""
        #TODO
        pass


    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 pipe.py < test-01.txt

            > from sys import stdin
            > line = stdin.readline().split()
        """
        cells = {}
        rows = 0
        columns = 0
        while True:
            line = stdin.readline().split()
            if not line:
                break
            columns = 0
            for char in line:
                match char:
                    case '0' | '1' | '2' | '3':
                        cells[(rows, columns)] = int(char)
                        columns += 1
                    case '.':
                        columns += 1
            rows += 1
        print(cells)
        return Board(rows, columns, cells)

    # TODO: outros metodos da classe

class Slitherlink(Problem):
    def __init__(self, board: Board, gui=None):
        """O construtor especifica o estado inicial."""
        # TODO
        pass


    def actions(self, state: SlitherlinkState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass


    def result(self, state: SlitherlinkState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: SlitherlinkState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas de acordo com as regras do problema."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    


if __name__ == "__main__":
    board = parsed_board = Board.parse_instance()
    print(board.adjacent_cell((0, 0)))
    print(board.adjacent_cell((2, 1)))
    board.change_state()

    print(f"VERTICAIS : {board.v_edges}")
    print(f"HORIZONTAIS : {board.h_edges}")
    board.get_cell_edges(0,0)


    #TODO:
    # Ler o ficheiro do standard input,

    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass







