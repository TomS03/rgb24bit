blueConst = 65536
greenConst = 256

blue = int(input('Enter B value: '))
green = int(input('Enter G value: '))
red = int(input('Enter R value: '))

rgb = (blue * blueConst) + (green * greenConst) + red

print(rgb)
