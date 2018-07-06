import urllib.request
import json
# https://storage.googleapis.com/tfjs-models/
# weights/posenet/mobilenet_v1_075/MobilenetV1_Conv2d_0_biases

# testurl = 'https://imgs.xkcd.com/comics/new_phone_thread_2x.png'
# response = urllib.request.urlopen(testurl)
# data = response.read()      # a `bytes` object
#text = data.decode('utf-8') # a `str`; this step can't be used if data is binary


with open("posenet-models/manifest.json", encoding='utf-8-sig') as json_file:
	json_data = json.load(json_file)

	url = "https://storage.googleapis.com/tfjs-models/weights/posenet/mobilenet_v1_075/"
	#https://storage.googleapis.com/tfjs-models/weights/posenet/mobilenet_v1_075/
	#https://storage.googleapis.com/tfjs-models/weights/posenet/mobilenet_v1_075/MobilenetV1_heatmap_2_biases
	#MobilenetV1_Conv2d_0_biases
	

	for sectionKey in json_data:
		section = json_data[sectionKey]
		
		filename = section["filename"]
		print(filename)
		response = urllib.request.urlopen(url + filename)
		data = response.read()      # a `bytes` object
		#text = data.decode('utf-8') # a `str`; this step ca

		with open("posenet-models/" + filename, 'bw+') as f:
			f.write(data)
