import re # INTENDED FOR REGEX BUT REGEX RUINS CODE
import smtplib #To send emails and login to gmail

"""

PYTHON IS CONSIDERED A 3RD PARTY APP
THEREFORE TO LOG ONTO GMAIL USING THIS CODE
YOUR SETTING FOR
"ALLOW LESS SECURE APPS" MUST BE TURNED ON

"""

#Class setup for email 
class mailman:
    
    def __init__(self, sender_email, rec_email, password, subject, text):
        self.sender_email=sender_email
        self.rec_email=rec_email
        self.password= password
        self.subject= subject
        self.text= text
        self.message = 'Subject: {}\n\n{}'.format(subject, text)
    
    def menuOptions(self):
        try:
            choice= int(input("\nEnter menu choice: "))
        except:
            print("/nError: Value is not an integer.\nReturning to main menu...\n")
            mailman.displayMenu(self)
        else:
            if(choice==1):
                mailman.setGmail(self)
            elif(choice==2):
                mailman.setPassword(self)
            elif(choice==3):
                mailman.setRec(self)
            elif(choice==4):
                mailman.compEmail(self)
            elif(choice==5):
                mailman.sendIt(self)
            elif(choice==6):
                mailman.reviewInfo(self)
            elif(choice==7):
                print("\nExiting program now...")
                return
            else:
                print("That is not a menu option.\nReturning to main menu...\n")
                mailman.displayMenu(self)
        
    def displayMenu(self):
        print("\nMain Menu")
        print("================")
        print("1: Set Gmail Address")
        print("2: Set Password")
        print("3: Set Receiving Email Address")
        print("4: Compose Email")
        print("5: Send Email")
        print("6: Review All Info")
        print("7: Exit Program")
        mailman.menuOptions(self)

    def setGmail(self): #OPTION 1: HANDLES EMAIL EXCEPTIONS
        self.sender_email=input(str("\nPlease type the gmail you are logging into: "))
        mailman.displayMenu(self)
        """ ERROR OCCURS WHEN ANALYZING EMAIL FOR ERROR
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]/+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.sender_email)
        if match == None:
            print('Error: Invalid Email Address')
            raise ValueError('Invalid Email Address')
        """

    def setPassword(self): #OPTION 2
        self.password=input(str("\nPlease type your login password : "))
        mailman.displayMenu(self)

    def setRec(self): #OPTION 3: HANDLES EMAIL EXCEPTIONS
        self.rec_email=input(str("\nPlease type the receiving email address : "))
        mailman.displayMenu(self)
        
    """ ERROR OCCURS WHEN ANALYZING EMAIL FOR ERROR
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.rec_email)
        if match == None:
            print('Error: Invalid Email Address')
            raise ValueError('Invalid Email Address')
    """

    def compEmail(self): #OPTION 4
        self.subject=input(str("\nPlease type your email's subject: "))
        self.text=input(str("\nPlease type your email's body:\n\n"))
        self.message = 'Subject: {}\n\n{}'.format(self.subject, self.text)

        mailman.displayMenu(self)

    def sendIt(self): #OPTION 5
        server= smtplib.SMTP('smtp.gmail.com', 587)
        try:
            server.ehlo()
            server.starttls()
            server.login(self.sender_email, self.password)

            print("Login success")
            server.sendmail(self.sender_email, self.rec_email, self.message)
            print("Email has been sent to", self.rec_email)
            print("\nNow returning to main menu...")
        except SMTPAuthenticationError:
            print("The username and/or password you entered may be incorrect.")
        except:
            print("An Unknown error occurred")
        server.quit()
        mailman.displayMenu(self)

    def reviewInfo(self): #OPTION 6
        print("\nLogin Email Address:".ljust(35)+ self.sender_email)
        print("Login Password:".ljust(34)+ self.password)
        print("Receiving Email Address:".ljust(34)+ self.rec_email)
        print(self.message)
        mailman.displayMenu(self)
      
#My Function calls
user1=mailman('','','','','')
user1.displayMenu()













