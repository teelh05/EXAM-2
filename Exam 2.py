import pandas as pd
import statsmodels.api as sm

# Step 1: Read the spreadsheet from the specified file path
file_path = r'C:\Users\teelh05\Downloads\Restaurant Revenue.xlsx'
restaurant_data = pd.read_excel(file_path)

# Step 2: Perform multiple regressions for each specified column
# Let's define a function to perform regression and print the results
def perform_regression(x_column, y_column):
    # Add constant term to the independent variable
    x = sm.add_constant(restaurant_data[x_column])
    y = restaurant_data[y_column]
    
    # Fit the regression model
    model = sm.OLS(y, x).fit()
    
    # Print the regression results
    print(f"Regression results for {y_column} based on {x_column}:")
    print(model.summary())
    print("\n")

# Perform regression for each specified column
columns_to_compare = ['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 
                      'Average_Customer_Spending', 'Promotions', 'Reviews']
for column in columns_to_compare:
    perform_regression(column, 'Monthly_Revenue')

