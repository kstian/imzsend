from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from random import randrange
import sys, urllib2, getopt

def main(argv):
	f=''
	try:
		opts, args = getopt.getopt(argv,"hf:",["help","file="])
	except getopt.GetoptError:
		print 'rbvgrab.py -c <cookie_PHPSESSID_value> -d <directory>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'rbvgrab.py -c <cookie_PHPSESSID_value> -d <directory>'
			sys.exit()
		elif opt in ("-f", "--file="):
			f = arg
		elif opt in ("-d", "--directory"):
			d = arg
		elif opt in ("-m", "--start-modul"):
			mIndex = int(arg)
		elif opt in ("-p", "--start-page"):
			pIndex = int(arg)
	UID=''
	files = {'file': open(f, 'rb')}
	cookies = dict(login='kendata1')
	for i in range(0,12):
		UID += str(randrange(10))
	#pkey = {'upload_id': UID, 'js_on': '1', 'utype':'reg', 'upload_type':'file'}
	register_openers()
	params = {'file': open(f, "rb"), 'name': 'upload test', 'upload_type':'file', 'sess_id':'504tr39nl8157sno', 'srv_tmp_url':'http://www.imzupload.com/tmp', 'tos':'1', 'submit_btn':'Upload!'}
	url='http://www.imzupload.com/cgi-bin/upload.cgi?upload_id='+UID+'&js_on=1&utype=reg&upload_type=file'
	datagen, headers = multipart_encode(params)
	request = urllib2.Request(url, datagen, headers)
	result = urllib2.urlopen(request)
	print result.getcode()
if __name__ == "__main__":
   main(sys.argv[1:])


