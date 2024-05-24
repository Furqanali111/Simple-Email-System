
class Email:
    def __init__(self,sender_address,subject_line,email_content):
        self.sender_address=sender_address
        self.subject_line=subject_line
        self.email_content=email_content
        self.has_been_read=False
        self.is_spam=False
        return

    def mark_as_read(self):
        self.has_been_read=True
        return

    def mark_as_spam(self):
        self.is_spam=True
        return

class Inbox:
    def __init__(self):
        self.email_list=[]
        return

    def add_email(self, from_address, subject_line, email_contents):
        email=Email(from_address,subject_line,email_contents)
        self.email_list.append(email)
        return

    def list_messages_from_sender(self, sender_address):
        x=0
        email_ex=True
        for email in self.email_list:
            if email.sender_address==sender_address:
                print(x,email.subject_line)
                x+=1
                email_ex=False
        if email_ex:
            print("Incorrect information!")
        return

    def get_email(self, sender_address, index):
        x=0
        email_ex=True
        for email in self.email_list:
            if email.sender_address==sender_address:
                if x==index:
                    print(email.subject_line,"\n",email.email_content)
                    email.mark_as_read()
                    email_ex=False
                x+=1
        if email_ex:
            print("Incorrect information!")
        return

    def mark_as_spam(self, sender_address, index):
        x = 0
        spam_ex=True
        for email in self.email_list:
            if email.sender_address == sender_address:
                if x == index:
                    email.mark_as_spam()
                    spam_ex=False
                x += 1
        if spam_ex:
            print("Incorrect information!")
        return

    def  get_unread_emails(self):
        x = 0
        email_ex=True
        for email in self.email_list:
            if email.has_been_read==False:
                print(email.subject_line)
                email_ex=False
                x+=1

        if email_ex:
            print("Their is no un read email")
        return

    def get_spam_emails(self):
        x = 0
        spam_ex=True
        for email in self.email_list:
            if email.is_spam == True:
                print(email.subject_line)
                spam_ex=False
                x += 1
        if spam_ex:
            print("Their is no email in spam folder")
        return

    def  delete(self, sender_address, index):
        x = 0
        y=0
        deleted=False
        for email in self.email_list:
            if email.sender_address == sender_address:
                if x == index:
                    self.email_list.pop(y)
                    deleted=True
                x += 1
            y+=1
        if deleted:
            print("Email successfully deleted")
        return


usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

#An Email Simulation
user_choice = ""

if __name__=="__main__":
    inbox=Inbox()
    while True:
        user_choice = input(usage_message).strip().lower()
        if user_choice == "s":
            # Send an email (Create a new Email object)
            sender_address = input("Please enter the address of the sender\n:")
            subject_line = input("Please enter the subject line of the email\n:")
            contents = input("Please enter the contents of the email\n:")

            # Now add the email to the Inbox
            inbox.add_email(sender_address,subject_line,contents)
            # Print a success message
            print("Email has been added to inbox.")

            pass
        elif user_choice == "l":
            # List all emails from a sender_address
            sender_address = input("Please enter the address of the sender\n:")

            # Now list all emails from this sender
            inbox.list_messages_from_sender(sender_address)
            pass
        elif user_choice == "r":
            # Read an email
            # Step 1: show emails from the sender
            sender_address = input("Please enter the address of the sender of the email\n:")

            # Step 2: show all emails from this sender (with indexes)
            inbox.list_messages_from_sender(sender_address)
            # Step 3: ask the user for the index of the email
            email_index = int(input("Please enter the index of the email that you would like to read\n:"))
            # Step 4: display the email
            inbox.get_email(sender_address,email_index)
            pass
        elif user_choice == "m":
            # Mark an email as spam
            # Step 1: show emails from the sender
            sender_address = input("Please enter the address of the sender of the email\n:")

            # Step 2: show all emails from this sender (with indexes)
            inbox.list_messages_from_sender(sender_address)
            # Step 3: ask the user for the index of the email
            email_index = int(input("Please enter the index of the email to be marked as spam\n:"))

            # Step 4: mark the email as spam
            inbox.mark_as_spam(sender_address,email_index)
            # Step 5: print a success message
            print("Email has been marked as spam")

            pass
        elif user_choice == "gu":
            # List all unread emails
            print("Unread emails: \n")
            inbox.get_unread_emails()
            pass
        elif user_choice == "gs":
            # List all spam emails
            print("Spam emails: \n")
            inbox.get_spam_emails()
            pass
        elif user_choice == "e":
            print("Goodbye")
            break
        elif user_choice == "d":
            # Delete an email
            # Step 1: show emails from the sender
            sender_address = input("Please enter the address of the sender of the email\n:")

            # Step 2: show all emails from this sender (with indexes)
            inbox.list_messages_from_sender(sender_address)
            # Step 3: ask the user for the index of the email
            email_index = int(input("Please enter the index of the email to be deleted\n:"))

            # Step 4: delete the email
            inbox.delete(sender_address,email_index)
            # Step 5: print a success message
            print("Email has been deleted")

            pass
        else:
            print("Oops - incorrect input")
