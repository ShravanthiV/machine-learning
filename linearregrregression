import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
data = {'square_feet': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200],
        'bedrooms': [2, 2, 3, 3, 4, 4, 4, 5, 5, 5],
        'bathrooms': [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
        'price': [180000, 200000, 250000, 310000, 350000, 390000, 420000, 470000, 500000, 530000]}
df = pd.DataFrame(data)
print("Columns:\n", df.columns)
X = df[['square_feet', 'bedrooms', 'bathrooms']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
example_house = pd.DataFrame([[2400, 4, 3]], columns=['square_feet', 'bedrooms', 'bathrooms'])
price_prediction = model.predict(example_house)
print(f"Predicted price for 2400 sq ft, 4 bed, 3 bath house: ${price_prediction[0]:,.2f}")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.show()
