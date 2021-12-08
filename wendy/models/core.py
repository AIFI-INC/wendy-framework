from tortoise.models import Model
from tortoise import fields

__all__ = [
    'Address',
    'Building',
    'Room'
]


class Address(Model):
    id = fields.BigIntField(pk=True)
    longtitude = fields.FloatField(
        description='the longtitude of the place', null=True)
    latitude = fields.FloatField(
        description='the latitude of the place', null=True)
    country_code = fields.CharField(null=False, default='jp', max_length=5)
    post_code = fields.CharField(max_length=50, null=False)
    city = fields.CharField(max_length=255, null=True)
    province = fields.CharField(max_length=255, null=True)
    address_1 = fields.CharField(max_length=255)
    address_2 = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = 'addresses'
        unique_together = (('longtitude', 'latitude'),
                           ('country_code', 'post_code', 'address_1'))

    def __str__(self) -> str:
        return f"{self.country_code} {self.post_code} {self.province}, {self.city}, {self.address_1}, {self.address_2}"


class Building(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    address = fields.ForeignKeyField(
        model_name='models.Address', related_name='buildings', on_delete=fields.CASCADE)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        table = 'buildings'
        indexes = (('name'),)  # should change to FullTextIndex later


class Room(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255, null=True)
    building = fields.ForeignKeyField(
        model_name='models.Building', related_name='rooms', on_delete=fields.CASCADE)
    floor = fields.SmallIntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.building.name}-{self.floor}F"

    class Meta:
        table = 'rooms'
