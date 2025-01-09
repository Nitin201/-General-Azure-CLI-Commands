import requests

def get_random_cat_fact():
    try:
        # Fetch a random cat fact from the API
        response = requests.get("https://catfact.ninja/fact")
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            print(f"Random Cat Fact: {data['fact']}")
        else:
            print(f"Failed to fetch cat fact. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the cat fact: {e}")

if __name__ == "__main__":
    # Fetch and display a random cat fact
    get_random_cat_fact()
