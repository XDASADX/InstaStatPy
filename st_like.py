import re
import requests
import os


code_addr='https://instagram.com/p/'

#os.mkdir(os.getcwd()+'\\data')

id='natgeo'
d_f=open(os.getcwd()+'\\data\\'+'stat_'+id+'.csv','w')


d_f.write('Instagram上'+id+'的统计\n')
d_f.write('like'+'\n')
r=requests.get('https://www.instagram.com/'+id+'/?hl=en')
con=r.content



start_i=r'"start_cursor":"[0-9]*"'
end_i=r'end_cursor":"[0-9]*"'
like=r'"likes":{"count":[0-9]*},"'
code_i=r'{"code":"[\w\-]+"'

start_cursor=re.findall(start_i,con.decode())
end_cursor=re.findall(end_i,con.decode())
like_list=re.findall(like,con.decode())
code_list=re.findall(code_i,con.decode())

start_var=start_cursor[0]
start_var=start_var[16:-1]

end_var=end_cursor[0]
end_var=end_var[13:-1]

like_list_f=[]
code_list_f=[]

print(code_list)
print(len(code_list))

for i in range(0,len(like_list)):
	a=like_list[i]
	a=a[17:-3]
	like_list_f.append(a)
	d_f.write(a+',')

	b=code_list[i]
	b=b[9:-1]
	code_list_f.append(b)
	d_f.write(code_addr+b+'\n')



pagenum=1

while(start_var!=end_var):
	print("Page",(pagenum),"has been counted.")
	pagenum+=1
	r=requests.get('https://www.instagram.com/'+id+'/?max_id='+end_var)
	con=r.content

	start_i=r'"start_cursor":"[0-9]*"'
	end_i=r'end_cursor":"[0-9]*"'
	like=r'"likes":{"count":[0-9]*},"'
	code_i=r'{"code":"[\w\-]+"'

	start_cursor=re.findall(start_i,con.decode())
	end_cursor=re.findall(end_i,con.decode())
	like_list=re.findall(like,con.decode())
	code_list=re.findall(code_i,con.decode())

	start_var=start_cursor[0]
	start_var=start_var[16:-1]
	
	end_var=end_cursor[0]
	end_var=end_var[13:-1]

	
	for i in range(0,len(like_list)):
		a=like_list[i]
		a=a[17:-3]
		like_list_f.append(a)
		d_f.write(a+',')
	
		b=code_list[i]
		b=b[9:-1]
		code_list_f.append(b)
		d_f.write(code_addr+b+'\n')


print (len(like_list_f))
	
d_f.write('=AVERAGE(A3:A'+str(len(like_list_f)+2)+')')
	

d_f.close()
