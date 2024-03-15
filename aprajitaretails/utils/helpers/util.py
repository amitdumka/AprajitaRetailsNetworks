#Utils 
# -*- encoding: utf-8 -*-
#It Generate Random String and Int
#Date 15/02/2024
#Author: Amit Kumar (AKS Labs(India))


import os, random, string

def h_random(aLen=32):
    letters = string.ascii_letters
    digits  = string.digits
    chars   = '_<>,.+'
    return ''.join(random.choices( letters + digits + chars, k=aLen))

def h_random_ascii(aLen=32):
    letters = string.ascii_letters
    digits  = string.digits
    return ''.join(random.choices( letters + digits, k=aLen))
