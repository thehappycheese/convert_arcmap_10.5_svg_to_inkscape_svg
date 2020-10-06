import sys
import os
import xml.etree.ElementTree as etree

filenames = sorted(sys.argv[1:])

if len(filenames)==0:
	print("Requires command line argument of at least one svg file!")
	#os.system("pause")
	exit()
	
output_directory = os.path.dirname(filenames[0])

print("\r\n>> Executing")

for index, input_filename in enumerate(filenames):
	print(f">> Attempting to convert: {input_filename}")
	(output_filename, output_extention) = os.path.splitext(input_filename)

	if not output_extention==".svg":
		raise Exception("input must be svg")
	output_filename = output_filename+"_inkscape_.svg"
	print(f">> Will output to:\r\n{os.path.join(output_directory, output_filename)}")
	with open(input_filename,"rt") as f_in :
		tree = etree.parse(f_in)
		root = tree.getroot()

		root.attrib["xmlns:inkscape"] = 'http://www.inkscape.org/namespaces/inkscape'
		root.attrib["xmlns:sodipodi"] = 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd'
		etree.register_namespace("", "http://www.w3.org/2000/svg")
		layers = tree.find('//{http://www.w3.org/2000/svg}g[@id="Layers"]')
		layers.attrib["inkscape:groupmode"] = "layer"
		layers.attrib["inkscape:label"] = layers.attrib['id']
		childs = layers[:]
		root_groups = root.findall("./{http://www.w3.org/2000/svg}g")
		layer_groups = layers.findall("./{http://www.w3.org/2000/svg}g")
		for root_group in [*root_groups, *layer_groups]:
			root_group.attrib["inkscape:groupmode"] = "layer"
			root_group.attrib["inkscape:label"] = root_group.attrib['id']
			root_group.attrib["sodipodi:insensitive"] = "1"

		with open(output_filename,"w") as output_file:
			tree.write(output_filename)


print("Success!")
#os.system("pause")
