import math
import sys

input = sys.stdin.readline

tree = {}

input_list = []

while True:
    try:
        a =int(input())
        input_list.append(a)
    except:
        break

input_len = len(input_list)

root = input_list[0]

tree[root] = [-1, -1]

parent = root

grand_parent = math.inf

parent_node = {root:0}

for i in range(1, input_len):
    node = input_list[i]
    sw = 0
    
    if node > grand_parent:
        while True:
            print(tree, parent_node,node, parent, grand_parent)
            print()
            if tree[root][1] == -1:
                if grand_parent == root and root < node:
                    parent = root
                    tree[grand_parent][1] = node
                    break
                elif grand_parent > node and parent < node:
                    tree[parent][1] = node
                    break
            parent = parent_node[parent]
            grand_parent = parent_node[grand_parent]
    elif node > parent:
        tree[parent][1] = node
    elif node < parent:
        tree[parent][0] = node
    
    tree[node] = [-1, -1]
    parent_node[node] = parent
    grand_parent = parent
    parent = node

print(tree)