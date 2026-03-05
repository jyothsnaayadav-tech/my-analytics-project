import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("✅ pandas version:", pd.__version__)
print("✅ numpy version:", np.__version__)
print("✅ matplotlib version:", plt.matplotlib.__version__)
print("✅ scikit-learn imported successfully")
print("\n🎉 ALL DATA SCIENCE PACKAGES WORKING!")

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

print("\n📊 Sample Data:")
print(data)