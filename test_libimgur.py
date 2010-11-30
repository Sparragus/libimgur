# Michael Hernandez
# aonbyte@gmail.com
# 11.27.2010
# Wrote original implementation

# Richard B. Kaufman-Lopez
# richardbkaufman@gmail.com
# 2010.11.29 - 00:30
# Created libimgur.py. Modularizing the code. Breaking it to classes and functions.
# 2010.11.29 - 15:00
# Created test_libimgur.py. Added basic functionality. Added command line interface.



# Description: Tests libimgur
# Usage: python test_libimgur.py [-h] [--vB] image

import sys
import getopt
import libimgur
import pyperclip
from xml.dom import minidom

# API Key provided by Alan@imgur.com
api_key = '02b62fd8f1d5e78321e62bb42ced459e'
    
# Copies text to the clipboard
def copy_to_clipboard(some_string):
    if type(some_string) is not str
        return
    pyperclip.setcb(some_string)

# Function: get_image_link
#
# Returns: 
# image link
#
# Parameters: 
# result = Output from imgur.upload(image)
#
# Return example:
# 'http://i.imgur.com/hdJ2S.png'
def get_image_link(imgur_result):
    xml_doc = minidom.parse(imgur_result)
    original = str(xmldoc.getElementsByTagName('original')[0].toxml())
    return original[10:-11]

# Returns: vBulletin code for posting in a vBulletin forum.
def vBulletin( image_original_link, image_large_link = None ): #aonbyte-done?
    if image_large_link is None
        return '[IMG]' + image_original_link + '[/IMG]
    return '[URl=' + image_original_link + '] [IMG]' + image_large_link + '[/IMG][/URL]'

# Prints usage info
def usage():
    print 'USAGE: python test_libimgur.py [-h] [--vB] image'
 
# Main function. The magic happens here.
def main(argv):
    # Read options and arguments
    try:                                
        opts, args = getopt.getopt(argv, "h", ["help", "vB",]) 
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)   
    
    for opt, arg in opts:                
	# Help - Optional
	if opt in ("-h", "--help"):      
            usage()                     
            sys.exit()                  
        # vBulletin code - Optional
	elif opt in ("--vB"):
	    global _vBulletin 
	    _vBulletin = True
    
    image = args[0]
    
    # TODO: Multi image support
    # images = args

    # Instance of the API
    imgur = libimgur.Client(api_key)

    # Upload image(s)
    result = imgur.upload(image)

    
    image_link = get_image_link(result)
    
    # Format for vBulletin and copy to clipboard
    if _vBulletin:
	    vBulletin_code = vBulletin(image_link)
	    copy_to_clipboard(vBulletin_code)
    
    return 1

# Test function. Uploads a picture to imgur.
# Prints response given by imgur.
#
# An image has to be passed to it on the command line.
if __name__ == '__main__':
    if len(sys.argv) <= 1:
	usage()
	sys.exit(2) 
    
    
    successful = main(sys.argv[1:])
    if successful:
        print 'Link has been copied to clipboard'
