from django.db import models

# Create your models here.

'''
Creadted model name contactform to get user input
'''

class contactform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=800, blank=False)
    
    def __str__(self):
        return self.subject
    
'''
Creadted model name QuesModel for Quiz-1

'''
    
class QuesModel(models.Model):
    question = models.CharField(max_length=200, blank=False)
    op1 = models.CharField(max_length=200, blank=False)
    op2 = models.CharField(max_length=200, blank=False)
    op3 = models.CharField(max_length=200, blank=False)
    op4 = models.CharField(max_length=200, blank=False)
    ans = models.CharField(max_length=200, blank=False)
    hint = models.CharField(max_length=500, blank=False)
    
    '''
    Creadted class Meta to display data base table name as Quiz_One_Questions
      
    '''
    
    class Meta:
        db_table = "Quiz_One_Questions"
        
    '''
    Creadted a function named __str__ to identify the row with its question
      
    '''
    
    def __str__(self):
        return self.question
  
'''
Creadted model name QuesModelTwo for Quiz-2

'''  

class QuesModelTwo(models.Model):
    question = models.CharField(max_length=200, blank=False)
    op1 = models.CharField(max_length=200, blank=False)
    op2 = models.CharField(max_length=200, blank=False)
    op3 = models.CharField(max_length=200, blank=False)
    op4 = models.CharField(max_length=200, blank=False)
    ans = models.CharField(max_length=200, blank=False)
    hint = models.CharField(max_length=500, blank=False)
    
    '''
    Creadted class Meta to display data base table name as Quiz_Two_Questions
      
    '''
    
    class Meta:
        db_table = "Quiz_Two_Questions"
        
    '''
    Creadted a function named __str__ to identify the row with its question
      
    '''

    def __str__(self):
        return self.question
    
    
'''
Creadted model name Leaderboard to store result

'''  

class Leaderboard(models.Model):
    sl_no = models.IntegerField(blank=False)
    name = models.CharField(max_length=200, blank=False)
    quiz_name = models.CharField(max_length=200, blank=False)
    total = models.CharField(max_length=200, blank=False)
    correct = models.CharField(max_length=200, blank=False)
    incorrect = models.CharField(max_length=200, blank=False)
    percentage = models.CharField(max_length=200, blank=False)
    
    '''
    Creadted a function named __str__ to identify the row with user name
      
    '''
    
    def __str__(self):
        return self.name
    
    '''
    Creadted class Meta to display data base table name as Quiz_Two_Questions
      
    '''
    
    class Meta:
        db_table = "Quiz_Leaderboard"
      
