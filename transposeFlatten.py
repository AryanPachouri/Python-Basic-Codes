
p = list(map(int, input().split())) 
Rows=p[0]
print(Rows)
   
example_matrix = []  
for i in range(Rows):  
    single_row = list(map(int, input().split()))   
    example_matrix.append(single_row)  

print(example_matrix)
import numpy as np
my_array=np.array(example_matrix)
print(np.transpose(example_matrix))
print(example_matrix.flatten())
