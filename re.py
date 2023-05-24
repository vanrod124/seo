import re

def generate_seo_url(title):
    title = title.lower()
    title = re.sub(r'\s+', '-', title)
    title = re.sub(r'[^\w-]', '', title)
    return title

blog_title = "My First Blog Post!"
seo_url = generate_seo_url(blog_title)
print(seo_url)  # Outputs: my-first-blog-post

import pandas as pd

# Load the data
data = pd.read_csv('website_data.csv')

# Calculate the average number of visitors
average_visitors = data['visitors'].mean()
print(f'Average number of visitors: {average_visitors}')

# Calculate the average number of page views
average_page_views = data['page_views'].mean()
print(f'Average number of page views: {average_page_views}')

# Calculate the average bounce rate
average_bounce_rate = data['bounce_rate'].mean()
print(f'Average bounce rate: {average_bounce_rate}')

# Find the date with the highest number of visitors
max_visitors_date = data.loc[data['visitors'].idxmax(), 'date']
print(f'Date with highest number of visitors: {max_visitors_date}')

