# Subdomain Finder

This Python script uses Google to find subdomains for a given domain.

# Usage

Clone the repository:

- git clone https://github.com/bulletproofmedic/subdomain-finder.git

# Navigate to the cloned repository:

- cd subdomain-finder

# Run the script with Python:

- python subdomain_finder.py

`When you run the script, it will prompt you to enter a URL in the format of a Fully Qualified Domain Name (FQDN), such as example.com. You do not need to provide the protocol or the 'www.'`

- The script will then confirm the Top-Level Domain (TLD) with you. If you confirm, the script will proceed to find subdomains for the given domain using Google. If you do not confirm, or if the URL you entered does not match a FQDN, the script will prompt you to try again.

# Requirements

- Python 3

- requests module

# Installation

To install the required Python module, run:

- pip install requests
