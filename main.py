#print("Это основной файл",__name__)
import pack_2
import importlib

print (dir(pack_2))
pack_2.file_21.x=3
print(pack_2.file_21.x)
pack_2 = importlib.reload(pack_2)

print(pack_2.file_21.x)