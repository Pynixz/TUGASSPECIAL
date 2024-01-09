### Project

Program "FOODSTREET 2077" dimulai dengan mencetak judul dan garis pembatas, menyambut pengguna untuk memulai pengalaman memesan makanan. Selanjutnya, pengguna diminta untuk memasukkan nama pelanggan dan tanggal pembelian sebagai langkah pertama dalam interaksi dengan program.
Setelah memasukkan informasi awal, program menampilkan menu makanan lengkap dengan harga masing-masing. Pengguna kemudian diminta untuk memilih menu dengan memasukkan nomor menu yang diinginkan, diikuti oleh input jumlah makanan yang ingin dipesan. Harga makanan yang dipilih kemudian ditambahkan ke dalam daftar harga sebanyak jumlah pembelian yang dimasukkan oleh pengguna.
Program mengimplementasikan validasi menu untuk memastikan bahwa nomor menu yang dimasukkan oleh pengguna benar-benar ada dalam daftar. Jika nomor menu tidak valid, program memberikan pesan kesalahan dan meminta input menu yang valid.
Setelah pengguna selesai memasukkan pesanan pertama, program memberikan opsi untuk menambah atau mengurangi pesanan. Jika pengguna memilih untuk menambah pesanan, program meminta input tambahan menu dan jumlah pembelian. Sebaliknya, jika pengguna memilih untuk mengurangi pesanan, program meminta input jumlah item yang ingin dikurangkan, dan item tersebut dihapus dari daftar harga.
Setelah pengguna selesai menambah atau mengurangkan pesanan, program menampilkan total pesanan dan total pembayaran. Pengguna juga memiliki opsi untuk menyelesaikan transaksi tanpa melakukan tambahan atau pengurangan pesanan.
Akhirnya, program mencetak total pesanan dan total pembayaran, menyelesaikan interaksi dengan pengguna dan mengakhiri program "FOODSTREET 2077". Dengan demikian, alur program ini mencakup langkah-langkah pemilihan menu, pengelolaan pesanan, dan perhitungan total pembayaran dalam konteks simulasi pemesanan makanan.



# Codingannya
```py
print("         FOODSTREET 2077         ")
print("=================================")

nama = input("Nama Pelanggan : ")
tanggal = input("Tanggal Pembelian : ")
print("==============================")
print("     ==== MENU ====      ")
print("1. Sate                              Rp.10000")
print("2. Ayam Ireng                        Rp.15000")
print("3. Mie Ayam                          Rp.13500")
print("4. Bakso                             Rp.12500")
print("5. Steak Wagyu                       Rp.50000")
print("     ==== MENU ====      ")
h=[]
a=1

menu_pesanan = int (input("Masukan Menu Pesanan (Nomer Menu) : "))
if menu_pesanan == 1:
    harga = 10000
elif menu_pesanan == 2:
    harga = 15000
elif menu_pesanan == 3:
    harga = 13500
elif menu_pesanan == 4:
    harga = 12500
elif menu_pesanan == 5:
    harga = 50000
else:
    while True :
        print("==== Menu Tidak Tersedia Silahkan Memesan Pilihan Menu Lainnya ====")
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4 or menu_pesanan == 5:
            if menu_pesanan == 1:
                harga = 10000
            elif menu_pesanan == 2:
                harga = 15000
            elif menu_pesanan == 3:
                harga = 13500
            elif menu_pesanan == 4:
                harga = 12500
            elif menu_pesanan == 5:
                harga = 50000
                break

jumlah_pembelian = int (input("Masukan Jumlah Pembelian : "))
for i in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input("Apakah ada yang ingin ditambah/dikurangi ? tambah/kurang/tidak : ")
    if jawab == 'tambah':
        tambah = int(input("Masukan Menu Pesanan (Nomer Menu): "))
        if tambah == 1:
            harga = 10000
        elif tambah == 2:
            harga = 15000
        elif tambah == 3:
            harga = 13500
        elif tambah == 4:
            harga = 12500 
        elif tambah == 5:
            harga = 50000
        jumlah_tambahan = int(input("Masukan Jumlah Pembelian : "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c = jumlah_tambahan + jumlah_pembelian
        print("Total Pesanan: ",c)
        bayar =  sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    elif jawab == 'kurang' :
        kurang = int(input("Berapa Jumlah yang Dikurungkan ? : "))
        for i in range(kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h[kurang]
                if kurang < 0:
                    break
        c = jumlah_pembelian - kurang
        print ("Total Pememsanan: ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break
    else:
        bayar = sum(h)
        c = jumlah_pembelian
        print("Total Pemesanan : ",c)
        print("Total Pembayaran : Rp.".format(bayar))
        break
```

### LINK YOUTUBE
``` https://youtu.be/ddbehRbDE7w ```
