import passwords
import requests

def main():
	URL = "https://httpbin.org/basic-auth/russ/test"
	user = passwords.user
	passwd = passwords.passwd

	vars = {"user":user, "passwd":passwd}
	r = requests.get(URL, params=vars)
	print(r.content)



main()
