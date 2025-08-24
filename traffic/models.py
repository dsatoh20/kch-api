from django.db import models
from club.models import Clubs

class ClickOnLink(models.Model):
    """
    各団体SNSリンクのクリックを記録する
    ClickOnLinkオブジェクトを集計することで、どのリンクがどれだけクリックされたかを把握できる
    """
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='clicks')
    link = models.CharField(max_length=200) # 遷移先
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Click on {self.club.name}"