class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def __str__(self):
        customer = f"User: {self.user}\n"
        items = ""
        for item in self.products:
            items += f"{item.name}: {self.products.get(item)} pcs.\n"
        return f"{customer}Items:\n{items}"

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item in self.products:
            total += item.price * self.products[item]
        return total


