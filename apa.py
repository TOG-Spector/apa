################################################################################
class Apa:
	#Capitalizing the first letter of words in a list
	def __init__(self):
		pass
	def sentence_case(self,something):
		for x in range(len(something)):
			something[x] = something[x].replace(something[x][0],something[x][0].upper(),1)
		return something

	#generate the initials for all names apart from the last name
	def initials(self,name):
		result = ''
		for x in range(len(name)-1):
			result = result + name[x][0] +'.'
		return result

	#function for formatting the name of the author
	def author_formatting(self,author):
		name = self.sentence_case(author.split(' '))
		return name[-1]+','+self.initials(name)

	#function for formatting the date dd/mm/yyyy
	def date_formatting1(self,date):
		dictionary = {'1':'January','2':'Ferbuary','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
		part = date.split('-')
		return '('+part[0] + ' '+ dictionary[part[1]] + ' '+part[2]+').'

	#formatting the title in a reference
	def title_formatting(self,title):
		final = title.split(' ')
		for x in range(1,len(final)):
			final[x].replace(final[x][0],final[x][0].lower(),1)
		return ' '.join(final)

	##function for formatting the date yyyy/dd/mm
	def date_formatting2(self,date):
		dictionary = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
		part = date.split('-')
		return '('+dictionary[part[1]] +' '+part[0] +' '+part[2]+').'

	################################################################################
	#function for formatting the reference of an article
	def article(self,author,date,title_of_article,title_of_periodical,volume_number,issue_number,url):
		return self.author_numbers(author)+self.date_formatting1(date)+title_of_article+'.'+title_of_periodical+','+volume_number+'('+issue_number+').Retrieved from '+url

	#function for formatting a reference of an article with multiple authors
	def author_numbers(self,authors):
		name = ''
		for x in authors:
			name = name + str(self.author_formatting(x))
		return name

	#function for the referencing of a book
	def book(self,author,title,year,location,publisher):
		formatted_publisher = self.sentence_case(publisher.split(' '))
		#print(publisher)
		return self.author_numbers(author)+'('+ str(year) +').'+title+'.'+location+': '+' '.join(formatted_publisher)

	#function for refrencing a webpage
	def webpage(self,author,date,title,site_name,url):
			return self.author_numbers(author)+self.date_formatting2(date)+self.title_formatting(title)+'.'+site_name+'.'+url

	#function for refrencing a webpage authored by a group
	def webpageOrg(self,author,date,title,site_name,url):
			return author+self.date_formatting2(date)+self.title_formatting(title)+'.'+site_name+'.'+url


'''
print(book('george orwell','1984',1955,'New York','new american library'))
print(article('Dieter Bohn','12-2-2020',"Samsung's Galaxy Z Flip beats the Motorola Razr in nearly every way","The Verge","12","14","https://www.theverge.com/2020/2/12/21134261/samsung-galaxy-z-flip-vs-motorola-razr-folding-flip-phone-camera-battery-processor"))
print(webpage('Devon Price','5-2-2020','Laziness Does Not Exist','Medium','https://humanparts.medium.com/laziness-does-not-exist-3af27e312d01'))
'''
