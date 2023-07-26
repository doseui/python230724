import re

def find_emails(text):
    # Regular expression pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Find all occurrences of email addresses in the text
    emails_found = re.findall(email_pattern, text)
    
    return emails_found

# Example usage:
text_to_search = "Hello, my email is john.doe@example.com and you can also reach me at jane_smith@gmail.com."
found_emails = find_emails(text_to_search)

print(found_emails)
