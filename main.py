import phonenumbers
from test import selvi

from phonenumbers import geocoder
ch_number = phonenumbers.parse(selvi,"ch")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(selvi ,"RO")
print(carrier.name_for_number(ch_number ,"en"))