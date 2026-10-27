from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    number = models.CharField(max_length=10, verbose_name="Номер столика")
    capacity = models.IntegerField(verbose_name="Количество мест")

    def __str__(self):
        return f"Столик {self.number} (Ресторан: {self.restaurant.name})"

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"


class TimeSlot(models.Model):
    STATUS_CHOICES = [
        ('free', 'Свободен'),
        ('booked', 'Занят'),
    ]
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='free', verbose_name="Статус")

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Временной слот"
        verbose_name_plural = "Временные слоты"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('cancelled', 'Отменено'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')
    slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='bookings')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Статус")

    def __str__(self):
        return f"Бронь {self.user.username} - {self.table} - {self.slot}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=255, verbose_name="Название блюда")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Меню"

