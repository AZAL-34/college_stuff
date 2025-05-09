# this doesn't work
import pandas as pd

d = {
    "products":["Jacket", "Pant", "Jumper", "Boot", "Belt", "Jacket", "Pant", "Jumper", "Belt"],
    "colours":["blue", "blue", "blue", "green", "blue", "green", "green", "green", "red"],
    "customer_price":[2345.89, 2390.50, 1820.00, 3100.00, 1784.50, 2545.89, 2590.50, 2220.00, 2084.50],
    "non_customer_price":[2445.89, 2495.50, 1980.00, 3400.00, 1921.00, 2645.89, 2655.50, 2140.00, 2190.00]
}
product_prices = pd.DataFrame(d)

x = product_prices.groupby("products")["customer_price", "non_customer_price"].mean()
print(x)