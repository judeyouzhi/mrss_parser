import urllib2
import xmltodict

tcount = 0  #VideoAdsDisplay = true
fcount = 0  #VideoAdsDisplay = false

def parsexml(key,url):
    global tcount, fcount
    inputfile = urllib2.urlopen(url)
    data = inputfile.read()
    inputfile.close()

    pdata = xmltodict.parse(data)
    try:
        if isinstance(pdata["rss"]["channel"]["item"], list):
            for i in pdata["rss"]["channel"]["item"]:
                #print i
                for kv in i["dfpvideo:keyvalues"]:
                    # print '\n' + "contentID : " + item["dfpvideo:contentID"]
                    if kv["@key"] == "VideoAdsDisplay":
                        if kv["@value"] == "true":
                            # print kv["@key"], kv["@value"]
                            tcount += 1
                        else:
                            fcount += 1
    except KeyError:
        print "empty xml response: no item included"


for i in range(195, 200):  #495
    parsexml('''VideoAdsDisplay''', 'https://s3-ap-southeast-1.amazonaws.com/ads-mrss.iflix.com/MRSS'+str(i)+'.xml')
    print i

print "VideoAdsDisplay true count = " + str(tcount)
print "VideoAdsDisplay false count = " + str(fcount)