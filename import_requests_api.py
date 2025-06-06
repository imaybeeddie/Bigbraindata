import requests


def fetch_movie_info():
   # api_key = "INPUT PERSONAL KEY"
    movie_title = input('Enter the movie title: ').strip()
    base_url = "http://www.omdbapi.com/" #Use this to access web for personal key, its free but has a limit of 1000
    params = {
        "t": movie_title,
        "apikey": api_key,
        "r": "json"
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        if data.get("Response") == "True":
            print("\n Movie Details: ")
            print(f"Title:{data.get('Title', 'N/A')}")
            print(f"Year:{data.get('Year', 'N/A')}")
            print(f"Genre:{data.get('Genre', 'N/A')}")
            print(f"Director:{data.get('Director', 'N/A')}")
            print(f"Actors:{data.get('Actors', 'N/A')}")
            print(f"Plot:{data.get('Plot', 'N/A')}")
            print(f"IMDb Rating:{data.get('Imdb Rating', 'N/A')}")
            print(f"Metascore:{data.get('Metascore', 'N/A')}")
        else:
            print(f"Error:{data.get('Error', 'Movie not found!')}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")

fetch_movie_info()