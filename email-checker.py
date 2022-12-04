import smtplib

# Define the list of email addresses to check
emails = ["user1@example.com", "user2@example.com", "user3@example.com"]

# Iterate through the list of email addresses
for email in emails:
    # Split the email address into username and domain
    username, domain = email.split("@")

    # Attempt to connect to the SMTP server for the domain
    try:
        smtp = smtplib.SMTP(f"smtp.{domain}")
    except (socket.gaierror, socket.error):
        # Email does not exist if the SMTP server cannot be found
        print(f"{email} does not exist")
    else:
        # Check if the username exists on the SMTP server
        try:
            smtp.verify(username)
        except smtplib.SMTPAuthenticationError:
            # Email does not exist if the username is invalid
            print(f"{email} does not exist")
        else:
            # Email exists if no errors are raised
            print(f"{email} exists")
