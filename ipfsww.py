import ipfsApi
import urllib.request
if __name__ == '__main__':
    a =  'http://localhost:8080/ipfs/'
    api = ipfsApi.connect('127.0.0.1', 5001)
    print(api)
    new_file = api.add('Blockchain.txt')
    print(new_file)
    data = new_file.get("Hash", "")
    print("This is the Hash of the file : ")
    print(data)
    a = a+data
    webUrl  = urllib.request.urlopen(a)
    print ("Check the file Contents for confrimation : ")
    data = webUrl.read()
    print (data)
