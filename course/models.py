from django.db import models

# Create your models here;
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50,null=True,blank=True)
    sem = models.TextField(max_length=10)
    dept = models.ForeignKey('department.Department',on_delete=models.DO_NOTHING,related_name="course_ddept")

    def __str__(self):
        return '{}{}{}{}{}'.format(self.id,self.name,self.sem,self.dept)
