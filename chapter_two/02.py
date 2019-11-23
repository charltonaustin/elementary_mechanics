from pylab import pi

# kg/m^3
STEEL_MASS_DENSITY = 7700


def sphere_mass(radius, mass_density):
    return (4 / 3) * pi * radius ** 3 * mass_density


def steel_sphere_mass(radius):
    return sphere_mass(radius, STEEL_MASS_DENSITY)


print("steel sphere mass for 1mm")
print(steel_sphere_mass(.001))

print("steel sphere mass for 1m")
print(steel_sphere_mass(1))

print("steel sphere mass for 10m")
print(steel_sphere_mass(10))
