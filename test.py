import requests

def test_google_search_api(api_key, cse_id, query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        search_results = response.json()
        print("Search results:", search_results)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print("Response content:", response.text)  # Add this line
    except Exception as err:
        print(f"Other error occurred: {err}")

# Replace with your actual API key and CSE ID
GOOGLE_SEARCH_API_KEY = 'AIzaSyB8w9IW7YVCskQE_DoAaW1-u2_MANrQt6Q'
GOOGLE_CSE_ID = '35849bae0e0b8486c'
query = 'tìm kiếm thông tin tổng bí thư việt nam hiện tại là ai'

test_google_search_api(GOOGLE_SEARCH_API_KEY, GOOGLE_CSE_ID, query)