class NodeCategoryRegistry:
    def __init__(self):
        self.categories = {}

    def add_category(self, category: str):
        self.categories[category] = True  # Marker to indicate a category exists

    def category_exists(self, category: str) -> bool:
        return category in self.categories
