from queue import Queue

#Mohammed Endji Aji Putra
#2IA26
#50422916

# Membuat objek Queue
q = Queue()

# Menambahkan elemen ke dalam Queue
q.put(1)
q.put(2)
q.put(3)

# Mengambil elemen dari Queue (dengan urutan pertama yang dimasukkan pertama keluar, FIFO)
element1 = q.get()
element2 = q.get()
element3 = q.get()

print("Elemen dari Queue:")
print(element1)
print(element2)
print(element3)