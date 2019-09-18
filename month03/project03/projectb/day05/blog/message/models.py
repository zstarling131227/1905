from django.db import models

from topic.models import Topic
from user.models import UserProfile


# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=50, verbose_name='留言内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='留言创建时间')
    parent_message = models.IntegerField(default=0)
    publisher_id = models.ForeignKey(UserProfile, max_length=10, verbose_name='留言的发布者')
    topic_id = models.ForeignKey(Topic, max_length=10, verbose_name='文章')

    class Meta:
        db_table = 'message'
