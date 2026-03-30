from sklearn.linear_model import LinearRegression
import numpy as np

#step1 data set 
x = np.array([[500], [1000], [1500], [2000]])
y = np.array([100, 200, 300, 400])

#step2 create model
model=LinearRegression()

#step3 train model
model.fit(x,y)

# Step 4: Take input from user
size = float(input("Enter house size (in sq ft): "))

# Step 5: Convert input into proper format
new_size = np.array([[size]])

# step 6 :predict the output 
predicted_price=model.predict(new_size)

# Step 7: Output
print("Predicted price:", predicted_price[0])