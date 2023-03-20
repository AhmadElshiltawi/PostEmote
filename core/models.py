from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
import uuid


class Profile(models.Model):

    # Connect the profile to the authenticated user via foreign key
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # ID that acts as the primary key
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Get profile uploaded picture and save it in the media folder under the folder "profile_images"
    # If the user doesn't upload a profile picture, then use the default blank-pp profile image
    # The blank-pp image can be found in media
    profile_image = models.ImageField(upload_to='profile_images', default="blank-pp.png")

class Post(models.Model):

    # ID that acts as the primary key
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Connect the post to the authenticated user via foreign key
    profile = models.ForeignKey(Profile, to_field='u_id', on_delete=models.CASCADE, blank=True, null=True)

    post_image = models.ImageField(upload_to='post_images')
    
    created = models.DateTimeField(default=timezone.now)

    happy_likes = models.IntegerField(default=0)
    angry_likes = models.IntegerField(default=0)
    sad_likes = models.IntegerField(default=0)
    shocked_likes = models.IntegerField(default=0)

class SuprisedReact(models.Model):
    superised_react_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    post = models.ForeignKey(Post, to_field='post_id', on_delete=models.CASCADE, blank=True, null=True)
    
    profile = models.ForeignKey(Profile, to_field='u_id', on_delete=models.CASCADE, blank=True, null=True)
    
class HappyReact(models.Model):
    happy_react_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    post = models.ForeignKey(Post, to_field='post_id', on_delete=models.CASCADE, blank=True, null=True)
    
    profile = models.ForeignKey(Profile, to_field='u_id', on_delete=models.CASCADE, blank=True, null=True)
    
class AngryReact(models.Model):
    angry_react_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    post = models.ForeignKey(Post, to_field='post_id', on_delete=models.CASCADE, blank=True, null=True)
    
    profile = models.ForeignKey(Profile, to_field='u_id', on_delete=models.CASCADE, blank=True, null=True)
    
class SadReact(models.Model):
    sad_react_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    post = models.ForeignKey(Post, to_field='post_id', on_delete=models.CASCADE, blank=True, null=True)
    
    profile = models.ForeignKey(Profile, to_field='u_id', on_delete=models.CASCADE, blank=True, null=True)
    
class Comment(models.Model):
    # ID that acts as the primary key
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Connect the comment to the post via foreign key
    post = models.ForeignKey(Post, to_field='post_id', on_delete=models.CASCADE, blank=True, null=True)

    # Connect the comment to the authenticated user via foreign key
    profile = models.ForeignKey(Profile, to_field='u_id', on_delete=models.CASCADE, blank=True, null=True)
    
    reaction = models.TextField()

    comment = models.TextField()