# Define job functions or Utils.
import datetime

import requests


def print_hello():
    print("Hello, world! The time is now {}".format(datetime.datetime.now()))

def fetch(url):
    # Add error handling here.
    response = requests.get(url)
    if response.status_code == 200:
        print(f'API job for {url} executed successfully')
    else:
        print(f'API job for {url} failed with status code {response.status_code}')