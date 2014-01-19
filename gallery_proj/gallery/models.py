from django.db import models

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length = 200)
	website = models.URLField(max_length = 200)
	profile_pic = models.FileField(upload_to = 'profile_pics/')
	biography = models.TextField()
	picture_1 = models.FileField(upload_to = 'artists/%Y.%m.%d.%H.%M.%S')
	picture_2 = models.FileField(upload_to = 'artists/%Y.%m.%d.%H.%M.%S')
	picture_3 = models.FileField(upload_to = 'artists/%Y.%m.%d.%H.%M.%S')
	picture_4 = models.FileField(upload_to = 'artists/%Y.%m.%d.%H.%M.%S')
	picture_5 = models.FileField(upload_to = 'artists/%Y.%m.%d.%H.%M.%S')
	picture_6 = models.FileField(upload_to = 'artists/%Y.%m.%d.%H.%M.%S')
