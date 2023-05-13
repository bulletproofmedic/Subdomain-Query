# Import necessary modules
import requests
import re

def validate_fqdn(url):
    """Validates the format of a FQDN (Fully Qualified Domain Name)"""
    pattern = r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$"
    if re.match(pattern, url):
        return True
    else:
        return False

# Step 1: Accept and validate the URL from the user
while True:
    url = input("Please enter a URL in the format of a FQDN (e.g., example.com): ")
    if validate_fqdn(url):
        tld_confirm = input(f"You entered {url}. Is this correct? (y/n): ")
        if tld_confirm.lower() == 'y':
            break
        else:
            print("Please try again.")
    else:
        print("The input does not match the format of a FQDN. Please try again.")

# Step 2: Define the base query and query it on Google
base_query = f"site:*.{url} -www"
response = requests.get(f"https://www.google.com/search?q={base_query}")

# Step 3: Extract subdomain names from the search results
subdomains = set(re.findall(r"^(?:https?://)?([\w-]+)\.{url}", response.text, re.MULTILINE))

# Step 4: Append subdomain names to the base query and query again
while subdomains:
    sub = subdomains.pop()  # Extract a subdomain
    query = f"{base_query} -{sub}"  # Update the query
    response = requests.get(f"https://www.google.com/search?q={query}")  # Make a new request

    # Extract new subdomain names from the search results
    new_subdomains = set(re.findall(r"^(?:https?://)?([\w-]+)\.{url}", response.text, re.MULTILINE))

    # Add new subdomain names to the set and repeat the loop
    subdomains.update(new_subdomains)

# Step 5: Do something with the search results for the current query
print(f"Search results for {query}:")
print(response.text)
