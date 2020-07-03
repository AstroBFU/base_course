import math as m
import numpy as np
import constant_module as cm

def FME (mass, spd, hgt):
    return mass*(spd**2/2 + cm.g*hgt)

print("Enter object's mass(kg), speed(m/s) and height(m)")
obj_mass = float(input())
obj_spd = float(input())
obj_hgt = float(input())

print("Full object's mechanic energy is", FME(obj_mass, obj_spd, obj_hgt), "joules")