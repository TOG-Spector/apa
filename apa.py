################################################################################
class Apa:
	#Capitalizing the first letter of words in a list
	def __init__(self):
		pass
	def sentence_case(self,cased_names):
		for x in range(len(cased_names)):
			cased_names[x] = cased_names[x].replace(cased_names[x][0],cased_names[x][0].upper(),1)
		return cased_names

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

	#function for formatting the date (day month year)
	def date_formatting1(self,date):
		dictionary = {1:'January',2:'Ferbuary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
		part = date.split('-')
		return '('+part[0] + ' '+ dictionary[int(part[1])] + ' '+part[2]+').'
	
	#function for formatting the date to (year, month day)
	def date_formatting2(self,date):
		dictionary = {1:'January',2:'Ferbuary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
		part = date.split('-')
		return '('+part[2] + ', '+ dictionary[int(part[1])] + ' '+part[0]+').'

	#formatting the title in a reference
	def title_formatting(self,title):
		final = title.split(' ')
		final = self.sentence_case(final)
		#final[0] = final[0].replace(final[0][0],final[0][0].upper(),1)
		for x in range(1,len(final)):
			final[x] = final[x].replace(final[x][0],final[x][0].lower(),1)
		return ' '.join(final)

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
		return self.author_numbers(author)+'('+ str(year) +').'+title+'.'+location+'. '+' '.join(formatted_publisher)

	#function for refrencing a webpage
	def webpage(self,author,date,title,site_name,url):
			return self.author_numbers(author)+self.date_formatting2(date)+self.title_formatting(title)+'.'+self.title_formatting(site_name)+'.'+url

