from matplotlib.pyplot import table
import numpy as np

table_data = [
    ['a', 'b', 'c'],
    ['aaaaaaaaaa', 'b', 'c'], 
    ['a', 'bbbbbbbbbb', 'c']
]
# status_list = ["Todo", "Doing", "Done"]

# x=np.zeros((len(status_list), 2))
# reverse_table_data = [[]]
# # for i in range(0, len(table_data)):
# #     for j in range(0, len(table_data[i])):
# #         x.append(table_data[i][j])
# #     reverse_table_data.append(x)

# print(x)
# for i in range(0, len(table_data)):
#     print(table_data[i][0])
#     np.append(x, np.array(table_data[i][0], ndmin=2), axis=0)
# print(x)

# #print(reverse_table_data)
for row in table_data:
   print("{: >20} {: >20} {: >20}".format(*row))