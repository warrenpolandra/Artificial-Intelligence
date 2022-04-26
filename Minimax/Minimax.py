class Node:
    def __init__(self, value, name):
        self.value = value
        self.left = None
        self.right = None
        self.mid = None
        self.name = name


# leaf node


leafL = Node(2, 'L')
leafM = Node(5, 'M')
leafN = Node(6, 'N')
leafO = Node(1, 'O')
leafP = Node(4, 'P')
leafQ = Node(3, 'Q')
leafR = Node(9, 'R')
leafS = Node(2, 'S')
leafT = Node(3, 'T')
leafU = Node(4, 'U')
leafV = Node(3, 'V')
leafW = Node(1, 'W')
leafX = Node(8, 'X')
leafY = Node(7, 'Y')

bodyE = Node(None, 'E')
bodyE.left = leafL
bodyE.right = leafM

bodyF = Node(None, 'F')
bodyF.left = leafN
bodyF.right = leafO

bodyG = Node(None, 'G')
bodyG.left = leafP
bodyG.right = leafQ

bodyH = Node(None, 'H')
bodyH.left = leafR
bodyH.right = leafS

bodyI = Node(None, 'I')
bodyI.left = leafT
bodyI.right = leafU

bodyJ = Node(None, 'J')
bodyJ.left = leafV
bodyJ.right = leafW

bodyK = Node(None, 'K')
bodyK.left = leafX
bodyK.right = leafY

bodyB = Node(None, 'B')
bodyB.left = bodyE
bodyB.right = bodyF

bodyC = Node(None, 'C')
bodyC.left = bodyG
bodyC.mid = bodyH
bodyC.right = bodyI

bodyD = Node(None, 'D')
bodyD.left = bodyJ
bodyD.right = bodyK

rootA = Node(None, 'A')
rootA.left = bodyB
rootA.mid = bodyC
rootA.right = bodyD


def minimax(node, is_max):

    left_val = None
    mid_val = None
    right_val = None

    if node.left is not None:
        if node.left.value is None:
            minimax(node.left, not is_max)
        else:
            print(node.left.name + ": " + str(node.left.value))
        left_val = node.left.value
    if node.mid is not None:
        if node.mid.value is None:
            minimax(node.mid, not is_max)
        else:
            print(node.mid.name + ": " + str(node.mid.value))
        mid_val = node.mid.value
    if node.right is not None:
        if node.right.value is None:
            minimax(node.right, not is_max)
        else:
            print(node.right.name + ": " + str(node.right.value))
        right_val = node.right.value

    if node.value is None:
        if is_max is True:
            if mid_val is None:
                node.value = max(left_val, right_val)
            else:
                node.value = max(left_val, mid_val, right_val)
        else:
            if mid_val is None:
                node.value = min(left_val, right_val)
            else:
                node.value = min(left_val, mid_val, right_val)

    print(node.name + ": " + str(node.value))


current_node = rootA
is_max = True

minimax(current_node, is_max)
