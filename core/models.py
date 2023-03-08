from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    # Connect the profile to the authenticated user via foreign key
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # ID that acts as the primary key
    id_user = models.IntegerField(unique=True)

    # Set bio to a text field with the option to be empty
    bio = models.TextField(blank=True)

    # Get profile uploaded picture and save it in the media folder under the folder "profile_images"
    # If the user doesn't upload a profile picture, then use the default blank-pp profile image
    # The blank-pp image can be found in media
    profile_image = models.ImageField(upload_to='profile_images', default="blank-pp.png")

    total_likes = models.IntegerField(default=0)
    happy_likes = models.IntegerField(default=0)
    angry_likes = models.IntegerField(default=0)
    sad_likes = models.IntegerField(default=0)
    shocked_likes = models.IntegerField(default=0)


class Post(models.Model):
    # Connect the post to the authenticated user via foreign key
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # ID that acts as the primary key
    post_id = models.IntegerField(unique=True)

    post_image = models.ImageField(upload_to='profile_images')

    happy_likes = models.IntegerField(default=0)
    angry_likes = models.IntegerField(default=0)
    sad_likes = models.IntegerField(default=0)
    shocked_likes = models.IntegerField(default=0)


class Comment(models.Model):
    # Connect the comment to the post via foreign key
    post = models.ForeignKey(Post, to_field='post_id', on_delete=models.CASCADE)

    # Connect the comment to the authenticated user via foreign key
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # ID that acts as the primary key
    comment_id = models.IntegerField(unique=True)

    comment = models.TextField()
