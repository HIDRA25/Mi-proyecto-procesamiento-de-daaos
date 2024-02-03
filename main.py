import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edades = data['age']

import numpy as np

edades_array = np.array (edades)

promedio_edad = np.mean(edades_array)
promedio_redondeado = round(promedio_edad,3)
print(promedio_redondeado)
