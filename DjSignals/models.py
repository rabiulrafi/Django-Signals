from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
# Create your models here.
from django.dispatch import receiver

class Post(models.Model):
	title= models.CharField(max_length=50)

	def __str__(self):
		return self.title



# def save_post(sender, instance, created, **kwargs):
# 	if created:	
# 		print("Post created")
# pre_save.connect(save_post, sender=Post)


# def update_post(sender, instance, created, **kwargs):
# 	if created==False:
# 		print("Post Updated")
# pre_save.connect(update_post, sender = Post)
# @receiver(pre_save, sender=Post)
# def post_create(sender,instance, **kwargs):
# 		print("Post Created")

# @receiver(pre_save, sender=Post)
# def post_updated(sender,instance, **kwargs):
# 		print("Post Updated")


@receiver(post_save, sender=Post, dispatch_uid="my_unique_1")
def post_create(sender,instance,created, **kwargs):
	if created:
		print("Post Created")

@receiver(post_save, sender=Post, dispatch_uid="my_unique_2")
def post_updated(sender,instance, **kwargs):
		print("Post Updated")
 
@receiver(post_delete, sender=Post,  dispatch_uid="my_unique_3")
def delete_post(sender,instance,**kwargs):
		print("Post Deleted")

