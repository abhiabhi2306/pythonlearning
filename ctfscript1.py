import urllib2
import requests


print ('Python script by abhiabhi2306 to obtain the flag in graffeectf ')

#making request to fetch the data

resp1 = urllib2.urlopen('http://webchal.thehackergiraffe.com/timebomb/part1')
resp2 = urllib2.urlopen('http://webchal.thehackergiraffe.com/timebomb/part2')
resp3 = urllib2.urlopen('http://webchal.thehackergiraffe.com/timebomb/part3')
resp4 = urllib2.urlopen('http://webchal.thehackergiraffe.com/timebomb/part4')
resp5 = urllib2.urlopen('http://webchal.thehackergiraffe.com/timebomb/part5')

#all the responses are concatinated.

key = resp1.read()+resp2.read()+resp3.read()+resp4.read()+resp5.read()

#the final url is given

final_url="http://webchal.thehackergiraffe.com/timebomb/submit"
payload = {'key':key}

#the payload (key=key) is posted the the URL

response = requests.post(final_url, data=payload)

#the response is printed
print(response.text)
print(response.status_code, response.reason) 



