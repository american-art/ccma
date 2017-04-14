import json

#filename = "museums/ccma/ccmadata/ccma-objects_artists_exhibs.json"
filename = "ccmadata/ccma-objects_artists_exhibs.json"

f = open(filename,"r")
f_objects = open("ccma_objects/ccma_objects.json","w")
f_artists = open("ccma_artists/ccma_artists.json","w")
data = json.loads(f.read())
artists = data["artists"]
objects = data["objects"]

f_artists.write('{"artists": ')
json.dump(artists, f_artists, indent=4)
f_artists.write("}")

f_objects.write('{"objects": ')
json.dump(objects, f_objects, indent=4)
f_objects.write("}")

f.close()
f_artists.close()
f_objects.close()