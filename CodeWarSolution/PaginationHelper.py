# PaginationHelper
# Define a new constructor

class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.c = collection
        self.i = items_per_page
        
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.c)
  
    # returns the number of pages
    def page_count(self):
        return (len(self.c) // self.i) + 1
	
    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        if page_index > len(self.c) // self.i:
            return -1
        elif page_index != len(self.c) // self.i:
            return self.i
        else: 
            return len(self.c) - self.i * page_index
  
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index >= len(self.c) or item_index <0:
            return -1
        return item_index // self.i
