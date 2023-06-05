from django.test import TestCase
from .models import *


class OrdersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Orders.objects.create(user=User.objects.filter(id=1).first(), orderType='Компьютерная диагностика двигателя', title='Диагностика', adress='Колесникова 3', price=20, time='2023-05-20T12:35', status='Active')
    def test_first_name_label(self):
        orders = Orders.objects.get(id=1)
        field_label = orders._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Title')

    def test_date(self):
        orders = Orders.objects.get(id=1)
        field_label = orders._meta.get_field('time').verbose_name
        self.assertEqual(field_label, 'Date')

    def test_title_max_length(self):
        orders = Orders.objects.get(id=1)
        max_length = orders._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_data(self):
        orders = Orders.objects.get(id=1)
        expected_object_name = f'{orders.orderType}, {orders.title}'
        self.assertEqual(f'{orders.orderType}, {orders.title}', expected_object_name)

class DetailsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Detail.objects.create(mark='Chevrolet Camaro', type='Прокладки', count=9, isAvaliable=True, price=70)
    def test_first_name_label(self):
        detail = Detail.objects.get(id=1)
        field_label = detail._meta.get_field('mark').verbose_name
        self.assertEqual(field_label, 'Mark')

    def test_date(self):
        detail = Detail.objects.get(id=1)
        field_label = detail._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'Type')

    def test_title_max_length(self):
        detail = Detail.objects.get(id=1)
        max_length = detail._meta.get_field('type').max_length
        self.assertEqual(max_length, 255)

    def test_data(self):
        detail = Detail.objects.get(id=1)
        expected_object_name = f'{detail.mark}, {detail.type}'
        self.assertEqual(f'{detail.mark}, {detail.type}', expected_object_name)


class ServicesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Services.objects.create(title='Диагностика', description='Компьютерная диагностика систем автомобиля. Компьютерная диагностика двигателя.', openDescription='Диагностика электрооборудования.', price='от 20 BYN (в некоторых случаях диагностика может проводиться бесплатно)')
    def test_first_name_label(self):
        sevice = Services.objects.get(id=1)
        field_label = sevice._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Title')

    def test_description(self):
        sevice = Services.objects.get(id=1)
        field_label = sevice._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'Description')

    def test_title_max_length(self):
        sevice = Services.objects.get(id=1)
        max_length = sevice._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_data(self):
        sevice = Services.objects.get(id=1)
        expected_object_name = f'{sevice.title}, {sevice.price}'
        self.assertEqual(f'{sevice.title}, {sevice.price}', expected_object_name)


class SuccessedOrdersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SuccessedOrders.objects.create(user=User.objects.filter(id=1).first(), order=Orders.objects.filter(id=1).first(), stars=4, feedback='qbjkqbwfjqwfqwfd')
    def test_first_name_label(self):
        sevice = SuccessedOrders.objects.get(id=1)
        field_label = sevice._meta.get_field('feedback').verbose_name
        self.assertEqual(field_label, 'Feedback')

    def test_title_max_length(self):
        sevice = SuccessedOrders.objects.get(id=1)
        max_length = sevice._meta.get_field('feedback').max_length
        self.assertEqual(max_length, 144)

    def test_data(self):
        sevice = SuccessedOrders.objects.get(id=1)
        expected_object_name = f'{sevice.feedback}, {sevice.stars}'
        self.assertEqual(f'{sevice.feedback}, {sevice.stars}', expected_object_name)