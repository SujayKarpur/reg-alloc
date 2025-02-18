from typing import List, Union, Any, Dict, Set, Tuple
from copy import deepcopy, copy 

graph_t = Dict[str, Set[str]]


class Graph:
    """Interference graph data structure"""
    def __init__(self) -> None:
        """construct a new interference graph"""
        self.graph : graph_t = dict()
    
    def __repr__(self) -> str:
        """display interference graph as a dictionary"""
        return repr(self.graph)

    def has_node(self, variable:str) -> bool:
        """check if variable exists in the interference graph"""
        return variable in self.graph  

    def has_edge(self, node_1:str, node_2:str) -> bool:
        """check if two variables exist simultaneously"""
        if not self.has_node(node_1):
            return False 
        return node_2 in self.graph[node_1] 

    def add_node(self,variable:str) -> None:
        """add new variable to the interference graph"""
        self.graph[variable] = set() 

    def add_edge(self, node_a:str, node_b:str) -> None:
        """"""
        if not self.has_node(node_a):
            self.add_node(node_a)
        if not self.has_node(node_b):
            self.add_node(node_b)
        self.graph[node_a].add(node_b)

    def remove_node(self, variable:str) -> str:
        """remove variable from interference graph"""
        if not self.has_node(variable):
            return None 
        return self.graph.pop(variable) 

    def remove_edge(self, node_1:str, node_2:str) -> int:
        """return -1 on failure"""
        if not self.has_edge(node_1, node_2):
            return -1 
        self.graph[node_1].remove(node_2)
        return 0   
    
    def degree(self, node) -> int:
        """return the degree of a node"""
        if not self.has_node(node):
            return -1 
        return len(self.graph[node])
    
    def nodes(self) -> set:
        """return all live variables""" 
        return set(self.graph.keys)