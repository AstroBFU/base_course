from constants import g

def mech_energy(mass, height, speed):

    p_energy = mass * g * height

    k_energy = 0.5 * mass * speed**2 

    energy = p_energy + k_energy
    return energy

mass = int(input('Введите массу: '))
height = int(input('Введите высоту: '))
speed = int(input('Введите скорость: '))

print(mech_energy(mass, height, speed))