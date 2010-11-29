import libimgur

if __name__ == '__main__':
    imgur = libimgur.Client('02b62fd8f1d5e78321e62bb42ced459e')
    img = imgur.upload('/Users/sparragus/Desktop/smiley.png')
    print img
