import urllib2, csv
import mechanize
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

br = mechanize.Browser()  #it's like opening a new tab in the browser
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx')

# Fill out the top form
br.select_form(nr=0)   #nr=0 get me the first form on the page 
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']   #mechanize wants the value submitted as a list
br.submit('ctl00$MainContent$btnElectionType')

# Fill out the bottom form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()   #equivelent of urllib2.urlopen(url).read() in urllib2

########## YOUR CODE HERE ##########
# Create a file and open csv writer
new_file = open('missouri_pimary_bycounty.csv', 'a')
writer = csv.writer(new_file)

# Set up BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the county-by-county table using the 'id' attribute
targeting_attributes = {'id': 'MainContent_dgrdCountyRaceResults'}
county_table = soup.find('table', targeting_attributes)

# Grab the rows from the table, represented as a list 
rows = county_table.find_all('tr')

# Loop over the rows and write the data into the csv file
for row in rows:
    names = [cell.text for cell in row.find_all('th')]
    data = [cell.text for cell in row.find_all('td')]
    writer.writerow(names)
    writer.writerow(data[::1])
    