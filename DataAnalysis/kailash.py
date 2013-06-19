import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.path as path
import matplotlib.patches as patches

class KMY():
	"""Data analysis of Kailash Mansarovar Yaatris 2013"""
	def __init__(self):
		print "ok"
		
	'''parse values and return as list'''
	def parse(self):
		print "hello"
		kmy = open('kmy.txt', "r")
		rows = 0
		line = kmy.readline()
		oldline = 'XXXX'
		doblist = []
		fnames = []
		lnames = []
		fatherExpired = 0
		fathersLastName = []
		name = []
		fathersName = []
		
		
		while line:
			rows = rows+1
			words = line.split(' ')
			#some lines have this extra whitespace which is blocking this to go through
			words[0] = words[0].strip()
			
			#print words[0]
			if (words[0].isdigit()):
				
				#print words[0]
				if (oldline!='XXXX'):
					words = oldline.split(' ')
					
					#find a line containing dob
					'''in this case it is next to word starting with KMY'''
					for i in range(len(words)):
						if (i==1):
							fnames.append(words[1])
						
						if (words[i].startswith('KMY')):
							#person's name has all words before this index
							name.append(words[1:i])
							fathersName.append(words[i+2:])
							doblist.append(words[i+1])
							lnames.append(words[i-1])
							if (words[i+2]=="LATE"):
								fatherExpired +=1
							#print words[i+1]
					fathersLastName.append(words[len(words)-1])
				
				#print oldline
				oldline = line
			else:
				#print "*********" + line
				oldline = oldline.replace("\n", " ")
				oldline = oldline + line #this still the continuation
			
			#print line
			line = kmy.readline()
		print "total lines are: " + str(rows)
		print "total dobs:" + str(len(doblist))
		print "father noMore:" + str(fatherExpired)
		kmy.close()
		return doblist, fnames, lnames, fathersLastName, name, fathersName
		
	''' extract year of birth '''	
	def parsedob(self, doblist):
		years = []
		for w in doblist:
			year = w.split('-')
			years.append(int(year[2]))
		return years
	
	''' plots histogram using matplotlib'''		
	def plotyears(self, years):
		years[:] = [2013 - x for x in years]#age makes more sense than showing year of birth
		bins = max(years) - min(years)
		print str(max(years)) + " , " + str(min(years))
 		n, bins = np.histogram(years, bins)

		'''myplotlib stuff here'''
		fig = plt.figure()
		ax = fig.add_subplot(111)
		
		# get the corners of the rectangles for the histogram
		left = np.array(bins[:-1])
		right = np.array(bins[1:])
		bottom = np.zeros(len(left))
		top = bottom + n
		
		# we need a (numrects x numsides x 2) numpy array for the path helper
		# function to build a compound path
		XY = np.array([[left,left,right,right], [bottom,top,top,bottom]]).T

		# get the Path object
		barpath = path.Path.make_compound_path_from_polys(XY)

		# make a patch out of it
		patch = patches.PathPatch(barpath, facecolor='green', edgecolor='gray', alpha=0.8)
		ax.add_patch(patch)
		
		
		# update the view limits
		ax.set_xlim(left[0], right[-1])
		ax.set_ylim(bottom.min(), top.max()+5)
		plt.grid(True, which="both", ls="dotted")
		
		#plot both mean and sd
		plt.vlines(np.mean(years), [0], top.max()+5, colors='r', linestyles='dashed')
		plt.vlines(np.mean(years) + np.std(years), [0], top.max()+5, colors='b', linestyles='dashed')
		plt.vlines(np.mean(years) - np.std(years), [0], top.max()+5, colors='b', linestyles='dashed')
		
		plt.xlabel("Age in years")
		plt.ylabel("Number of travellers")
		plt.title("KMY 2013 Profile")
		plt.show()
		print "mean is: " + str(np.mean(years))
		print "sd : " + str(np.std(years))
		print str(n)
		
	'''find most occuring value in list'''	
	def mostCommonValue(self, firstNames):
		
		fname_counter = {}
		for name in firstNames:
			if name in fname_counter:
				fname_counter[name] +=1
			else:
				fname_counter[name] = 1
			
		most_common_fnames = sorted(fname_counter, key = fname_counter.get, reverse = True)
		
		#print most_common_fnames[:10]
		for i in range(len(fname_counter)):
			print "[" + "\'" + most_common_fnames[i].replace("\n", " ") + "\'" + ", " + str(fname_counter[(most_common_fnames[i])]) + "],"
		print "ok"
		
	''' shortcut to print a list'''
	def printList(self, itemlist):
		for w in itemlist:
			print w
			
	def maxBirthday(self, doblist):
		daymonth = []
		for w in doblist:
			daymonth.append(w[:6])
			#print w[:6]
		self.mostCommonValue(daymonth)
	
	''' find relations based on names (assumptions based on the fact that women in india change their name after marriage)'''	
	def findRelations(self, names, fathersName):
		
		for i in range(len(names)-1):
			if (names[i+1] is not None) and (len(names[i+1]) >= 2):
				if (names[i][0].replace("\n", "") == names[i+1][1].replace("\n", "")):
					#print str(names[i]) + " and " + str(names[i+1])
					if len(fathersName[i+1])>=2:
						lname = names[i][-1]
						fathersName[i+1][-1] = fathersName[i+1][-1].replace("\n", "")
						if (lname not in fathersName[i+1]):
							print str(names[i][-1]) + " ~ " + str(fathersName[i+1][-1].replace("\n", ""))+  " | " + str(fathersName[i+1][0].replace("\n", ""))
							#print "###" + str(fathersName[i+1][0].replace("\n", "")) + " vs " + str(names[i][-1])
	
	def findRelationsNorthIndia(self, names, fathersName):
				for i in range(len(names)-1):
					if (len(names[i+1]) >= 2) and (len(names[i+1]) < 4) : #name length between 2 and 3 only
						#if last name is same (which is the case in North India to be related)
						if (names[i][-1].replace("\n", "") == names[i+1][-1].replace("\n", "")):
								if len(fathersName[i+1])>=2:
									lname = names[i][-1]
									fathersName[i+1][-1] = fathersName[i+1][-1].replace("\n", "")
									if (lname not in fathersName[i+1]) and (names[i][0] != names[i+1][1]): #ignore earlier condition of women having their husband's name add to theirs
											print str(names[i][-1]) + " ~ " + str(fathersName[i+1][-1].replace("\n", ""))+  " | " + str(fathersName[i+1][0].replace("\n", ""))
						
def main():
	obj = KMY()
	doblist, fnames, lnames, fathersLastName, name, fathersName = obj.parse()
	years = obj.parsedob(doblist)
	#obj.plotyears(years)
	#obj.mostCommonValue(fnames)
	#obj.mostCommonValue(lnames)
	#obj.mostCommonValue(fathersLastName)
	#obj.mostCommonValue(fathersName)
	
	#obj.mostCommonValue(doblist)
	#obj.maxBirthday(doblist)
	#obj.findRelations(name, fathersName)
	obj.findRelationsNorthIndia(name, fathersName)
	#obj.printList(name)
	
if __name__ == '__main__':main()	

	
		