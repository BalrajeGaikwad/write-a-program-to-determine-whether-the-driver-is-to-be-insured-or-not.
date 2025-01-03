"""

A company insures its drivers in the following cases:

If the driver is married.

If the driver is unmarried, male & above 30 years of age.

If the driver is unmarried, female & above 25 years of age.

In all other cases, the driver is not insured. If the marital status, sex

and age of the driver are the inputs, write a program to determine whether the driver is to be insured or not.

"""
materital_status=input("Enter the marital status : married / not marrid :-  ")
sex=input("Enter the sex : male / female :-- ")
age=int(input("Enter the age:   "))

if(materital_status=="married"):
    print("Driver is insured ")
else:
    if(sex=="male"):
        if(age>30):
            print("Driver is insured")
        else:
            print("Driver is not insured")

    else:
        if(age>25):
            print("Driver is insured ")
        else:
            print("Driver is not insured ")
