from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.CharField(max_length=256)
    userImage = models.CharField(max_length=256)
    user = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    rating = models.IntegerField()
    title = models.CharField(max_length=256)
    item = models.CharField(max_length=256)
    size = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    show = models.BooleanField(default=True)
    price = models.IntegerField(choices=((10, '$10'), (20, '$20'), (30, '$30'), (40, '$40')), default=20)
    # matchId = models.CharField(max_length=256)

    def _str_(self):
        return self.itemId


# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=256)
#     email = models.CharField(max_length=256)
#     password = models.CharField(max_length=256)

#     def str(self):
#         return self.id

class Match(models.Model):
    item1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='match1')
    item2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='match2')

    created_time = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return '{}-{}'.format(self.item1, self.item2)