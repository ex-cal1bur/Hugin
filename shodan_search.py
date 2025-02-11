import shodan

class ShodanSearch:
    
    def __init__(self, api_key):
        self.client = shodan.Shodan(api_key)

    def search (self, query, page=1):
        """"""
        try:
            results= self.client.search(query, page=page)
            return results
        except Exception as e:
            print("Shodan request error: ",e)