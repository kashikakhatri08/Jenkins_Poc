# This file creates a file in cwd workspace location
print('==================== start ========================')
print('===================================================')
file = open('example.txt', 'w+')
print('==================== writing file =================')
file.write('I am a file created by freestyle job')
file.close()
print('===================================================')
print('==================== end ==========================')
