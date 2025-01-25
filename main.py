# Import required libraries
from dotenv import load_dotenv  # For loading environment variables from a .env file
import imaplib  # For connecting to and interacting with an IMAP email server
import email  # For handling email messages
import os  # For interacting with the operating system and environment variables
from bs4 import BeautifulSoup  # For parsing and extracting content from HTML
import requests  # For making HTTP requests

# Load environment variables from the .env file
load_dotenv()

# Fetch email and password from environment variables
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Function to connect to the email server
def connect_to_mail():
    # Create a secure connection to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    # Log in to the email account using the provided credentials
    mail.login(username, password)
    # Select the inbox folder to fetch emails
    mail.select("inbox")
    return mail

# Function to extract all "unsubscribe" links from the given HTML content
def extract_links_from_html(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    # Find all links with "unsubscribe" in their href attribute
    links = [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]
    return links

# Function to visit a given link (HTTP GET request)
def click_link(link):
    try:
        # Send a GET request to the link
        response = requests.get(link)
        # Check if the request was successful
        if response.status_code == 200:
            print("Successfully visited", link)
        else:
            print("Failed to visit", link, "error code", response.status_code)
    except Exception as e:
        # Handle any exceptions that occur during the request
        print("Error with", link, str(e))

# Function to search for emails containing "unsubscribe" links
def search_for_email():
    # Connect to the email server
    mail = connect_to_mail()
    # Search for emails containing the word "unsubscribe" in their body
    _, search_data = mail.search(None, 'TEXT "unsubscribe"')
    data = search_data[0].split()  # Get a list of email IDs matching the search criteria

    links = []  # Initialize an empty list to store links

    # Loop through each email ID
    for num in data:
        # Fetch the email data
        _, data = mail.fetch(num, "(RFC822)")
        # Parse the email message from bytes
        msg = email.message_from_bytes(data[0][1])

        # Check if the email has multiple parts (e.g., text and HTML)
        if msg.is_multipart():
            # Loop through each part of the email
            for part in msg.walk():
                # Check if the part is of type "text/html"
                if part.get_content_type() == "text/html":
                    # Decode and extract the HTML content
                    html_content = part.get_payload(decode=True).decode(errors="replace")
                    # Extract "unsubscribe" links from the HTML content
                    links.extend(extract_links_from_html(html_content))
        else:
            # For single-part emails, extract content type and payload
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode(errors="replace")

            # If the content type is "text/html", extract links
            if content_type == "text/html":
                links.extend(extract_links_from_html(content))

    # Logout from the email server
    mail.logout()
    return links

# Function to save the extracted links to a file
def save_links(links):
    with open("links.txt", "w") as f:
        # Write each link on a new line in the file
        f.write("\n".join(links))

# Extract unsubscribe links from the emails
links = search_for_email()

# Visit each extracted link
for link in links:
    click_link(link)

# Save the extracted links to a file
save_links(links)