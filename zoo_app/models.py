from django.db import models

# Create your models here.
from django.db import models
from datetime import date

# こちらでテーブルの中身を定義します
class Animal(models.Model):
    # DBのカラムに相当する部分の定義
    id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=64)
    update_date_time = models.DateField(default=date.today)

    # モデルに関する関数をここで定義
    def register(self):
        self.update_date_time = date.today()
        self.save()

    # 管理画面に表示方法を定義
    def __str__(self):
        return '%d: %s' % (self.id, self.name)

class AnimalInfo(models.Model):
    categories = (
        (0, '説明'),
        (1, 'リンク'),
    )
    # DBのカラムに相当する部分の定義
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    category = models.IntegerField(choices=categories, default=0)
    titele = models.CharField(max_length=32)
    content = models.TextField()
    disp_order_no = models.IntegerField(default=0)
    update_date_time = models.DateField(default=date.today)

    # モデルに関する関数をここで定義
    def register(self):
        self.update_date_time = date.today()
        self.save()

    # 管理画面に表示方法を定義
    def __str__(self):
        return '%s, %d, %s, %d, %s:%s' % (self.update_date_time.strftime('%Y-%m-%d'), self.id, self.animal.name, self.category, self.titele, self.content)