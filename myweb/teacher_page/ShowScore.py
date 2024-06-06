from .models import *

class ShowScoreWithClass(models.Model):
    stu_id_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    score1 = models.SmallIntegerField(null=True)
    score2 = models.SmallIntegerField(null=True)
    score3 = models.SmallIntegerField(null=True)
    class_id_id = models.SmallIntegerField()

    class Meta:
        db_table = 'showscorewithclass2'
        managed = False