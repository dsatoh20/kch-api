import secrets
from django.conf import settings
from rest_framework import permissions

class HasApiKeyForPost(permissions.BasePermission):
    """
    POSTリクエストに対してのみ、X-API-Keyヘッダーの検証を行う権限クラス
    """
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS のような安全なメソッドは常に許可する
        if request.method in permissions.SAFE_METHODS:
            return True

        # POSTリクエストの場合のみ、APIキーの検証を行う
        if request.method == 'POST':
            # リクエストヘッダーから 'X-API-Key' を取得
            # (Djangoではヘッダー名が大文字になり、'HTTP_' プレフィックスが付く)
            api_key = request.META.get('HTTP_X_API_KEY')
            
            # settingsにキーが設定されているか、かつ、リクエストでキーが送られてきたか
            if not settings.SECRET_API_KEY or not api_key:
                return False

            # タイミング攻撃対策を施した安全な文字列比較を行う
            return secrets.compare_digest(api_key, settings.SECRET_API_KEY)
        
        # 上記以外のメソッド (PUT, DELETEなど) は許可しない
        return False