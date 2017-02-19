from selenium import webdriver 
import urllib2

driver = webdriver.Firefox()
response = urllib2.urlopen("http://quora.com")
print "response is:" , response
driver.get(response.geturl())
# To get url
print "The url is:", response.geturl()

#to get code
print "This gets the code:", response.code

# Get the Headers. 
# This returns a dictionary-like object that describes the page fetched, 
# particularly the headers sent by the server
print "The Headers are: ", response.info()

# Get the date part of the header
print "The Date is: ", response.info()['date']

# Get the server part of the header
print "The Server is: ", response.info()['server']

# Get all data
html = response.read()
print "Get all data: ", html

# Get only the length
print "Get the length :", len(html)

# Showing that the file object is iterable
for line in response:
 print line.rstrip()

# Note that the rstrip strips the trailing newlines and carriage returns before
# printing the output.
