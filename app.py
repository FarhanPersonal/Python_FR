# Following mosh's lecture 5.7:

items = [("product1", 10), ("product2", 5), ("product3", 30)]


def sort_items(item):
    return item[1]


items.sort(key=sort_items)

print(items)
