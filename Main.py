from  Register import  Register
from Login import Login
from project import Project
import re


def validateDate(date):
    if re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', date):
        return date
    else:
        newDate = input("Enter date Correct Please: \n")
        validateDate(newDate)

def second_display(user):
    ch = int(input("Please The Choose: \n 1 Create \n 2 View  \n 3 Edit \n "
        "4 Delete  \n 5 Exit \n"))
    if ch == 1:
        project = Project()
        project.create()
        projectAttr = [user[0], project.title, project.Discribtion, project.totalTarget, project.startDate, project.endtDate]
        listToStr = " "
        for item in projectAttr:
            listToStr += item
            listToStr += ":"
        file = open("projects.txt", "a")
        file.write(listToStr)
        file.write("\n")
        file.close()
        second_display(user)
    elif ch==2:
        file = open("projects.txt", "r")
        lines = file.readlines()
        for line in lines:
            projectAttr=line.split(":")
            print(" Title: ", projectAttr[1])
            print(" Details: ", projectAttr[2])
            print(" Total Target: ", projectAttr[3])
            print(" Start Date: ", projectAttr[4])
            print(" End Date: ", projectAttr[5])
            print("____________________________________________")
        second_display(user)
    elif ch == 3:
        print("Enter Name The Project: ")
        userID = user[0]
        file = open("projects.txt", "r")
        lines = file.readlines()
        userProjects = []
        i=0
        for line in lines:
            projectList = line.split(":")
            if projectList[0] == userID:
                userProjects.append(projectList[1])
            i+=1
        j=1
        for project in userProjects:
            print(j, "_", project)
            j += 1
        choice = input()
        Project.editProject(choice)
        second_display(user)

    elif ch == 4:
        print("Enter Name The Project: ")
        userID = user[0]
        file = open("projects.txt", "r")
        lines = file.readlines()
        userProjects = []
        i = 0
        for line in lines:
            projectList = line.split(":")
            if projectList[0] == userID:
                userProjects.append(projectList[1])
            i += 1
        j = 1
        for project in userProjects:
            print(j, "_", project)
            j += 1
        choice = input()
        Project.deleteProject(choice, user[0])
        second_display(user)

    
    elif ch == 5:
        pass

def first_display ():
    choice = int(input("Please enter The Choose: \n 1 Register \n 2 Login \n 3 Exit \n"))
    if choice==1:
        user = Register()
        user.register()
        strID= str(user.id)
        list = [strID, user.fname, user.lname, user.email, user.password, user.phonenum]
        listToStr = " "
        for item in list:
            listToStr += item
            listToStr += ":"
        file = open("DatabaseFile.txt","a")
        file.write(listToStr)
        file.write("\n")
        file.close()
        first_display()
    elif choice==2:
        user = Login()
        userInfo = user.login()
        second_display(userInfo)
        first_display()
    elif choice==3:
        pass

first_display()
