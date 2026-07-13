import requests

def get_cat_fact():

    try: 
        url = "https://catfact.ninja/fact"
        # Write your code here
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cat_fact = data.get("fact")

        #if cat_fact is None:
           # print("The 'fact' field is missing in the response.")
      #  else:
           # print("Cat fact: ", cat_fact)

   # except requests.exceptions.RequestException as e: 
           # print("Error:", e)
   # except ValueError: 
      #  print("Failed to decode JSON from the response.")

        if not cat_fact:
            raise Exception()
        print(cat_fact)
            
    except Exception:
        print("Failed to retrieve cat fact.")

get_cat_fact()
