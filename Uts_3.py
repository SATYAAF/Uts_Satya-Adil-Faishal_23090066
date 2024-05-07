def hitung_total(jumlah_barang, harga_barang1, harga_barang2):
    return (jumlah_barang * harga_barang1) + (jumlah_barang * harga_barang2)

def main():
    jumlah_barang = int(input("Jumlah barang: "))
    harga_barang1 = float(input("Harga barang 1: "))
    harga_barang2 = float(input("Harga barang 2: "))

    total = hitung_total(jumlah_barang, harga_barang1, harga_barang2)
    print("Total belanjaan:", total)
if __name__ == "__main__":
    main()
