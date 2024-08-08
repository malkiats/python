import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    # Email details
    from_email = 'youremail@example.com'
    password = 'yourpassword'

    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body to the MIME object
    msg.attach(MIMEText(body, 'plain'))

    # Setup the SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()  # Secure the connection
    server.login(from_email, password)

    # Send the email
    server.send_message(msg)
    print(f"Email sent to {to_email}")

    # Close the server
    server.quit()

# Example usage
send_email(
    subject='Meeting Reminder',
    body='This is a reminder for our meeting scheduled at 3 PM today.',
    to_email='recipient@example.com'
)


'''
More Advanced Automation Tasks
Python's power comes from its rich ecosystem of libraries, allowing you to automate more complex tasks. Here are some ideas:

Web Scraping:

Use requests and BeautifulSoup or Scrapy to scrape data from websites.
Excel Automation:

Use pandas or openpyxl to automate Excel tasks, such as data analysis or report generation.
Email Automation:

Use smtplib and email libraries to send automated emails.
Task Scheduling:

Use schedule or APScheduler to run scripts at specific intervals.
File Manipulation:

Use os and shutil for file operations like copying, moving, or deleting files based on conditions.
Data Analysis:

Use pandas, numpy, and matplotlib for data manipulation and visualization.
'''
