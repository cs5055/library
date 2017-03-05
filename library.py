#codedby cs5055
import requests
from bs4 import BeautifulSoup 
id = raw_input('Enter id: ')
params = {'__VIEWSTATE':'/wEPDwUKLTM1NzczNTkxNw9kFgJmD2QWAgIBD2QWAgIDD2QWJAIDDw8WAh4HVmlzaWJsZWhkZAIFDw8WAh8AaGRkAgcPDxYCHwBoZGQCCQ8PFgIfAGhkZAILDw8WAh8AaGRkAg0PDxYCHwBoZGQCDw8PFgIfAGhkZAIRDw8WAh8AaGRkAhMPDxYCHwBoZGQCFQ8PFgIfAGhkZAIXDw8WAh8AaGRkAhkPDxYCHwBoZGQCGw8PFgIfAGhkZAIdDzwrAAsAZAIfDw8WAh8AaGRkAiEPPCsACwBkAiMPDxYCHwBoZGQCJQ88KwALAGRkMSxw6dKF1XbXMbOcFTso6csxYAw=','__EVENTVALIDATION':'/wEWAwKO1aEbAvTZiLYOAtaW9bIDiZAxtbxnxVjqL9fHHYjbRBJBA14=','ctl00$CPHmaster$txtMemcd':id,'ctl00$CPHmaster$btnsearch':'Search Member'}
r = requests.post("http://webopac.cit.ac.in/memberstatus.aspx",data=params)
soup = BeautifulSoup(r.text,'lxml')
member_name = soup.find('span',id="ctl00_CPHmaster_lblmemname").text.strip()
member_code = soup.find('span',id="ctl00_CPHmaster_lblmemcd").text.strip()
member_dept = soup.find('span',id="ctl00_CPHmaster_lbldept").text.strip()
member_cat = soup.find('span',id="ctl00_CPHmaster_lblcat").text.strip()
member_due = soup.find('span',id="ctl00_CPHmaster_lbldue").text.strip()
member_item = soup.find('span',id="ctl00_CPHmaster_lblissued").text.strip()
table = soup.find('table',id="ctl00_CPHmaster_DgIssued")
print('Member name: '+member_name+' | Member code: '+member_code+'\nMember dept: '+member_dept+'\n'+'Category: '+member_cat+' | Overdue: '+member_due+' | Issue item: '+member_item)
print('\nBook List: \n')
if member_item == '': 
	print('No books issued')
else:
	rows = table.find_all('tr')[1:]
	for tr in rows:
		cols = tr.find_all('td')
		for td in cols:
			print td.text
		print('')
