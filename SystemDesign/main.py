

class ContentSorter:
    def __init__(self, user_data_source, content_data_source):
        self.user_data_source = user_data_source
        self.content_data_source = content_data_source

    def sort_content(self,  user_id: str, content_ids: list[str]) -> list[str]:
        """
        This method takes user_id and content_ids as input parameters
        and returns the content_ids sorted based on user preference 
        and sales boost factor.
        """
        pass

    def calculate_priority_score(self,user_score: int, sales_boost: int) -> float:
        """
        Calculate priority score based on user affection and sales boost and return a score. 
        """
        pass
    
    
class UserData:
    def get_user_affection_scores(self, user_id: str) -> dict:
        """ Fetch user preference scores by user_id.
        Example: { 'furniture': 12, 'dairy_products': 81 } """
        pass

class ContentData:
    def get_content_details(self, content_id: str) -> tuple :
        """ Fetch content category and sales-boost factor for a content_id.
        Example: ('sweets', 35) """
        pass
    
    
# Example Usage
user_data = UserData()
content_data = ContentData()
sorter = ContentSorter(user_data, content_data)

user_id = "user_1"
content_ids = ["content_1", "content_2", "content_3"]
sorted_result = sorter.sort_content(user_id, content_ids)
print(sorted_result)  # Output: Sorted list of content IDs
    

