# WRITE YOUR FUNCTIONS HERE
from http.client import CannotSendHeader
from io import BufferedReader
import unittest
from src.pet_shop import *

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    pet_shop["admin"]["total_cash"] == cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#def get_pets_by_breed(pet_shop, breed):
    
   # pets = []
   # for pet in pet_shop["pets"]:
     #   if "British Shorthair" == breed:
     #       pets.append(pet)
   # return pets









    





    
    







    


    

    

