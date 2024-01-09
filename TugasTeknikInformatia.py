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