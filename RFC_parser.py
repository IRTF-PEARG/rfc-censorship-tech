inf = open('parsable_cites.txt', 'r')
outf = open('rfc_cites.xml', 'w')
i = 1
while i < 62:
	inf.readline()

	author = inf.readline()
	temp_line = inf.readline()
	if (temp_line[0] == '&'):
		print "caught"
		temp_line = inf.readline()
	parsed_date = inf.readline().split(' ')
	reference = inf.readline().strip(' ').strip('\n')
	author_last = author.split(", ")[0]
	author_first = author.split(", ")[1]
	outf.write('<reference anchor="ref-'+str(i)+'" target="'+reference+'">\n')
	outf.write('<front>\n')
	########################
	outf.write('<title>\n')
	outf.write(temp_line)
	outf.write('</title>\n')
	#######################
	outf.write('<author ')
	outf.write('initials="'+author_first[0]+'.'+author_last[0]+'." ')
	outf.write('surname="'+author_last+'" ')
	outf.write('fullname="'+author_first+' '+author_last+'">')
	outf.write('</author>\n')
	outf.write('<date month="'+parsed_date[0]+'" ')
	try:
		outf.write('year="'+parsed_date[1]+'" ')
	except IndexError:
		outf.write('year="N/A" ')
	try:
		outf.write('day="'+parsed_date[2]+'" />\n')
	except IndexError:
		outf.write('day="N/A" />\n')
	#outf.write('<eref target="'+inf.readline()+'"></eref>\n')
	outf.write('</front>\n')
	outf.write('</reference>\n')
	i = i+1
inf.close()
outf.close()