from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    is_active = models.BooleanField(_("Active"), default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(class)s_created")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="%(class)s_updated")

    class Meta:
        abstract = True

class Country(BaseModel):
    name = models.CharField(_("Country Name"), max_length=50)
    phone_code = models.PositiveIntegerField(_("Phone Code"))

class User(BaseModel):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("Email"))

class CreditCardBrand(BaseModel):
    name = models.CharField(_("Brand Name"), max_length=50)

class Bank(BaseModel):
    name = models.CharField(_("Bank Name"), max_length=50)

class Rights(BaseModel):
    name = models.CharField(_("Rights Name"), max_length=50)

class Carrier(BaseModel):
    name = models.CharField(_("Carrier Name"), max_length=50)

class Rating(BaseModel):
    stars_number = models.IntegerField(_("Stars Number"))


class MainCateg(BaseModel):
    name = models.CharField(_("Main Category Name"), max_length=50)

    class Meta:
        verbose_name = _("Main Category")
        verbose_name_plural = _("Main Categories")

    def __str__(self):
        return self.name

class SubCateg(BaseModel):
    name = models.CharField(_("Sub Category Name"), max_length=50)

class Size(BaseModel):
    value = models.CharField(_("Size Value"), max_length=20)

class Color(BaseModel):
    name = models.CharField(_("Color Name"), max_length=20)

class Brand(BaseModel):
    name = models.CharField(_("Brand Name"), max_length=50)

class Product(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(_("Product Name"), max_length=100)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_("Stock"))
    description = models.TextField(_("Description"), blank=True)

class State(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states")
    name = models.CharField(_("State Name"), max_length=100)

class City(BaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(_("City Name"), max_length=50)

class Purchase(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE, related_name="purchases")
    waybill_number = models.CharField(_("Waybill Number"), max_length=100)

class PurchaseOrder(BaseModel):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Quantity"))

class Favorite(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorited_by")

class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    headline = models.CharField(_("Headline"), max_length=50)
    comment = models.TextField(_("Comment"))

class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    info = models.TextField(_("Address Info"))

class CreditCard(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="credit_cards")
    brand = models.ForeignKey(CreditCardBrand, on_delete=models.CASCADE)
    number = models.CharField(_("Card Number"), max_length=20)

class BankAccount(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bank_accounts")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_number = models.CharField(_("Account Number"), max_length=20)

class PhoneNumber(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="phone_numbers")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    number = models.CharField(_("Phone Number"), max_length=20)

class UserRights(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rights")
    rights = models.ForeignKey(Rights, on_delete=models.CASCADE)

class ProductSize(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

class ProductColor(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

class MenuType(BaseModel):
    category = models.OneToOneField(
        MainCateg, 
        on_delete=models.CASCADE, 
        related_name="menu_type",  
        primary_key=True
    )
    options = models.JSONField(_("Options"))

    class Meta:
        verbose_name = _("Menu Type")
        verbose_name_plural = _("Menu Types")

    def __str__(self):
        return f"Menu for {self.category.name}"