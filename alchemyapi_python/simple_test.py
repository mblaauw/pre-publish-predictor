#!/usr/bin/env python

#	Copyright 2013 AlchemyAPI
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

with open ("/03_P-PROJECTS/CollectDutchBookFeatures/data/nl_books/test_en.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')


demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
demo_url = 'http://www.npr.org/2013/11/26/247336038/dont-stuff-the-turkey-and-other-tips-from-americas-test-kitchen'
demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'
demo_text = data


#Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')  
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Entities ##')
	for entity in response['entities']:
		print('text: ', entity['text'].encode('utf-8'))
		print('type: ', entity['type'])
		print('relevance: ', entity['relevance'])
		print('sentiment: ', entity['sentiment']['type'])
		if 'score' in entity['sentiment']:
			print('sentiment score: ' + entity['sentiment']['score'])
		print('')
else:
	print('Error in entity extraction call: ', response['statusInfo'])




response = alchemyapi.language('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Language ##')
	print('language: ', response['language'])
	print('iso-639-1: ', response['iso-639-1'])
	print('native speakers: ', response['native-speakers'])
	print('')
else:
	print('Error in language detection call: ', response['statusInfo'])


