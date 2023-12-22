from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Followers(models.Model):
    followers = models.CharField(max_length=10)
    followers_img = models.ImageField(upload_to='static/images/', height_field=None, width_field=None, max_length=None, default='/static/images/travel.jpg')

    def __str__(self):
        return self.followers


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to='static/images/', height_field=None, width_field=None, max_length=None, default='/static/images/travel.jpg')

    def __str__(self):
        return self.category_name

class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    feedback_email = models.CharField(max_length=100)
    feedback_msg = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name
    

class SellAcc(models.Model):
    ac_name = models.CharField(max_length=50)
    ac_category = models.CharField(max_length=50)
    ac_followers = models.CharField(max_length=50)
    ac_age = models.CharField(max_length=50)
    ac_fullname = models.CharField(max_length=50)
    ac_email = models.CharField(max_length=50)

    def __str__(self):
        return self.ac_name
    

class InstaAccounts(models.Model):
    ac_name = models.CharField(max_length=100)
    ac_join_date = models.DateField(auto_now=False, auto_now_add=False)
    ac_rating = models.CharField(max_length=50)
    ac_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ac_follow = models.ForeignKey(Followers, on_delete=models.CASCADE, null=True)
    ac_bio = models.CharField(max_length=100)
    ac_followers = models.CharField(max_length=50)
    ac_price = models.CharField(max_length=50)
    ac_dp = models.ImageField(upload_to='static/images/sellAccount/', height_field=None, width_field=None, max_length=None, default='/static/images/travel.jpg')

    ac_info = models.CharField(max_length=500)

    ac_pic_one = models.ImageField(upload_to='static/images/sellAccount/', height_field=None, width_field=None, max_length=None, default='/static/images/travel.jpg')
    ac_pic_two = models.ImageField(upload_to='static/images/sellAccount/', height_field=None, width_field=None, max_length=None, default='/static/images/travel.jpg')
    ac_pic_three = models.ImageField(upload_to='static/images/sellAccount/', height_field=None, width_field=None, max_length=None, default='/static/images/travel.jpg')


    def __str__(self):
        return self.ac_name

    
class Sociallinks(models.Model):
    facebook_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    razor_pay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razor_pay_payment_signature = models.CharField(max_length=500, null=True, blank=True)

    sell_ac = models.ForeignKey(InstaAccounts, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.razor_pay_order_id

