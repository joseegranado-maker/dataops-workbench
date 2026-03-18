import sys
import pandas as pd

print("Python:", sys.version)
print("Executable:", sys.executable)
print("Pandas:", pd.__version__)

df = pd.DataFrame({"Category": ["A", "B", "C"], "Value": [10, 20, 15]})
print(df)
