# Coursera Algorithm Part II
# The script for Q3 of week 1 PA
# Author: Chao Zhang

# I don't implemented with heap, instead I used list and sort every time, since I
# have no time to figure out to update the heap entry using heapq
#

from __future__ import division
import random

def read_edges(raw_data, node_set):
########################################################################
#  The edge data has the format                                        #
#  node 1 number, node 2 number, edge cost, there would be a new line  #
#  appending to the last. so it has to be stripped                     #
########################################################################
    with open('%s' % raw_data, 'r') as data_content:
        # skip the first line
        data_content.readline()
        # read the raw data and 
        for edge_data in data_content.readlines():
            # parse the node, edge info
            edge_details = edge_data.rsplit(" ")
            node_one = Node(edge_details[0])
            node_two = Node(edge_details[1])
            new_edge = Edge(node_one, node_two, int(edge_details[2].rstrip("\n")))

            for node in node_one, node_two:
                if node_set.has_key(node):
                    node_set[node].append(new_edge)
                else:
                    node_set[node] = [new_edge]

def pick_mst_edge(node_set, new_edges, edge_list, mst_edges, edge_record):
    for edge in new_edges:
        if edge not in edge_list and edge not in edge_record:
            edge_list.append(edge)

    for edge in edge_list:
        if edge.node_one not in node_set and edge.node_two not in node_set:
            edge_list.remove(edge)
            edge_record.append(edge)

    return sorted(edge_list, key=lambda edge: edge.cost)

class Node:
####################################################
#    All the node instance                         #
####################################################
    def __init__(self, node_id):
        self.node_id = node_id

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
        self.node_one = node_one
        self.node_two = node_two
        self.cost = cost

    def __repr__(self):
        return "edge detail, cost: %s, node 1: %s , node 2 : %s " % \
            (self.cost, self.node_one.node_id, self.node_two.node_id)
 
    def __eq__(self, other):
        return self.cost == other.cost and \
               ((self.node_one.node_id == other.node_two.node_id and \
                    self.node_two.node_id == other.node_one.node_id ) \
                or \
                (self.node_one.node_id == other.node_one.node_id and \
                    self.node_two.node_id == other.node_two.node_id))

if __name__ == '__main__':
    edge_list = []
    mst_edges = []
    edge_record = []
    node_set = dict()
    read_edges('edges.txt', node_set)

    # Randomly pick up a node, precobdition is the there should be at least
    # two nodes in the set
    if len(node_set) > 1:
        first_node_pair = node_set.popitem()
        first_node = first_node_pair[0]
        first_edges = first_node_pair[1]
        previous_node = first_node

    edge_list = pick_mst_edge(node_set, first_edges, edge_list, mst_edges, edge_record)
    while node_set:
        mst_edge = edge_list.pop(0)
        edge_record.append(mst_edge)
        mst_edges.append(mst_edge)

        if mst_edge.node_one not in node_set:
            deleted_node = mst_edge.node_two
        else:
            deleted_node = mst_edge.node_one
        additional_edges = (node_set.pop(deleted_node))
        edge_list = pick_mst_edge(node_set, additional_edges, edge_list, mst_edges, edge_record)

    mst_cost = 0
    for edge in mst_edges:
        mst_cost += edge.cost
    print("************************************")
    print("the total cost of mst %s" % mst_cost)
    print("************************************")
