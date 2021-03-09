import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response)
Llist=data["result"]["results"]#得到一個列表

with open("data.txt","w",encoding="utf-8") as file:
    # for location in Llist:
    #     location["file"].replace(".JPG",".jpg")
    for location in Llist:
        file.write(location["stitle"]+","+location["longitude"]+","+location["latitude"]+","+(location["file"].replace(".JPG",".jpg").split("jpghttp"))[0]+"jpg"+"\n")