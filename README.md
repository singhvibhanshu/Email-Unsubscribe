# Unsubscribe Link Extractor

## Overview
This project provides a Python script to extract and interact with "unsubscribe" links from emails in your inbox. The script connects to your email account, searches for emails containing the word "unsubscribe," extracts the links, and visits them to simulate unsubscribing from mailing lists. Additionally, it saves the links to a text file for reference.

## Features
- Connects to your email inbox using IMAP.
- Searches for emails containing "unsubscribe" links.
- Extracts links from the HTML content of emails.
- Visits the unsubscribe links to simulate the action.
- Saves all extracted links to a `links.txt` file.

## Requirements
- Python 3.x
- A Gmail account (or any other IMAP-supported email service).
- The following Python libraries:
  - `dotenv`
  - `imaplib`
  - `email`
  - `os`
  - `beautifulsoup4`
  - `requests`

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Dependencies
Ensure you have all required libraries installed. Run the following command:
```bash
pip install -r requirements.txt
```
> **Note:** If `requirements.txt` is not available, manually install the libraries using pip.

### 3. Create a `.env` File
Create a `.env` file in the project directory and add the following environment variables:
```
EMAIL=your_email@example.com
PASSWORD=your_email_password
```
> **Important:** Replace `your_email@example.com` and `your_email_password` with your actual email credentials. Enable "Less Secure App Access" in your email account settings if required (for Gmail, refer to [this guide](https://support.google.com/accounts/answer/6010255?hl=en)).

## Usage

### Run the Script
Execute the script to extract and interact with unsubscribe links:
```bash
python script.py
```

### Output
1. The script will visit each unsubscribe link and print the status (success or error).
2. All extracted links will be saved in a file named `links.txt` in the project directory.

## How It Works
1. **Environment Variables:**
   - Loads email credentials from the `.env` file.

2. **Email Connection:**
   - Connects to the email server using IMAP.
   - Logs into the inbox with the provided credentials.

3. **Email Search and Parsing:**
   - Searches for emails containing "unsubscribe" in their body.
   - Parses email content to find HTML parts.
   - Extracts links containing "unsubscribe" from the HTML content.

4. **Link Interaction:**
   - Visits each extracted link using an HTTP GET request.
   - Logs the success or failure of visiting each link.

5. **Saving Links:**
   - Stores all extracted links in a file named `links.txt`.

## Example Output
### Console Output:
```
Successfully visited https://example.com/unsubscribe
Failed to visit https://example.com/unsubscribe2 error code 404
Error with https://example.com/unsubscribe3 ConnectionError
```

### Links File (`links.txt`):
```
https://example.com/unsubscribe
https://example.com/unsubscribe2
https://example.com/unsubscribe3
```

## Security Note
- **Do not share your `.env` file or credentials publicly.**
- For production use, consider using OAuth or app-specific passwords instead of plain text credentials.

## Contributing
Contributions are welcome! If you'd like to improve the script, please fork the repository and submit a pull request.

## Disclaimer
This script is intended for educational purposes only. Use it responsibly and ensure you comply with the terms of service of your email provider.

