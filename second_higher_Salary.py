import pandas as pd
import numpy as np

data = pd.DataFrame({'Id': [1,2,3,4],"salary": [150, 200, 300, 250]})
print(data)


# select second highest salary
heap = np.array()
for item in np.array(data['salary']):
    while item 
