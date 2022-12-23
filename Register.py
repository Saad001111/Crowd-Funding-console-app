import re
class Register:
    def FirstName(self, fname):
        fnameValid = re.fullmatch(r'[a-zA-Z]+$',fname)
        if fnameValid:
            self.fname=fname
        else:
            anotherFname = input("Enter your first name: \n")
            self.FirstName(anotherFname)

    def LastName(self, lname):
        lnameValid = re.fullmatch(r'[a-zA-Z]+$', lname)
        if lnameValid:
            self.lname = lname
        else:
            anotherLname = input("Enter your last name: \n")
            self.LastName(anotherLname)

    def Email(self, email):
        emailValid = re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email)
        if emailValid:
            self.email = email
        else:
            anotherEmail = input("Enter your email please: \n")
            self.Email(anotherEmail)

    def Password(self):
        password = input("Enter your password \n")
        confirmpwd= input("Confirm Password: \n")
        if password != confirmpwd:
            print("password Not match")
            self.Password()
        else:
            self.password = password

    def MobileNumber(self, number):
        numberValid = re.match(r'^01[0125][0-9]{8}$', number)
        if numberValid:
            self.phonenum = number
        else:
            anothernum = input("Enter your Phone: \n")
            self.MobileNumber(anothernum)

    def register(self):
        self.id = id(self)
        fname= input("Enter your First name: \n")
        self.FirstName(fname)
        lname = input("Enter your Last name: \n")
        self.LastName(lname)
        email = input("Enter your Email: \n")
        self.Email(email)
        self.Password()
        number = input("Enter you Phone: \n")
        self.MobileNumber(number)
