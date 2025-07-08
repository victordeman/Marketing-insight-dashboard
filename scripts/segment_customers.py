import pandas as pd
import sqlite3

# Load customer data
df = pd.read_csv('data/customers.csv')
conn = sqlite3.connect('data/customers.db')
df.to_sql('customers', conn, if_exists='replace', index=False)

# Query and refine segment
query = "SELECT * FROM customers WHERE region = 'EMEA' AND industry = 'Retail' AND email_open_rate > 20"
segment = pd.read_sql_query(query, conn)
segment.to_csv('data/emea_retail_high_engagement.csv', index=False)
print("Segmented audience saved to 'emea_retail_high_engagement.csv'")
