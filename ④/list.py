# ①リストの定義
my_list = [1, 2, "apple", 4.5]

# ②アクセス: 要素へのアクセスは0から始まるインデックス
print(f"Element at index 2: {my_list[2]}")

# ③append()メソッドはリストの最後に新しい要素を追加
my_list.append("banana")
print(f"After append: {my_list}")

# ③insert()メソッドは指定した位置に新しい要素を挿入
my_list.insert(1, 3.0)
print(f"After insert: {my_list}")

# ③remove()メソッドは指定した要素をリストから削除
my_list.remove(1)
print(f"After remove: {my_list}")

# ③pop()メソッドは指定した位置の要素をリストから削除し、その要素を返す
popped_element = my_list.pop(2)
print(f"After pop: {my_list}")
print(f"Popped element: {popped_element}")

# ④スライス: リストから部分リストを取得するためにスライスを使用できる
print(f"Sliced list from index 1 to 3: {my_list[1:4]}")
