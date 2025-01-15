from django.db import models

# Create your models here.
from neomodel import StructuredNode, StringProperty, JSONProperty

class User(StructuredNode):
    username = StringProperty(unique_index=True)
    email = StringProperty()
    preferences = JSONProperty()  # Może przechowywać preferencje użytkownika w formacie JSON