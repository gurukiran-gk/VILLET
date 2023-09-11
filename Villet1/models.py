from django.db import models

class VilletUser(models.Model):
    userid = models.AutoField(primary_key=True,)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, unique=True) 
    dob = models.CharField(max_length=20,default='01/01/2000')
    gender = models.CharField(max_length=128,default=00)
    perm_adr = models.CharField(max_length=328,default=00)
    temp_adr = models.CharField(max_length=328,default=00)
    city = models.CharField(max_length=128,default=00)
    state = models.CharField(max_length=128,default=00)
    pan=models.CharField(max_length=98,default=00,)
    aadhar=models.CharField(max_length=12,default=00)
    occn=models.CharField(max_length=98,default=00)
    anninc=models.CharField(max_length=98,default=00)
    exc_cre=models.CharField(max_length=98,default=00)
    c_b_name = models.CharField(max_length=98,default=00)
    designation = models.CharField(max_length=98,default=00)
    no_of_yemp=models.CharField(max_length=98,default=00)
    active_number = models.IntegerField(default=0)


    def __str__(self):
        return self.username

class ActiveCreditCard(models.Model):

    userid = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=70)
    active_numberAV = models.IntegerField(default=0)
    credit_limit = models.DecimalField(max_digits=9, decimal_places=2)
    credit_score = models.IntegerField(default=600)
    credit_points = models.IntegerField(default=300)
    card_number = models.CharField(max_length=16, unique=True)
    last_bill_date = models.DateField(auto_now_add=True)
    new_bill_date = models.DateField(auto_now_add=True)
    Bill_paid = models.IntegerField(default=0)

    def generate_card_number(self):
        # Calculate the card number based on the user_id and starting value
        card_number = str(2000300040005000 + self.userid - 1)
        return card_number

    def save(self, *args, **kwargs):
        if not self.card_number:
            self.card_number = self.generate_card_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"User ID: {self.userid}, Card Number: {self.card_number}"



class VUTransaction(models.Model):
    
    transaction_id = models.AutoField(primary_key=True)
    Transaction_Name= models.CharField(max_length=100,default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    date_time = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=30,default=0)
    Receiver_Account_Number = models.CharField(max_length=30,default=0)
    Villet_Credit_Card_Number = models.CharField(max_length=30,default=0)
    Periodic_Transaction = models.CharField(max_length=30,default=0)
    Duration = models.CharField(max_length=30,default=0)
    active = models.CharField(max_length=30,default="active") 


    def __str__(self):
        return self.transaction_id




