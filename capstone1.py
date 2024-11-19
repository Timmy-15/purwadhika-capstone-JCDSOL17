def print_daftar_barang(db_barang):
    print("|Index\t | Nama  \t | Harga\t | Stok\t | Cart\t |")
    for i in range(0, len(db_barang)):
        print(f"|{i}\t | {db_barang[i]['nama']}  \t | {db_barang[i]['harga']} \t | {db_barang[i]['stok']}\t | {db_barang[i]['cart']}\t |")

def read_validated_input(dtype, message):
    temp_input = None
    while temp_input is None:
        try:
            temp_input = dtype( input(f"Masukkan {message}: "))
        except Exception as e:
            print("Input Belum Benar, Input Ulang!")
    else:
        return temp_input

db_barang = [
    {
        "nama":"Rokok",
        "harga":20000,
        "stok":40,
        "cart":None,
    },
    {
        "nama":"Sabun",
        "harga":10000,
        "stok":60,
        "cart":None,
    },
    {
        "nama":"Kopi",
        "harga":5000,
        "stok":30,
        "cart":None,
    },
    {
        "nama":"Permen",
        "harga":1000,
        "stok":70,
        "cart":None,
    }
]

menu=0
while menu!=6:
    print("Selamat datang di Toko Jaya")
    print("List Menu: ")
    print("1. Menampilkan Daftar Barang")
    print("2. Menambah Barang")
    print("3. Menghapus Barang")
    print("4. Update Barang")
    print("5. Membeli Barang")
    print("6. Exit Program")
    try:
        menu = int(input("Masukkan input Menu, 1-6: "))
        if menu == 1:
            print_daftar_barang(db_barang)
        elif menu == 2:
            print_daftar_barang(db_barang)
            nama_barang_lama = [barang['nama'] for barang in db_barang]
            nama_barang_baru = read_validated_input(str, "Nama Barang Baru")
            
            if nama_barang_baru in nama_barang_lama:
                print("Barang sudah ada! ")
            else:
                harga_barang_baru = read_validated_input(int,"Masukkan Harga Barang Baru: ")
                stok_barang_baru = read_validated_input(int,"Masukkan Stok Barang Baru: ")
                db_barang.append({
                    "nama":nama_barang_baru,
                    "harga":harga_barang_baru,
                    "stok":stok_barang_baru,
                    "cart":None,
                })
        elif menu == 3:
            print_daftar_barang(db_barang)
            for i in range(0, len(db_barang)):
                print(f"Barang tersedia: {db_barang[i]['nama']}, Indeks: {i} ")
            index_barang_to_be_deleted = read_validated_input(int,"Masukkan Index Barang Ingin Dihapus: ")
            del db_barang[index_barang_to_be_deleted]
        elif menu == 4:
            print_daftar_barang(db_barang)
            for i in range(0, len(db_barang)):
                print(f"Barang tersedia: {db_barang[i]['nama']}, Indeks: {i} ")
            index_barang_to_be_updated = read_validated_input(int,"Masukkan Index Barang Ingin Diperbarui: ")
            print(f"Barang yang akan diperbarui: {db_barang[index_barang_to_be_updated]['nama']}")
            print(f"Harga Barang sekarang: {db_barang[index_barang_to_be_updated]['harga']}")
            harga_barang_baru = read_validated_input(int,"Masukkan Harga Baru: ")
            if harga_barang_baru == 0 :
                pass
            else:
                db_barang[index_barang_to_be_updated]['harga'] = harga_barang_baru

            print(f"Stok Barang sekarang: {db_barang[index_barang_to_be_updated]['stok']}")
            stok_barang_baru = read_validated_input(int,"Masukkan Stock Barang Baru: ")
            if stok_barang_baru == 0 :
                pass
            else:
                db_barang[index_barang_to_be_updated]['stok'] = stok_barang_baru
        elif menu == 5:
            print_daftar_barang(db_barang)
            for i in range(0, len(db_barang)):
                while db_barang[i]['cart'] is None:
                    print(f"Jumlah {db_barang[i]['nama']} yang tersedia: {db_barang[i]['stok']}")
                    try:
                        temp_jumlah_barang = read_validated_input(int,(f"Masukkan Jumlah {db_barang[i]['nama']} : "))
                        if temp_jumlah_barang<= db_barang[i]['stok']:
                            db_barang[i]['cart'] = temp_jumlah_barang
                        else:  
                            print("Kelebihan!")
                    except Exception as e:
                        print(e)
                        print("Input tidak benar!")
               
            grand_total = 0
            for i in range(0, len(db_barang)):
                db_barang[i]['total_belanja'] = db_barang[i]['cart'] * db_barang[i]['harga']
                grand_total = grand_total + db_barang[i]['total_belanja']

            print("\nDetail Belanja")
            for i in range(0, len(db_barang)):
                print(f"{db_barang[i]['nama']} : {db_barang[i]['cart']} x {db_barang[i]['harga']} = {db_barang[i]['total_belanja']}")
            if grand_total == 0: 
                pass
            else:
                print("\nTotal :", grand_total)

                jumlah_pembayaran = read_validated_input(int,"Masukkan jumlah uang : ")
                if jumlah_pembayaran>grand_total:
                    print("Terimakasih")
                    print("Kembalian anda ",jumlah_pembayaran-grand_total)

                    for i in range(0, len(db_barang)):
                        db_barang[i]['stok'] = db_barang[i]['stok'] - db_barang[i]['cart']


                elif jumlah_pembayaran==grand_total:
                    print("Terimakasih")
                    for i in range(0, len(db_barang)):
                        db_barang[i]['stok'] = db_barang[i]['stok'] - db_barang[i]['cart']
                else:
                    print("Pembelian anda dibatalkan")
                    print("Uang anda Kurang : ",abs(grand_total-jumlah_pembayaran))

            for i in range(0, len(db_barang)):
                db_barang[i]['cart'] = None

        else:
            print("Input yang anda masukan salah")
            pass

    except Exception as e:
        print(e)
        print("Input tidak benar!")
