'''
Created on 27 Sep 2015

@author: matt
'''
import logging
import atws

from suds.cache import ObjectCache

from atws.connection import get_zone_url
from atws.connection import connect
from atws.query import Query
import atws.wrapper

from passwords import password,username

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

atws.connection.REQUEST_TRANSPORT_TYPE = False
atws.connection.REQUEST_TRANSPORT_TYPE = True

ticket_id_with_600_ticket_notes = 377506
query = Query('TicketNote')
query.WHERE('TicketID', query.Equals, ticket_id_with_600_ticket_notes)
print query
query.minimum_id = 213434
print query
query.minimum_id = 1324343
print query
query.reset()
query = Query('TicketNote')
query.WHERE('TicketID', query.Equals, ticket_id_with_600_ticket_notes)

url = get_zone_url(username)
print url
# suds plugins example... not required
oc = ObjectCache(hours=1)

at = connect(username=username,password=password,cache=oc)

version = at.GetWsdlVersion() 
print version


# tested using notes on a specific ticket to make my life easy
at = atws.wrapper.connect(url=url,username=username,password=password)



def get_tn():
    tn = at.new('TicketNote')
    tn.Title = 'test1'
    tn.Description = 'test1'
    tn.Publish = 1
    tn.NoteType = 13 
    tn.TicketID = ticket_id_with_600_ticket_notes
    return tn
tns = [get_tn() for i in xrange(201)]
print 'creating ticket notes:',len(tns)

results = at.create(tns)
assert len(results) == 201, 'result length (%s) is not 201' % results
ticket_notes = at.query(query)
assert len(ticket_notes) > 500, 'less than 500 ticket notes received (%s)' % len(ticket_notes)
ticket_notes2 = at.query(query.get_query_xml())
assert len(ticket_notes2) == 500,'a text based query should only return the first 500 results'




quit()
#ticket 377506


quit()