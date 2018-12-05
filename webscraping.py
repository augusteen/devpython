# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage =  'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)

# parse the html using beautiful soup and store in variable 'soup'soup = BeautifulSoup(page, 'html.parser')
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
# print (soup)


# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')
print('Number of results', len(results))

# create and write headers to a list 
rows = [['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year end', 'Annual sales rise over 3 years',
         'Sales £000s', 'Staff', 'Comments']]
print(rows)

# loop over results
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data 
    if len(data) == 0: 
        continue
    # write columns to variables
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    year_end = data[3].getText()
    sales_rise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()
    print('Company is', company)
    # Company is Wonderfly Personalised children's books
    print('Sales', sales)
    # Sales *25,860
    company_name = data[1].find('span', attrs={'class':'company-name'}).getText()
    description = company.replace(company_name, '')
    
    # remove unwanted characters
    sales = sales.strip('*').strip('†').replace(',','')
    # go to link and extract company website
    url = data[1].find('a').get('href')
    page = urllib.request.urlopen(url)
    # parse the html 
    soup = BeautifulSoup(page, 'html.parser')
    # find the last result in the table and get the link
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        web_page = tableRow.find('a').get('href')
    except Exception:
        web_page = None
    # write each result to rows
    rows.append([rank, company_name, web_page, description, location, year_end, sales_rise, sales, staff, comments])

print(rows)

# Create csv and write rows to output file
with open('techtrack100.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
