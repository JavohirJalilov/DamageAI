def size(f):
	"""
	Returns: Width and Height (tuple)
	"""
	w1 = f.find('width')+6
	w2 = f.find('width',w1)-2
	W = int(f[w1:w2])

	h1 = f.find('height')+7
	h2 = f.find('height',h1)-2
	H = int(f[h1:h2])

	return  W,H

def find_contors_class(f):
	"""
	Parameters(str): string file(f)
	returns(list): x_min,y_min,x_max,y_max,classes(tuple)
	"""
	data = []
	i = 0
	while True:
		if i == 0:
			an_idx1 = f.find('object')+6
			an_idx2 = f.find('object',an_idx1)
			
			x_min_idx1 = f.find('xmin')+5
			x_min_idx2 = f.find('xmin',x_min_idx1,an_idx2)
			x_min = f[x_min_idx1:x_min_idx2-2]

			y_min_idx1 = f.find('ymin')+5
			y_min_idx2 = f.find('ymin',y_min_idx1,an_idx2)
			y_min = f[y_min_idx1:y_min_idx2-2]
		
			x_max_idx1 = f.find('xmax')+5
			x_max_idx2 = f.find('xmax',x_max_idx1,an_idx2)
			x_max = f[x_max_idx1:x_max_idx2-2]


			y_max_idx1 = f.find('ymax')+5
			y_max_idx2 = f.find('ymax',y_max_idx1,an_idx2)
			y_max = f[y_max_idx1:y_max_idx2-2]

			x_min,y_min,x_max,y_max = int(x_min),int(y_min),int(x_max),int(y_max)

			# Find Class

			class_idx1 = f.find('Background')+len('Background')+1
			class_idx2 = f.find('Background',class_idx1,an_idx2)
			class_1 = ('Background',f[class_idx1:class_idx2-2])
			
			class_idx3 = f.find('Crack')+len('Crack')+1
			class_idx4 = f.find('Crack',class_idx3,an_idx2)
			class_2 = ('Crack',f[class_idx3:class_idx4-2])

			class_idx5 = f.find('Spallation')+len('Spallation')+1
			class_idx6 = f.find('Spallation',class_idx5,an_idx2)
			class_3 = ('Spallation',f[class_idx5:class_idx6-2])

			class_idx7 = f.find('Efflorescence')+len('Efflorescence')+1
			class_idx8 = f.find('Efflorescence',class_idx7,an_idx2)
			class_4 = ('Efflorescence',f[class_idx7:class_idx8-2])

			class_idx9 = f.find('ExposedBars')+len('ExposedBars')+1
			class_idx10 = f.find('ExposedBars',class_idx9,an_idx2)
			class_5 = ('ExposedBars',f[class_idx9:class_idx10-2])

			class_idx11 = f.find('CorrosionStain')+len('CorrosionStain')+1
			class_idx12 = f.find('CorrosionStain',class_idx11,an_idx2)
			class_6 = ('CorrosionStain',f[class_idx5:class_idx6-2])
			classes = (class_1,class_2,class_3,class_4,class_5,class_6)
			an_idx1 = an_idx2+6
			i+=1
			data.append((x_min,y_min,x_max,y_max,classes))
		else:
			if an_idx1 == -1:
				break
			else:
				an_idx1 = f.find('object',an_idx1)
				if an_idx1 == -1:
					break
				an_idx1 = an_idx1+6
				an_idx2 = f.find('object',an_idx1)

				x_min_idx1 = f.find('xmin',an_idx1)+5
				x_min_idx2 = f.find('xmin',x_min_idx1,an_idx2)
				x_min = f[x_min_idx1:x_min_idx2-2]

				y_min_idx1 = f.find('ymin',an_idx1)+5
				y_min_idx2 = f.find('ymin',y_min_idx1,an_idx2)
				y_min = f[y_min_idx1:y_min_idx2-2]
			
				x_max_idx1 = f.find('xmax',an_idx1)+5
				x_max_idx2 = f.find('xmax',x_max_idx1,an_idx2)
				x_max = f[x_max_idx1:x_max_idx2-2]


				y_max_idx1 = f.find('ymax',an_idx1)+5
				y_max_idx2 = f.find('ymax',y_max_idx1,an_idx2)
				y_max = f[y_max_idx1:y_max_idx2-2]

				x_min,y_min,x_max,y_max = int(x_min),int(y_min),int(x_max),int(y_max)

				# Find Class

				class_idx1 = f.find('Background')+len('Background')+1
				class_idx2 = f.find('Background',class_idx1,an_idx2)
				class_1 = ('Background',f[class_idx1:class_idx2-2])
				
				class_idx3 = f.find('Crack')+len('Crack')+1
				class_idx4 = f.find('Crack',class_idx3,an_idx2)
				class_2 = ('Crack',f[class_idx3:class_idx4-2])

				class_idx5 = f.find('Spallation')+len('Spallation')+1
				class_idx6 = f.find('Spallation',class_idx5,an_idx2)
				class_3 = ('Spallation',f[class_idx5:class_idx6-2])

				class_idx7 = f.find('Efflorescence')+len('Efflorescence')+1
				class_idx8 = f.find('Efflorescence',class_idx7,an_idx2)
				class_4 = ('Efflorescence',f[class_idx7:class_idx8-2])

				class_idx9 = f.find('ExposedBars')+len('ExposedBars')+1
				class_idx10 = f.find('ExposedBars',class_idx9,an_idx2)
				class_5 = ('ExposedBars',f[class_idx9:class_idx10-2])

				class_idx11 = f.find('CorrosionStain')+len('CorrosionStain')+1
				class_idx12 = f.find('CorrosionStain',class_idx11,an_idx2)
				class_6 = ('CorrosionStain',f[class_idx5:class_idx6-2])
				classes = (class_1,class_2,class_3,class_4,class_5,class_6)
				an_idx1 = an_idx2+6

				data.append((x_min,y_min,x_max,y_max,classes))
	return data

def image_information(file_name):
	"""
	Parameter(str): filename
	Returns(tuple):size, contours and classes
	"""
	f = open(f"sample/annotations/{file_name}.xml").read()
	return size(f),find_contors_class(f)




	
	
