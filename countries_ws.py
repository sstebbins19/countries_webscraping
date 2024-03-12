# Import Modules
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Get Data
url = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all('div', attrs={'class': 'col-md-4 country'})

# Get Headers
last_headers = [title.text.strip() for title in table[0].find_all('strong')]
headers = ['Country Name:'] + last_headers


# Create DataFrame
df = pd.DataFrame(columns = headers)


# Country Names
## [i.text.strip() for i in table[0].find_all('h3')]
# Other Data
## [i.text.strip() for i in table[0].find_all('span')]

# Add data into dataframe
for i in range(0,len(table)-1):
    indiv_names = [j.text.strip() for j in table[i].find_all('h3')]
    indiv_other = [k.text.strip() for k in table[i].find_all('span')]
    indiv_row = indiv_names + indiv_other
    df.loc[i] = indiv_row
