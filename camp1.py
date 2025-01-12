# txt ="hi"
# print(txt)


# fruits = ["apple","banana"]
# fruits.append("orange")
# fruits.remove("apple")
# fruits.insert(0,"Hi")
# for fruit in fruits:
#    print(f"This is a {fruit}.")
# i = 0 
#  while i < 100:
#     print(i)
#     i = 1 + 1
# print("done")

# :D  Dictionary in mobile robot
    #     A
    #    / \
    #   B   C
    #  / \    \
    # D   E    F
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': [],

}
start = 'A'
goal = 'B'
frontire = [start]
explored = set ( ) # Use a set for unique (ignore duplicate append)

print(frontire, explored)
while len(frontire) > 0:
    current = frontire.pop() #Remove and put into current varable
    print(current)

    if current == goal:
        print("Goal reach")
        break
    print(f"neighbor of {current} is {graph[current]}")
    for neighbor in graph[current]:
        frontire.append(neighbor)





