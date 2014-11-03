#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class TelNumberTree:
    def __init__(self, values):
        self._root = TreeNode(values[0], None)
        # print >> sys.stderr, values[1:]
        self._root.add_tree(values[1:])
        
    def get_root(self):
        return self._root
        
    def calc_length(self):
        return self._root.calc_length()


class TreeNode:
    def __init__(self, value, parent):
        self._parent = parent
        self._value = value
        self._children = []
        # print >> sys.stderr, type(self._value)
        # print >> sys.stderr, self._value
        assert type(self._value) == type("")
        
    def get_val(self):
        return self._value
    
    def get_children(self):
        return self._children
    
    def add_child(self, child):
        child._parent = self
        self._children.append(child)
        
    def calc_length(self):
        total_length = 1
        for c in self._children:
            total_length += c.calc_length()
        return total_length
    
    def add_tree(self, values):
        node = self
        for v in values:
            child = TreeNode(v, node)
            node.add_child(child)
            node = child

    def __str__(self):
        return str(self.get_val())
        

if __name__ == "__main__":
    # N = int(raw_input())
    telnum_trees = []
    telnums = [
        "0412578440",
        "0412199803",
        "0468892011",
        "112",
        "15",
        # "0468309302",
    ]
    # for i in xrange(N):
    for i, num in enumerate(telnums):
        telephone = num
        # telephone = raw_input()
        # print >> sys.stderr, telephone
        
        tree = filter( 
            lambda n: n.get_root().get_val() == telephone[0], 
            telnum_trees 
        )
        if tree:
            node = tree[0].get_root()
            children = node.get_children()
            for i, n in enumerate(telephone):
                print >> sys.stderr, "children: " + str("".join([ child.get_val() for child in children]))

                child_list = filter(lambda c: c.get_val() != n, children )
                if not child_list:
                    rest_tel_num = telephone[i:]
                    node.add_tree(rest_tel_num)
                    print >> sys.stderr, rest_tel_num
                    break
                else:
                    node = child_list[0]
                    children = node.get_children()
                    continue
        else:
            new_tree = TelNumberTree(telephone)
            # print >> sys.stderr, "telephone :" + str(telephone[0])
            # print >> sys.stderr, "index :" + str(i)
            telnum_trees.append(new_tree)
        
    #print >> sys.stderr, telnum_trees[0]._root._value
    #print >> sys.stderr, map(lambda t: t.calc_length(), telnum_trees)
    # node = telnum_trees[0]._root
    # while True:
    #     print >> sys.stderr, node.get_val()
    #     children = node.get_children()
    #     if not children:
    #         break;
    #     else:
    #         node = children[0]

    # print >> sys.stderr, map(lambda t: t.calc_length(), telnum_trees)
    total_length = sum(map(lambda t: t.calc_length(), telnum_trees))

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print total_length # The number of elements (referencing a number) stored in the structure.
