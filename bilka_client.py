import requests
import json
from typing import List, Dict, Any, Optional

class BilkaClient:
    def __init__(self):
        self.base_url = "https://f9vbjlr1bk-dsn.algolia.net/1/indexes/*/queries"
        self.headers = {
            "x-algolia-api-key": "1deaf41c87e729779f7695c00f190cc9",
            "x-algolia-application-id": "F9VBJLR1BK",
            "content-type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"
        }

    def search_products(
        self,
        query: str = "*",
        hits_per_page: int = 50,
        store_id: int = 1654,
        object_ids: Optional[List[str]] = None,
        attributes_to_retrieve: List[str] = None,
        facets: List[str] = None
    ) -> Dict[str, Any]:
        """
        Search for products in Bilka To Go
        
        Args:
            query: Search query string
            hits_per_page: Number of results per page
            store_id: Store ID to search in
            object_ids: List of specific product IDs to search for
            attributes_to_retrieve: List of attributes to return
            facets: List of facets to return
            
        Returns:
            Dict containing search results
        """
        if attributes_to_retrieve is None:
            attributes_to_retrieve = ["*"]
        if facets is None:
            facets = ["*"]
            
        # Build the filter string
        filters = []
        if object_ids:
            filters.append(f"({' OR '.join(f'objectID:{id}' for id in object_ids)})")
        filters.append(f"isInAssortmentIn:{store_id}")
        filters.append(f"inStockStore:{store_id}")
        filters.append("nonsearchable:false")
        
        # Build the request body
        requests_list = [
            #{
            #    "indexName": "prod_qs_BILKATOGO_PRODUCT",
            #    "params": f"query={query}&hitsPerPage=5&filters=&attributesToRetrieve={json.dumps(attributes_to_retrieve)}&facets={json.dumps(facets)}&distinct=false&clickAnalytics=true&getRankingInfo=false"
            #},
            # {
            #     "indexName": "crawler_bilkatogo_content_pages",
            #     "params": f"query={query}&hitsPerPage=2&filters=&attributesToRetrieve={json.dumps(attributes_to_retrieve)}&facets={json.dumps(facets)}&distinct=false&clickAnalytics=true&getRankingInfo=false"
            # },
            {
                "indexName": "prod_BILKATOGO_PRODUCTS",
                "params": f"query={query}&hitsPerPage={hits_per_page}&filters={' AND '.join(filters)}&attributesToRetrieve={json.dumps(attributes_to_retrieve)}&facets={json.dumps(facets)}&distinct=false&clickAnalytics=true&getRankingInfo=true"
            }
        ]
        
        data = {
            "requests": requests_list,
            "strategy": "none"
        }
        
        response = requests.post(
            self.base_url,
            headers=self.headers,
            params={"x-algolia-agent": "Algolia for JavaScript (4.14.3); Browser"},
            data=json.dumps(data)
        )
        
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
    client = BilkaClient()
    
    # Example 1: Search for all products in store 1654
    #results = client.search_products()
    #print(json.dumps(results, indent=2))
    
    # Example 2: Search for specific products
    #specific_products = client.search_products(
    #    object_ids=["19687", "86696", "53366"],
    #    hits_per_page=3
    #)
    #print(json.dumps(specific_products, indent=2)) 

    # Example 3: Search for specific products
    specific_products = client.search_products(
        query="kage",
        hits_per_page=3,
        attributes_to_retrieve=["name"]
    )
    print(json.dumps(specific_products, indent=2))