from dotenv import load_dotenv
import os
from shodan_search import ShodanSearch

def main():
    load_dotenv()
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

    shodan_search = ShodanSearch(SHODAN_API_KEY)

    search_results = shodan_search.search("title:dvwa", page = 1)

    for i in range (10):
        print(f"\n Results {i}")
        print(f"IP: {search_results['matches'][i]['ip_str']}")
        print(f"HOSTNAMES: {search_results['matches'][i]['hostnames']}")
        print(f"LOCATION: {search_results['matches'][i]['location']}")



if __name__== "__main__":
    main()
