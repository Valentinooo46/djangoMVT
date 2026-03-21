from django.db import models




class TrainUnit(models.Model):
    """Базовий клас для всіх одиниць поїзда (локомотив та вагони)"""
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, unique=True)
    previous_unit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='next_unit_rel')
    next_unit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='previous_unit_rel')

    def __str__(self):
        return f"{self.name} ({self.number})"

    class Meta:
        ordering = ['number']

class Train(TrainUnit,models.Model):
   
    """Поїзд - основна модель, яка містить інформацію про поїзд та його одиниці"""
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    image = models.ImageField(upload_to='train_images/', blank=True, default='train_images/default.png')

    def __str__(self):
        return f"{self.name} ({self.number})"
# class Locomotive(TrainUnit):
#     """Локомотив - головна одиниця поїзда"""

#     def __str__(self):
#         return f"Локомотив {self.name} ({self.number})"


class Carriage(TrainUnit):
    """Вагон - причепна одиниця поїзда"""

    def __str__(self):
        return f"Вагон {self.name} ({self.number})"