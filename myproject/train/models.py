from django.db import models
from django.db import transaction




class TrainUnit(models.Model):
    """Базовий клас для всіх одиниць поїзда (локомотив та вагони)"""
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, unique=True)
    previous_unit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='next_unit_rel')
    next_unit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='previous_unit_rel')

    def __str__(self):
        return f"{self.name} ({self.number})"

    def save(self, *args, **kwargs):
        # Викликаємо валідацію перед збереженням
        self.full_clean()
        super().save(*args, **kwargs)

        # Оновлюємо зворотні зв'язки після збереження
        self._update_reverse_links()
    def _update_reverse_links(self):
        """
        Оновлює зворотні зв'язки для підтримання симетрії
        """



        """
        Якщо у нашого об'єкту попередня одиниця змінилась на None, то потрібно від'єднати стару попередню одиницю від нас (якщо вона існує)
        Аналогічно для наступної одиниці. Це потрібно для підтримання цілісності даних, щоб не було "завислих" зв'язків, коли одна одиниця вказує на іншу,
        але та не вказує на неї у відповідь.
        """
        if self.pk:  # існуючий об'єкт
            old = TrainUnit.objects.filter(pk=self.pk).first()
            if old:
                if old.previous_unit and self.previous_unit is None:
                    old.previous_unit.next_unit = None
                    old.previous_unit.save(update_fields=["next_unit"])
                if old.next_unit and self.next_unit is None:
                    old.next_unit.previous_unit = None
                    old.next_unit.save(update_fields=["previous_unit"])

        # Якщо є previous_unit, встановлюємо його next_unit на self
        if self.previous_unit:
            if self.previous_unit.next_unit != self:
                #забороняємо приєднання якщо існує зв'язок з іншим об'єктом
                if self.previous_unit.next_unit:
                    self.previous_unit = None
                    self.save(update_fields=['previous_unit'])
                else:

                    self.previous_unit.next_unit = self
                    # Зберігаємо без виклику сигналів, щоб уникнути рекурсії
                    self.previous_unit.save(update_fields=['next_unit'])

        # Якщо є next_unit, встановлюємо його previous_unit на self
        if self.next_unit:
            if self.next_unit.previous_unit != self:
                #забороняємо приєднання якщо існує зв'язок з іншим об'єктом
                if self.next_unit.previous_unit:
                    self.next_unit = None
                    self.save(update_fields=['next_unit'])
                else:
                    self.next_unit.previous_unit = self
                    self.next_unit.save(update_fields=['previous_unit'])
    def get_available_previous_units(self):
        """
        OK
        Повертає одиниці, які можна приєднати як previous_unit
        (мають вільний next_unit і не в одному ланцюжку з поточною)
        """
        # Виключаємо себе
        units = TrainUnit.objects.exclude(pk=self.pk)

        # Фільтруємо ті, що мають вільний next_unit
        available = units.filter(next_unit__isnull=True)

        # Виключаємо одиниці, які вже в одному ланцюжку з поточною
        chain_units = self.get_chain_units()
        available = available.exclude(pk__in=chain_units.values_list('pk', flat=True))

        return available

    def get_available_next_units(self):
        """
        OK
        Повертає одиниці, які можна приєднати як next_unit
        (мають вільний previous_unit і не в одному ланцюжку з поточною)
        """
        # Виключаємо себе
        units = TrainUnit.objects.exclude(pk=self.pk)

        # Фільтруємо ті, що мають вільний previous_unit
        available = units.filter(previous_unit__isnull=True)

        # Виключаємо одиниці, які вже в одному ланцюжку з поточною
        chain_units = self.get_chain_units()
        available = available.exclude(pk__in=chain_units.values_list('pk', flat=True))

        return available

    def get_chain_units(self):
        """
        OK
        Повертає всі одиниці в одному ланцюжку з поточною
        """
        chain = set()
        current = self

        # Йдемо назад по ланцюжку
        while current.previous_unit:
            chain.add(current.previous_unit)
            current = current.previous_unit

        # Йдемо вперед по ланцюжку
        current = self
        while current.next_unit:
            chain.add(current.next_unit)
            current = current.next_unit

        return TrainUnit.objects.filter(pk__in=[unit.pk for unit in chain])

    def can_attach_previous(self, unit):
        """
        WARNING
        Перевіряє, чи можна приєднати unit як previous_unit
        """
        if unit == self:
            return False
        if unit.next_unit is not None:
            return False
        # ////
        if unit in self.get_chain_units():
            return False
        # ////
        return True

    def can_attach_next(self, unit):
        """
        WARNING
        Перевіряє, чи можна приєднати unit як next_unit
        """
        if unit == self:
            return False
        if unit.previous_unit is not None:
            return False
        # ////
        if unit in self.get_chain_units():
            return False
        # ////
        return True

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


class Carriage(TrainUnit,models.Model):
    """Вагон - причепна одиниця поїзда"""
    image = models.ImageField(upload_to='carriage_images/', blank=True, default='carriage_images/default.png')
    def __str__(self):
        return f"Вагон {self.name} ({self.number})"