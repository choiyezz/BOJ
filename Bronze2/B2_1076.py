val = {'black': 0,
       'brown': 1,
       'red': 2,
       'orange': 3,
       'yellow': 4,
       'green': 5,
       'blue': 6,
       'violet': 7,
       'grey': 8,
       'white': 9}

col1 = str(val[input()])
col2 = str(val[input()])
col3 = val[input()]

print(int(col1 + col2) * (10 ** col3))
