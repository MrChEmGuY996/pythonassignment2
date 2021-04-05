
# design a program that can accept user input
# 1 enter first and last names
# 2 enter country of origin
# 3 enter nature of your current job
# 4 enter your email address (can be fake)
# 5 enter your phone number (can be fake)
# 6 enter your current city of residence (can be fake)
# 7 enter your mailing address (can be fake)

first_name = input("Enter your first name")
last_name = input("Enter your last name")

names = (first_name +" " +last_name)
# 1 enter first and last names

country = input("Where were you born?")
# 2 enter country of origin

profession = input("What is your job?")
# 3 enter nature of your current job

e_mail_address = input("What is your e-mail?")
# 4 enter your email address (can be fake)

phone_number = input("What is your phone number?")
# 5 enter your phone number (can be fake)

city_of_residence = input("What city do you live in?")
# 6 enter your current city of residence (can be fake)

mailing_address = input("What is your mailing address?")
# 7 enter your mailing address (can be fake)

print("Name: " +names)
print("Country: " +country)
print("Profession: " +profession)
print("E-mail: " +e_mail_address)
print("Phone: " +phone_number)
print("City: " +city_of_residence)
print("Address: " +mailing_address)
