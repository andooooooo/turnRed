

i=1
p="profile=\"link\""
d="profile=\"des\""
y="little.txt"
while i<201:
	number = '{0:04d}'.format(i)
	title = number+"_css.html"
	try:
		tt = open(title,"r").read()
		pc = tt.count(p)
		dc = tt.count(d)
		if pc>1:
			if dc==0:
				with open(y,"a") as d
					d.write(repr(i)+" 1 0\n")
			elif dc==1:
				with open(y,"a") as d
					d.write(repr(i)+" 1 1\n")
			elif dc>1:
				with open(y,"a") as d
					d.write(repr(i)+" 1 2\n")
		elif pc==0:
			if dc==0:
				with open(y,"a") as d
					d.write(repr(i)+" 0 0\n")
			elif dc==1:
				with open(y,"a") as d
					d.write(repr(i)+" 0 1\n")
			elif dc>1:
				with open(y,"a") as d
					d.write(repr(i)+" 0 2\n")

	except:
		print("error")

	i+=1
