# Coursera Algorithm Part II
# The script for Q3 of week 1 PA
# Author: Chao Zhang

from __future__ import division
import heapq

def read_edges(raw_data, edge_heap, node_set):
    with open('%s' % raw_data, 'r') as data_content:
        # skip the first line
        data_content.readline()
        # read the raw data and 
        for edge_data in data_content.readlines():
            # parse the node, edge info
            edge_details = edge_data.rsplit(" ")
            node_one = Node(edge_details[0])
            node_two = Node(edge_details[1])
            new_edge = (node_one, node_two, int(edge_details[2].rstrip("\n"))) 
            # the nodes add the edge to its adjacency edge list 
            node_one.add_edge(new_edge)
            node_two.add_edge(new_edge)
            # push the edge to the heap
            heapq.heappush(edge_heap, new_edge)
            node_set.add(node_one)
            node_set.add(node_two)

class Node:
####################################################
#    All the node instance would have kept the     #
#  adjacency list which next to it                 #
####################################################
    def __init__(self, node_id):
        self.node_id = node_id
        self.ajacency_list=[]

    def add_edge(self, new_edge):
        self.ajacency_list.append(new_edge)

    def __repr__(self):
        return "node id: %s" % self.node_id         

    def __eq__(self, other):
        return self.node_id == other.node_id

    def __hash__(self):
        return hash(self.node_id)

class Edge:
####################################################
#    All the edge instance would have kept the     #
#  cost of the edge and its two ending node id     #
####################################################
    def __init__(self, node_one, node_two, cost):
        self.node_one = node_one.id
        self.node_two = node_two.id
        self.cost = cost

    def __repr__(self):
        return "edge detail, cost: %s, node 1: %s , node 2 : %s " % (self.cost, self.node_one, self.node_two)

    # for the use of heapq
    def __lt__(self, other):
        return self.cost < other.cost
 
if __name__ == '__main__':
    #initialize the 
    edge_list = []
    node_set = set() 
    read_edges('edges.txt', edge_list, node_set)

    while len(edge_list) > 0:
        top_edge = heapq.heappop(edge_list)
        print(top_edge) 
