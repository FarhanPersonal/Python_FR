# Following mosh's lecture 5.8:

items = [("product1", 10), ("product2", 5), ("product3", 30)]


# def sort_items(item):
#     return item[1]


items.sort(key=lambda item: item[1])

print(items)
