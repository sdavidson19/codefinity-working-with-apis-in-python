import requests

def print_three_cat_facts():
    # Your code goes here
        for i in range(3):
            response = requests.get("https://catfact.ninja/fact")
            data = response.json()
            cat_fact = data.get("fact")
            print(f"{cat_fact}")

print_three_cat_facts()

 