from jinja2 import Template
import pandas as pd

# Load template and customer segment
with open('emails/email_template.html') as file:
    template = Template(file.read())

# Generate personalized emails
segment = pd.read_csv('data/emea_retail_high_engagement.csv')
for _, row in segment.iterrows():
    email_content = template.render(CompanyName=row['company_name'], Industry=row['industry'], Region=row['region'])
    with open(f'emails/email_{row["customer_id"]}.html', 'w') as file:
        file.write(email_content)
print("Emails generated in 'emails/' directory")
