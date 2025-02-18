from typing import List, Union, Any, Dict, Set
from copy import deepcopy, copy 

graph_t = Dict[str, Set[str]]


class Graph:
    
    def __init__(self) -> None:
        self.graph : graph_t = dict()

    def add_node(self,variable:str) -> None:
        pass 

    def add_edge(self, node_a:str, node_b:str) -> None:
        pass 

    def remove_node(self,) -> str:
        pass 

    def remove_edge(self, node_1:str, node_2:str) -> str:
        pass 