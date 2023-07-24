# ①辞書を作成
my_dict = {"name": "John", "age": 25, "city": "Tokyo"}
print(f"Original dictionary: {my_dict}")

# ②アクセス: 辞書の要素には、そのキーを使ってアクセス
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict['age']}")
print(f"City: {my_dict['city']}")

# ③変更: 辞書の要素は、キーを使って変更することが可能
my_dict['age'] = 26
print(f"Dictionary after change: {my_dict}")

# ③追加: 新たなキーと値のペアを辞書に追加することが可能
my_dict['profession'] = 'Software Developer'
print(f"Dictionary after adding a new key-value pair: {my_dict}")

# ③削除: 辞書からキーと値のペアを削除することが可能
del my_dict['city']
print(f"Dictionary after deletion: {my_dict}")
