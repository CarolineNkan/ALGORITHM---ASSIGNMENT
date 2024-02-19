# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:40:01 2024

@author: User
"""

class Product:
   def __init__(self, ID, name, price, category):
       self.ID = ID
       self.name = name
       self.price = price
       self.category = category

   def __str__(self):
       return f"{self.ID} {self.name} {self.price} {self.category}"

   @staticmethod
   def load_products_array(file_path):
       products = []
       try:
           with open(file_path, "r") as file:
               for line in file:
                   ID, name, price, category = line.strip().split(",")
                   price = float(price)
                   products.append(Product(ID, name, price, category))
       except FileNotFoundError:
           print("File not found at the specified path:", file_path)
       except Exception as e:
           print("An error occurred:", e)
       return products


class Node:
   def __init__(self, product=None, next=None):
       self.product = product
       self.next = next


class LinkedList:
   def __init__(self):
       self.head = None

   def append(self, product):
       if not self.head:
           self.head = Node(product)
       else:
           current = self.head
           while current.next:
               current = current.next
           current.next = Node(product)

   def to_array(self):
       products = []
       current = self.head
       while current:
           products.append(current.product)
           current = current.next
       return products

   @staticmethod
   def load_products_linked_list(file_path):
       linked_list = LinkedList()
       with open(file_path, "r") as file:
           for line in file:
               ID, name, price, category = line.strip().split(",")
               price = float(price)
               product = Product(ID, name, price, category)
               linked_list.append(product)
       return linked_list


def insert_product_array(products_array, product):
   products_array.append(product)


def insert_product_linkedlist(linkedlist, product):
   new_node = Node(product)
   new_node.next = linkedlist.head
   linkedlist.head = new_node


def update_product_array(products_array, updated_product):
   for product in products_array:
       if product.ID == updated_product.ID:
           product.name = updated_product.name
           product.price = updated_product.price
           product.category = updated_product.category
           break


def update_product_linkedlist(linkedlist, updated_product):
   current = linkedlist.head
   while current is not None:
       if current.product.ID == updated_product.ID:
           current.product = updated_product
           break
       current = current.next


# Delete a product from the array by ID
def delete_product_array(products_array, product_id):
   products_array[:] = [product for product in products_array if product.ID != product_id]


# Delete a product from the linked list by ID
def delete_product_linkedlist(linkedlist, product_id):
   if linkedlist.head is None:
       return

   if linkedlist.head.product.ID == product_id:
       linkedlist.head = linkedlist.head.next
       return

   prev = linkedlist.head
   current = prev.next
   while current is not None:
       if current.product.ID == product_id:
           prev.next = current.next
           break
       prev = current
       current = current.next


# Search for a product in the array by ID
def search_product_array(products_array, product_id):
   for p in products_array:
       if p.ID == product_id:
           return p
   return None

# Search for a product in the linked list by ID
def search_product_linkedlist(linkedlist, product_id):
   if linkedlist.head is None:
       return None

   current = linkedlist.head
   while current is not None:
       if current.product.ID == product_id:
           return current.product
       current = current.next
   return None

#Sort by Price
def bubble_sort(arr):
   n = len(arr)
   for i in range(n-1):
       for j in range(0, n-i-1):
           if arr[j].price > arr[j+1].price:
               arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
file_path = r"C:\Users\User\Desktop\ASSIGNMENT 1\product_data.txt"

# Load product data from file (product_data.txt) into an array
products_array = Product.load_products_array(file_path)

# Load product data from a file (product_data.txt) into a LinkedList
#linked_list = LinkedList.load_products_linked_list(file_path)

# Insert a new product at the end of the array
new_product = Product("5", "Iphone13", 20.5, "Electronics")
insert_product_array(products_array, new_product)

# Insert a new product at the beginning of the linked list
#insert_product_linkedlist(linked_list, new_product)

# Update a product in the array by ID
updated_product = Product("1", "Updated Product", 15.9, "Electronics")
update_product_array(products_array, updated_product)

# Update a product in the linked list by ID
#update_product_linkedlist(linked_list, updated_product)

# Printing products from array
for product in products_array:
  print(product)

# Printing products from linked list
#current = linked_list.head
#while current:
 #  print(current.product)
  # current = current.next

# Delete a product from the array by ID
delete_product_array(products_array, "2")

# Delete a product from the linked list by ID
#delete_product_linkedlist(linked_list, "2")

# Printing products from array after deletion
print("\nAfter deletion from array:")
for product in products_array:
   print(product)

# Printing products from linked list after deletion
#print("\nAfter deletion from linked list:")
#current = linked_list.head
#while current:
  # print(current.product)
  # current = current.next

# Search for a product in the array by ID
product = search_product_array(products_array, "1")
if product:
   print("Product found in array:", product)
else:
  print("Product not found in array.")

# Search for a product in the linked list by ID
#product = search_product_linkedlist(linked_list, "1")
#if product:
 #  print("Product found in linked list:", product)
#else:
  # print("Product not found in linked list.")
# Search for a product in the array by ID
#product = search_product_array(products_array, "1")
#if product:
   #print("Product found in array:", product)
#else:
 #  print("Product not found in array.")

# Search for a product in the linked list by ID
#product = search_product_linkedlist(linked_list, "1")
#if product:
 #  print("Product found in linked list:", product)
#else:
 #  print("Product not found in linked list.")
   
   # Sort products array by price
bubble_sort(products_array)

# Print sorted products array
print("Sorted products array:")
for product in products_array:
   print(product)
