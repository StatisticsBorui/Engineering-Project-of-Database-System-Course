from .models import *

class ShowScore(models.Model):
    stu_id_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    score1 = models.SmallIntegerField(null=True)
    score2 = models.SmallIntegerField(null=True)
    score3 = models.SmallIntegerField(null=True)

    class Meta:
        db_table = 'showscore2'
        managed = False