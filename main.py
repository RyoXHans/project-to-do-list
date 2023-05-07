# Project To Do List menggunakan Python dan MYSQL untuk latihan
# Date: 5/7/2023
# Project by: Hans
import mysql.connector
import datetime

connx = mysql.connector.connect(user="root",password="kali",host="127.0.0.1",database="todolist")

cursor = connx.cursor()

banner = """
+========================+
|	TO DO LIST	 |
+========================+
1.) Tampilkan daftar tugas
2.) Tambahkan tugas baru
3.) Edit tugas
4.) Hapus tugas
5.) Keluar
"""

def tampilkanTugas():
	query = "SELECT * FROM todolist"
	cursor.execute(query)
	results = cursor.fetchall()
	if cursor.rowcount <= 0:
		print("Anda belum membuat Tugas!")
		main()
	else:
		for data in results:
			print(list(data))
	input("\nTekan [ENTER] untuk kembali ke menu!")
	main()

def tambahkanTugasBaru():
	nama = input("Masukan nama tugas: ")
	keterangan = input("Masukan keterangan [Terpenuhi/Proses/Belum Terpenuhi]: ")
	date = datetime.datetime.now()
	query = "INSERT INTO todolist(nama, tanggal, keterangan) VALUES(%s,%s,%s)"
	value = (nama, date, keterangan)
	cursor.execute(query, value)
	connx.commit()
	print("{} Tugas telah ditambahkan...".format(cursor.rowcount))
	input("\nTekan [ENTER] untuk kembali ke menu!")
	main()

def editTugas():
	cursor.execute("SELECT * FROM todolist")
	results = cursor.fetchall()
	for data in results:
		print(list(data))
	idTugas = input("Masukan id Tugas: ")
	namaBaru = input("Masukan nama tugas (Update): ")
	keterangan = input("Update keterangan [Terpenuhi/Proses/Belum Terpenuhi]: ")
	query = "UPDATE todolist SET nama=%s, keterangan=%s WHERE id=%s"
	value = (namaBaru, keterangan, idTugas)
	cursor.execute(query, value)
	connx.commit()
	print("{} data telah diubah...".format(cursor.rowcount))
	input("\nTekan [ENTER] untuk kembali ke menu!")
	main()

def hapusTugas():
	cursor.execute("SELECT * FROM todolist")
	results = cursor.fetchall()
	for data in results:
		print(list(data))
	idTugas = int(input("Masukan id Tugas: "))
	confirmDeleteTugas = input("Apakah anda ingin menhapusnya [Y/N]: ")
	if confirmDeleteTugas == "N" or confirmDeleteTugas == "n":
		input("\nTekan [ENTER] untuk kembali ke menu!")
		main()
	elif confirmDeleteTugas == "Y" or confirmDeleteTugas == "y":
		query = "DELETE FROM todolist WHERE id={}".format(idTugas)
		cursor.execute(query)
		connx.commit()
		print("{} data telah dihapus...".format(cursor.rowcount))
		input("\nTekan [ENTER] untuk kembali ke menu!")
		main()

def main():
	print(banner)
	pilihan = int(input("Pilihan: "))
	if pilihan == 1:
		tampilkanTugas()
	elif pilihan == 2:
		tambahkanTugasBaru()
	elif pilihan == 3:
		editTugas()
	elif pilihan == 4:
		hapusTugas()
	elif pilihan == 5:
		print("Terimakasih telah mencoba project ini...")


if __name__ == '__main__':
	main()
