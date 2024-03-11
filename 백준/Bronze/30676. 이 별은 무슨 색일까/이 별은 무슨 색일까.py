wavelength = int(input())

if wavelength < 425:
    print('Violet')
elif wavelength < 450:
    print('Indigo')
elif wavelength < 495:
    print('Blue')
elif wavelength < 570:
    print('Green')
elif wavelength < 590:
    print('Yellow')
elif wavelength < 620:
    print('Orange')
else:
    print('Red')