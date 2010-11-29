#Michael Hernandez
#aonbyte@gmail.com
#11.27.2010
#Wrote original implementation

#Richard B. Kaufman-Lopez
#richardbkaufman@gmail.com
#2010.11.29
#Modularizing the code. Breaking it to class and functions.

#Description: Uploads an image to imgur.

import sys
import urllib
import urllib2
import base64

IMG_FILE_TYPES = ['JPEG', 'JPG', 'GIF', 'PNG', 'APNG', \
		    'TIFF', 'BMP', 'PDF', 'XCF']

class Client:
    def __init__(self, api_key):
	self.key = api_key

    def upload(self, image):
	# Check if image is actually an image
	file_type = image.upper().partition('.')[2]
	if file_type not in IMG_FILE_TYPES:
	    print image + ' is not an image'
	    sys.exit(10)

	# Read image and encode it in base64
	image_encoded = None
	try:
	    image_encoded = base64.b64encode(open(image ,'rb').read())
	except IOError:
	    print 'Cannot find: ' + image
	    sys.exit(11)

	
	# Prepare url for uploading
	url = 'http://api.imgur.com/2/upload'
	url_parameters = {'key' : self.key, 'image' : image_encoded}
	url_data = urllib.urlencode(url_parameters)
	http_request = urllib2.Request(url, url_data)
	response = urllib2.urlopen(http_request)
	output = response.read()

	# TODO: Check for error in upload

	# Succesful upload. Return output
	return output
	
	
	        
