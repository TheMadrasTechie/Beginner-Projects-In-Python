email = input("Your mail Id: ").strip()

user_name = email[:email.index("@")]

domain_name = email[email.index("@")+1:]

output  = "Your Username is "+user_name+" \n your domain name is:"+domain_name

print(output)