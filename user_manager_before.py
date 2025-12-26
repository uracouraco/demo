# ユーザー管理システム
users = []

def register_user(username, password):
    # 変数名が短すぎる問題
    u = {
        'username': username,
        'password': password  # パスワードをそのまま保存（セキュリティ問題）
    }
    users.append(u)
    return True

def get_user(username):
    # エラーハンドリングが不十分
    for user in users:
        if user['username'] == username:
            return user
    
def login(username, password):
    user = get_user(username)
    # None チェックが不足
    if user['password'] == password:
        return True
    return False
