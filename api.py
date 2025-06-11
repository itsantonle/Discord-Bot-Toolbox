import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        print(f"🌟 \"{quote}\"\n— {author}")
    else:
        print("Failed to fetch quote.")

get_quote()
