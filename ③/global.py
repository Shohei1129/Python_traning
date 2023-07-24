#グローバル変数を設定
global_var = "Global Varibale"
def get_global():
    local_var = global_var
    return local_var
print(get_global())
