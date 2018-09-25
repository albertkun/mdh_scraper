## imports
import lxml, json, csv, requests
from lxml import html

## require:
## pip install lxml, requests


## trying objectify to turn xml to python class
## https://lxml.de/objectify.html
from lxml import etree
from lxml import objectify

## ref: https://stackoverflow.com/questions/29919753/
## trying html soupparser
import lxml.html.soupparser

## workon webscraper


## variables
frameworks =[]                              #for framework data 
cms = []                                    #for cms data
widgets = []                                #for widget data
webserver = []                              #for webserver data
the_target = "sample_data.html"               #the target html file
target_output = "sample_data.csv"               #the output csv file

## sub-functions
def set_object(object_name,key,value):
    object_name.update({key:value})


def set_defaults(target_array,value):
    if len(target_array)==0:
        msg = value+" not found"
        target_array.append(msg)
        print msg

# with open(target_output) as f:
#     reader = csv.reader(f)
#     for booking_data in reader:
#         url_data = {}

def node_checker(tree,the_node):
    target_node = [node.text_content() for node in tree.xpath(the_node)]
    # print target_node
    print target_node

# C:\Users\akocha\projects\mdh_scraper\sb_data.html
## main function
def __main__():
    print "hello"
    with open(the_target, "r") as f:
        page = f.read()
        tree = lxml.html.soupparser.fromstring(page)
        # p = tree.xpath('//p')
        # node_checker(tree,"//*[@class='bookingNumber']")

    # for elem in tree.xpath("//*[@class='bookingNumber']"):
    for elem in tree.xpath("//p"):
        result = elem.text + ''.join(lxml.html.tostring(e, pretty_print=True) for e in elem)
        print result        

        # node_checker(tree,"//img")

        # print the_p



## run the main function here
__main__()