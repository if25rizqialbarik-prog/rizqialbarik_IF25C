#create

import csv

def create_data(nama_barang,qty,nomor_resi):
    with open('data.csv','a',newline='')as file:
        writer = csv.writer(file)
        writer.writerow([nama_barang,qty,nomor_resi])
print("data berhasil ditambahkan")

# READ
def read_data():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# UPDATE
def update_data(nama_barang, qty, nomor_resi):
    rows = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == nama_barang:
                row = [nama_barang, qty, nomor_resi]
            rows.append(row)

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Data berhasil diupdate")

# DELETE
def delete_data(nama_barang):
    rows = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != nama_barang:
                rows.append(row)

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Data berhasil dihapus")


create_data("buku",10,210003302)
read_data()
update_data("buku", "10",210003302)
delete_data("penghapus")