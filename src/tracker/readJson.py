json_fileName = 'json_tracklets.json'

if __name__ == '__main__':
    try:
        file = open(json_fileName, 'rb')
        # TODO: load function to read json--pass into overlay
        file.close()
    except:
        print "could not open file: " + json_fileName