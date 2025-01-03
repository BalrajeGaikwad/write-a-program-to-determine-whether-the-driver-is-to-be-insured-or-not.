#by using logical operator

marital_status=input("Enter the marital status : married / not_marrid :-  ")
sex=input("Enter the sex : male / female :-- ")
age=int(input("Enter the age:   "))


if marital_status == "married" or \
   (marital_status == "not_marrid" and sex == "male" and age > 30) or \
   (marital_status == "not_marrid" and sex == "female" and age > 25):
    print("The driver is eligible for insurance.")
else:
    print("The driver is not eligible for insurance.")
