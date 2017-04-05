import json

#filename = "museums/ccma/ccmadata/ccma-objects_artists_exhibs.json"
filename = "ccmadata/ccma-objects_artists_exhibs.json"

f = open(filename,"r")
foo = open("ccma_objects/ccma_objects.json","w")
foa = open("ccma_artists/ccma_artists.json","w")
data = json.loads(f.read())
artists = data["artists"]
objects = data["objects"]

foa.write('{"artists": ')
json.dump(artists, foa, indent=4)
foa.write("}")

foo.write('{"objects": ')
json.dump(objects, foo, indent=4)
foo.write("}")

f.close()
foa.close()
foo.close()