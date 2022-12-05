"""6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )"""
firstlist=["Java","Python","SQL"]
secondlist=["C","Cpp","NoSQL"]
firstlist.append(secondlist[0])
firstlist.append(secondlist[1])
firstlist.append(secondlist[2])
print(firstlist)