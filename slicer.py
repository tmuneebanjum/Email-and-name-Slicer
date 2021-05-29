# Email Slicer

email = input("Enter Your Email : ").strip()

# tmuneebanjum@gmail.com

username = email[:email.index('@')]
domain = email[email.index('@')+1:]

result = "Your username is {} & your domain name is {}".format(username, domain)

print (result)