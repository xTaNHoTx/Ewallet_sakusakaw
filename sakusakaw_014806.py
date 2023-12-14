#REGRISTRASI 
import random
print('+=+=+=++===================++=+=+=+')
print('|   Regristrasi terlebih dahulu   |')
print('+=+=+=++===================++=+=+=+')
akun=(input("masukan Username anda : "))
passw=(input("masukan Password anda : "))
saldoal=0


#defnisi
print('+=+=+=++===================++=+=+=+')
print('|         Login dulu Rek          |')
print('+=+=+=++===================++=+=+=+')

#looping
for i in range(3):
    print()
    username=str(input("masukan username :"))
    password=str(input("masukan Password :"))
    if username==akun and password==passw :
       print()
       print("username dan password benar")
       print()
       break 
    elif username==akun or password==passw :
        print()
        print("salah satu dari username dan password salah")
        print()
    else :
        print("Password salah")
        if i == 2 :
            print('+=+=+=++===================++=+=+=+')
            print('untuk sementara akun anda di blokir')        
            print('+=+=+=++===================++=+=+=+')
            quit()

#menu home
pilihan = 'y'
while (pilihan == 'y'):

    print('+=+=+=++================================++=+=+=+')
    print('|         SELAMAT DATANG DI SAKUSAKAW          |')
    print('+=+=+=++================================++=+=+=+')
    print('|_____________SILAHKAN PILIH MENU______________|')
    print('+=+=+=++================================++=+=+=+')
    print('|1. |Cek Informasi Saldo Top Up                |')
    print('|2. |Top Up Saldo                              |')
    print('|3. |Isi Pulsa                                 |')
    print('|4. |Transfer Rekening                         |')
    print('|5. |Riwayat Transaksi                         |')
    print('|6. |Pesan Makanan & Minuman                   |')
    print('|7. |Pesan Tiket Pesawat                       |')
    print('|8 .|Pesan Tiket Kapal                         |')
    print('|9. |Keluar                                    |')
    print('+=+=+=++================================++=+=+=+')
    print()

    menu = input('silahkan pilih menu : ')
    print('+=+=+=++================================++=+=+=+')

#pilihan opsi menu

# cek saldo top up
    if menu == '1':
        print(f"informasi saldo top up anda : Rp. {saldoal}")


# top up saldo 
    elif menu == '2':
        print('silahkan masukan tanggal, bulan, dan tahun transaksi : ')
        j=int(input("masukan tanggal : "))
        if j > 31 :
            print ('input tanggal salah')

        k = int(input("masukan bulan : "))
        if (k==1):
            k='Januari'
        elif (k==2):
            k='Februari'
        elif (k==3):
            k='Maret'
        elif (k==4):
            k='April'
        elif (k==5):
            k='Mei'
        elif (k==6):
            k='Juni'
        elif (k==7):
            k='Juli'
        elif (k==8):
            k='Agustus'
        elif (k==9):
            k='September'
        elif (k==10):
            k='Oktober'
        elif (k==11):
            k='November'
        elif (k==12):
            k='Desember'
        else:
            print('input bulan salah')

        l = int(input("masukan tahun : "))
        w = (j , k , l )
        
        topup = 'n'
        while (topup == 'n'):
        
            print('+=+=+=++================================++=+=+=+')
            print('------PILIH ISI SALDO TOP UP YANG ANDA MAU------')
            print('+=+=+=++================================++=+=+=+')
            print('|No |Top up       | Harga                      |')
            print('|1. |Rp. 50000    | Rp. 55000                  |')
            print('|2. |Rp. 75000    | Rp. 85000                  |')
            print('|3. |Rp. 100000   | Rp. 115000                 |')
            print('|4. |Rp. 150000   | Rp. 165000                 |')
            print('|5. |Rp. 175000   | Rp. 180000                 |')
            print('|6. |Rp. 200000   | Rp  230000                 |')
            print('|7. |Rp. 500000   | Rp  520000                 |')
            print('|8. Home                                       |')
            print()

            topup = input('silahkan pilih top up saldo: ') 
            print('+=+=+=++================================++=+=+=+')

        if topup == '1' :
            print("anda akan melakukan top up saldo senilai Rp. 50000")
            topup = input('apakah anda ingin melanjutkan top up (y/n) : ')
            if topup == 'y' :
                top1=50000
                hargatop1=55000
                pembayarantop1=int(input('masukan uang pembayaran anda sesuai harga : '))
                if hargatop1 == pembayarantop1 :
                  saldoal = saldoal + top1
                  riw=top1
                  hariw=hargatop1
                  print('transaksi saldo top up berhasil')
                  print('anda melakukan transaksi top up saldo pada : ', w , 'sebesar : Rp.', top1 , 'harga : Rp.', hargatop1)
                  print(f"jumlah top up saku anda : Rp. {saldoal}")
                  pilihan = input('kembali ke menu awal (y/n) : ')
                elif top1 != pembayarantop1 :
                    print("maaf pembayaran top up anda tidak sesuai dengan harga pembayaran")
                    pilihan = input('kembali ke menu awal (y/n) : ')
                                   
        elif topup == '2' :
            print("anda akan melakukan top up saldo senilai Rp. 75000")
            topup = input('apakah anda ingin melanjutkan top up (y/n) : ')
            if topup == 'y' :
                top2 = 75000
                hargatop2 = 85000
                pembayarantop2=int(input('masukan uang pembayaran anda sesuai harga : '))
                if hargatop2 == pembayarantop2 :
                  saldoal = saldoal + top2
                  riw=top2
                  hariw=hargatop2
                  print('transaksi saldo top up berhasil')
                  print('anda melakukan transaksi top up saldo pada : ', w , 'sebesar : Rp.', top2 , 'harga : Rp.', hargatop2)
                  print(f"jumlah top up saku anda : Rp. {saldoal}")
                  pilihan = input('kembali ke menu awal (y/n) : ')
                elif top2 != pembayarantop2 :
                    print("maaf pembayaran top up anda tidak sesuai dengan harga pembayaran")
                    pilihan = input('kembali ke menu awal (y/n) : ')
                                   
        elif topup == '3' :
            print("anda akan melakukan top up saldo senilai Rp. 100000")
            topup = input('apakah anda ingin melanjutkan top up (y/n) : ')
            if topup == 'y' :
                top3 = 100000
                hargatop3 = 115000
                pembayarantop3=int(input('masukan uang pembayaran anda sesuai harga : '))
                if hargatop3 == pembayarantop3 :
                  saldoal = saldoal + top3
                  riw=top3
                  hariw=hargatop3
                  print('transaksi saldo top up berhasil')
                  print('anda melakukan transaksi top up saldo pada : ', w , 'sebesar : Rp.', top3 , 'harga : Rp.', hargatop3)
                  print(f"jumlah top up saku anda : Rp. {saldoal}")
                  pilihan = input('kembali ke menu awal (y/n) : ')
                elif top3 != pembayarantop3 :
                    print("maaf pembayaran top up anda tidak sesuai dengan harga pembayaran")
                    pilihan = input('kembali ke menu awal (y/n) : ')
                                   
        elif topup == '4' :
            print("anda akan melakukan top up saldo senilai Rp. 150000")
            topup = input('apakah anda ingin melanjutkan top up (y/n) : ')
            if topup == 'y' :
                top4 = 150000
                hargatop4 = 165000
                pembayarantop4=int(input('masukan uang pembayaran anda sesuai harga : '))
                if hargatop4 == pembayarantop4 :
                  saldoal = saldoal + top4
                  riw=top4
                  hariw=hargatop4
                  print('transaksi saldo top up berhasil')
                  print('anda melakukan transaksi top up saldo pada : ', w , 'sebesar : Rp.', top4 , 'harga : Rp.', hargatop4)
                  print(f"jumlah top up saku anda : Rp. {saldoal}")
                  pilihan = input('kembali ke menu awal (y/n) : ')
                elif top4 != pembayarantop4 :
                    print("maaf pembayaran top up anda tidak sesuai dengan harga pembayaran")
                    pilihan = input('kembali ke menu awal (y/n) : ')

        elif topup == '5' :
            print("anda akan melakukan top up saldo senilai Rp. 175000")
            topup = input('apakah anda ingin melanjutkan top up (y/n) : ')
            if topup == 'y' :
                top5 = 175000
                hargatop5 = 180000
                pembayarantop5=int(input('masukan uang pembayaran anda sesuai harga : '))
                if hargatop5 == pembayarantop5 :
                  saldoal = saldoal + top5
                  riw=top5
                  hariw=hargatop5
                  print('transaksi saldo top up berhasil')
                  print('anda melakukan transaksi top up saldo pada : ', w , 'sebesar : Rp.', top5 , 'harga : Rp.', hargatop5)
                  print(f"jumlah top up saku anda : Rp. {saldoal}")
                  pilihan = input('kembali ke menu awal (y/n) : ')
                elif top5 != pembayarantop5 :
                    print("maaf pembayaran top up anda tidak sesuai dengan harga pembayaran")
                    pilihan = input('kembali ke menu awal (y/n) : ')

        elif topup == '6' :
            print("anda akan melakukan top up saldo senilai Rp. 200000")
            topup = input('apakah anda ingin melanjutkan top up ini (y/n) : ')
            if topup == 'y' :
                top6 = 200000
                hargatop6 = 230000
                pembayarantop6=int(input('masukan uang pembayaran anda sesuai harga : '))
                if hargatop6 == pembayarantop6 :
                  saldoal = saldoal + top6
                  riw=top6
                  hariw=hargatop6
                  print('transaksi saldo top up berhasil')
                  print('anda melakukan transaksi top up saldo pada : ', w , 'sebesar : Rp.', top6 , 'harga : Rp.', hargatop6)
                  print(f"jumlah top up saku anda : Rp. {saldoal}")
                  pilihan = input('kembali ke menu awal (y/n) : ')
                elif top6 != pembayarantop6 :
                    print("maaf pembayaran top up anda tidak sesuai dengan harga pembayaran")
                    pilihan = input('kembali ke menu awal (y/n) : ')

        elif topup == '7' :
            print("anda akan melakukan top up saldo senilai Rp. 500000")
            topup = input('apakah anda ingin melanjutkan top up ini (y/n) : ')
            if topup == 'y' :
                top7 = 500000
                hargatop7 = 520000
                pembayarantop7=int(input('masukan uang pembayaran anda sesuai harga : '))
                if hargatop7 == pembayarantop7 :
                  saldoal = saldoal + top7
                  riw=top7
                  hariw=hargatop7
                  print('transaksi saldo top up berhasil')
                  print('anda melakukan transaksi top up saldo pada : ', w , 'sebesar : Rp.', top7 , 'harga : Rp.', hargatop7)
                  print(f"jumlah top up saku anda : Rp. {saldoal}")
                  pilihan = input('kembali ke menu awal (y/n) : ')
                elif top7 != pembayarantop7 :
                    print("maaf pembayaran top up anda tidak sesuai dengan harga pembayaran")
                    pilihan = input('kembali ke menu awal (y/n) : ')

        elif topup == '8' :

            pilihan = input("anda ingin kembali ke menu awal (y/n): ")

        else : 
            print("input anda salah")
    
    elif menu == '3' :

        print('silahkan masukan tanggal, bulan, dan tahun transaksi : ')
        a=int(input("masukan tanggal : "))
        if a > 31 :
            print ('input tanggal salah')

        b = int(input("masukan bulan : "))
        if (b==1):
            b='Januari'
        elif (b==2):
            b='Februari'
        elif (b==3):
            b='Maret'
        elif (b==4):
            b='April'
        elif (b==5):
            b='Mei'
        elif (b==6):
            b='Juni'
        elif (b==7):
            b='Juli'
        elif (b==8):
            b='Agustus'
        elif (b==9):
            b='September'
        elif (b==10):
            b='Oktober'
        elif (b==11):
            b='November'
        elif (b==12):
            b='Desember'
        else:
            print('input bulan salah')

        c = int(input("masukan tahun : "))
        d = (a , b , c )
    
        isipulsa = 'n'
        while (isipulsa == 'n'):

            print('+=+=+=++================================++=+=+=+')
            print('------PILIH ISI ULANG PULSA YANG ANDA MAU-------')
            print('+=+=+=++================================++=+=+=+')
            print('|No |Isi pulsa    | Harga                      |')
            print('|1. |Rp. 5000     | Rp. 6000                   |')
            print('|2. |Rp. 10000    | Rp. 11000                  |')
            print('|3. |Rp. 15000    | Rp. 16000                  |')
            print('|4. |Rp. 20000    | Rp. 21000                  |')
            print('|5. |Rp. 25000    | Rp. 26000                  |')
            print('|6. |Rp. 50000    | Rp  51000                  |')
            print('|7. |Rp. 55000    | Rp  56000                  |')
            print('|8. |Rp. 70000    | Rp  72000                  |')
            print('|9. |Rp. 75000    | Rp  77000                  |')
            print('|10.|Rp. 100000   | Rp  103000                 |')
            print('|11.|Rp. 500000   | Rp  501000                 |')
            print('|12. Home                                      |')
            print()

            isipulsa=input('Silahkan pilih isi ulang pulsa yang anda mau : ')
            print('+=+=+=++================================++=+=+=+')
        
        if isipulsa == '1' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 5000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa1 = 5000
                hargapulsa1 = 6000
                if saldoal >= hargapulsa1 :
                    saldoal = saldoal - hargapulsa1
                    pulsariw=pulsa1
                    hargapuriw=hargapulsa1
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa1 , 'harga : Rp.', hargapulsa1 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa1  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '2' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 10000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa2 = 10000
                hargapulsa2 = 11000
                if saldoal >= hargapulsa2 :
                    saldoal = saldoal - hargapulsa2
                    pulsariw=pulsa2
                    hargapuriw=hargapulsa2
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa2 , 'harga : Rp.', hargapulsa2 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa2  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '3' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 15000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa3 = 15000
                hargapulsa3 = 16000
                if saldoal >= hargapulsa3 :
                    saldoal = saldoal - hargapulsa3
                    pulsariw=pulsa3
                    hargapuriw=hargapulsa3
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa3 , 'harga : Rp.', hargapulsa3 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa3  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '4' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 20000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa4 = 20000
                hargapulsa4 = 21000
                if saldoal >= hargapulsa4 :
                    saldoal = saldoal - hargapulsa4
                    pulsariw=pulsa4
                    hargapuriw=hargapulsa4
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa4 , 'harga : Rp.', hargapulsa4 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa4  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '5' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 25000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa5 = 25000
                hargapulsa5 = 26000
                if saldoal >= hargapulsa5 :
                    saldoal = saldoal - hargapulsa5
                    pulsariw=pulsa5
                    hargapuriw=hargapulsa5
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa5 , 'harga : Rp.', hargapulsa5 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa5  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '6' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 50000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa6 = 50000
                hargapulsa6 = 51000
                if saldoal >= hargapulsa6 :
                    saldoal = saldoal - hargapulsa6
                    pulsariw=pulsa6
                    hargapuriw=hargapulsa6
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa6 , 'harga : Rp.', hargapulsa6 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa6  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')
        elif isipulsa == '7' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 55000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa7 = 55000
                hargapulsa7 = 56000
                if saldoal >= hargapulsa7 :
                    saldoal = saldoal - hargapulsa7
                    pulsariw=pulsa7
                    hargapuriw=hargapulsa7
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa7 , 'harga : Rp.', hargapulsa7 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa7  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '8' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 70000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa8 = 70000
                hargapulsa8 = 11000
                if saldoal >= hargapulsa8 :
                    saldoal = saldoal - hargapulsa8
                    pulsariw=pulsa8
                    hargapuriw=hargapulsa8
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa8 , 'harga : Rp.', hargapulsa8 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa8  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')
        elif isipulsa == '9' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 75000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa9 = 75000
                hargapulsa9 = 77000
                if saldoal >= hargapulsa9 :
                    saldoal = saldoal - hargapulsa9
                    pulsariw=pulsa9
                    hargapuriw=hargapulsa9
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa9 , 'harga : Rp.', hargapulsa9 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa9  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')
        elif isipulsa == '10' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 100000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa10 = 100000
                hargapulsa10 = 103000
                if saldoal >= hargapulsa10 :
                    saldoal = saldoal - hargapulsa10
                    pulsariw=pulsa10
                    hargapuriw=hargapulsa10
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa10 , 'harga : Rp.', hargapulsa10 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa10  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '11' :
            nomorpulsa = input('Silahkan masukan Nomor Hp anda : ')
            print("anda akan melakukan isi ulang pulsa senilai Rp. 500000")
            isipulsa = input('apakah anda ingin melanjutkan Isi pulsa (y/n)? : ')
            if isipulsa == 'y' :
                pulsa11 = 500000
                hargapulsa11 = 501000
                if saldoal >= hargapulsa11 :
                    saldoal = saldoal - hargapulsa11
                    pulsariw=pulsa11
                    hargapuriw=hargapulsa11
                    nomorriw=nomorpulsa
                    print('isi ulang pulsa berhasil')
                    print('anda melakukan isi ulang pulsa pada : ', d , 'sebesar : Rp.', pulsa11 , 'harga : Rp.', hargapulsa11 , 'di nomor : ', nomorpulsa)
                    print(f"jumlah top up saku anda : Rp. {saldoal}")
                    pilihan = input('kembali ke menu (y/n) : ')
                elif saldoal < hargapulsa11  :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            else :
                print('input anda salah')

        elif isipulsa == '12' :
                pilihan = input("anda ingin kembali ke menu awal (y/n): ")

        else :
            print('input anda salah')

    elif menu == '4':
    
        print('silahkan masukan tanggal, bulan, dan tahun transaksi : ')
        m=int(input("masukan tanggal : "))
        if m > 31 :
            print ('input tanggal salah')

        n = int(input("masukan bulan : "))
        if (n==1):
            n='Januari'
        elif (n==2):
            n='Februari'
        elif (n==3):
            n='Maret'
        elif (n==4):
            n='April'
        elif (n==5):
            n='Mei'
        elif (n==6):
            n='Juni'
        elif (n==7):
            n='Juli'
        elif (n==8):
            n='Agustus'
        elif (n==9):
            n='September'
        elif (n==10):
            n='Oktober'
        elif (n==11):
            n='November'
        elif (n==12):
            n='Desember'
        else:
            print('input bulan salah')

        o = int(input("masukan tahun : "))
        p = (m , n , o )
        x =int(input("masukan nomor rekening tujuan : "))
        q =int(input("masukan jumlah transfer : "))
        if q>saldoal :
            print("saldo anda tidak mencukupi, silakan lakukan top up terlebih dahulu")
        elif q<(saldoal):
            saldoal=saldoal-q
            raw=q
            print()
            print("Transaksi anda berhasil")
            print('Anda melakukan transaksi transfer pada : ', p ,' ke rekening : ', x , 'sebesar Rp. : ',q)
            print(f"sisa saldo anda : Rp. ", saldoal)
    
    

    elif menu == '5':
        print('+=+=+=++================================++=+=+=+')
        print('------------PILIH RIWAYAT TRANSAKSI-------------')
        print('+=+=+=++================================++=+=+=+')
        print('|No |Menu Riwayat                              |')
        print('|1  |Untuk Harian                              |')
        print('|2  |Untuk Mingguan                            |')
        print('|3  |Untuk Bulanan                             |')
        print('+=+=+=++================================++=+=+=+')
        option = input("pilih menu : ")

        print('silahkan masukan tanggal, bulan, dan tahun transaksi : ')
        hari=int(input("masukan tanggal : "))
        if hari > 31 :
            print ('input tanggal salah')

        bulan = int(input("masukan bulan : "))
        if (bulan==1):
            bulan='Januari'
        elif (bulan==2):
            bulan='Februari'
        elif (bulan==3):
            bulan='Maret'
        elif (bulan==4):
            bulan='April'
        elif (bulan==5):
            bulan='Mei'
        elif (bulan==6):
            bulan='Juni'
        elif (bulan==7):
            bulan='Juli'
        elif (bulan==8):
            bulan='Agustus'
        elif (bulan==9):
            bulan='September'
        elif (bulan==10):
            bulan='Oktober'
        elif (bulan==11):
            bulan='November'
        elif (bulan==12):
            bulan='Desember'
        else:
            print('input bulan salah')

        tahun = int(input("masukan tahun : "))

        riwayat = (hari , bulan , tahun )

        if option == '1':
            print('1, top up')    
            print('2, transfer')
            print('3, isi pulsa')
            bay = input('pilih transaksi : ')
               
            if bay == '1':
                if riwayat == w :
                    print('hari ini anda melakukan top up saku pada tanggal : ', w ,' sebesar : Rp. ', riw , 'harga : Rp. ', hariw)
                elif riwayat != w :
                    print('anda tidak melakukan top up apapun')
            elif bay == '2':
                if riwayat == p :
                    print('hari ini anda melakukan transfer pada tanggal : ', p , ' sebesar : Rp. ', raw) 
                elif riwayat != p : 
                    print('anda tidak melakukan transaksi apapun')
            elif bay == '3':
                if riwayat == d :
                    print('hari ini anda melakukan isi ulang pulsa saku pada tanggal : ', d ,' sebesar : Rp. ', pulsariw , 'harga : Rp. ', hargapuriw , 'di nomor : Rp. ' , nomorriw)
                elif riwayat != d :
                    print('anda tidak melakukan top up apapun')

        elif option == '2':
            print('1, top up')    
            print('2, transfer')
            print('3, isi pulsa')
            bay = input('pilih transaksi : ')
            
            if bay == '1':
                if riwayat == w :
                    print('minggu ini anda melakukan top up saku pada tanggal : ', w ,' sebesar : Rp. ', riw , 'harga : Rp. ', hariw)
                elif riwayat != w :
                    print('anda tidak melakukan top up apapun')
            elif bay == '2':
                if riwayat == p :
                    print('minggu ini anda melakukan transfer pada tanggal : ', p , ' sebesar : Rp. ', raw) 
                elif riwayat != p : 
                    print('anda tidak melakukan transaksi apapun')
            elif bay == '3':
                if riwayat == d :
                    print('minggu ini anda melakukan isi ulang pulsa saku pada tanggal : ', d ,' sebesar : Rp. ', pulsariw , 'harga : Rp. ', hargapuriw , 'di nomor : Rp. ' , nomorriw)
                elif riwayat != d :
                    print('anda tidak melakukan top up apapun')

        elif option == '3':
            print('1, top up')    
            print('2, transfer')
            print('3, isi pulsa')
            bay = input('pilih transaksi : ')
        
            if bay == '1':
                if riwayat == w :
                    print('bulan ini anda melakukan top up saku pada tanggal : ', w ,' sebesar : Rp. ', riw , 'harga : Rp. ', hariw)
                elif riwayat != w :
                    print('anda tidak melakukan top up apapun')
            elif bay == '2':
                if riwayat == p :
                    print('bulan ini anda melakukan transfer pada tanggal : ', p , ' sebesar : Rp. ', raw) 
                elif riwayat != p : 
                    print('anda tidak melakukan transaksi apapun')
            elif bay == '3':
                if riwayat == d :
                    print('bulan ini anda melakukan isi ulang pulsa saku pada tanggal : ', d ,' sebesar : Rp. ', pulsariw , 'harga : Rp. ', hargapuriw , 'di nomor : Rp. ' , nomorriw)
                elif riwayat != d :
                    print('anda tidak melakukan top up apapun')
        else:
            print("inputan salah")
            
    elif menu == '6' :
        
        makmin='n'
        while (makmin == 'n'):

            print('+=+=+=++================================++=+=+=+')
            print('|           MENU MAKANAN DAN MINUMAN           |')
            print('+=+=+=++================================++=+=+=+')
            print('|_______PILIH MERCHANT YANG ANDA INGINKAN______|')
            print('+=+=+=++================================++=+=+=+')
            print('|1. |Rissoles 69                               |')
            print('|2. |Sabung pried ciken                        |')
            print('|3. |Burhotbab                                 |')
            print('|4. |SugMadik fresh                            |')
            print('|5. |Moonbuck                                  |')
            print('|6. |Ice Wallow come                           |')
            print('|7. |Menu awal                                 |')
            print('+=+=+=++================================++=+=+=+')
            print()

            makmin=input('silahkan pilih merchant yang anda pesan : ')
            print('+=+=+=++================================++=+=+=+')

        if makmin == '1':
            print('+=+=+=++================================++=+=+=+')
            print('|_______________Menu Rissoles 69_______________|')
            print('+=+=+=++================================++=+=+=+')
            print('|No |Nama produk           |Harga              |')
            print('|1. |Rissol ayam suir pedas|Rp.4000            |')
            print('|2. |Rissol mayo lumer     |Rp.4000            |')
            print('+=+=+=++================================++=+=+=+')
            print()

            Banyak_jenisri  = int(input("Masukan Banyak Jenis Yang Ingin Di Beli : "))
            nomor           = []
            Banyak_produkri = []
            Jenis_produkri  = []
            Harga           = []
            Jumlah          = []

            print('+=+=+=++================================++=+=+=+')

            stock=0
            while stock<Banyak_jenisri:
                print("Jenis ke - ",stock +1)
                nomor.append(str(input("No Produk  : ")))
                try:
                    Banyak_produkri.append(int(input("Mau beli berapa banyak rissol : ")))
                except ValueError:
                    print(" salah ")
                    continue
                if nomor[stock] == "1" :
                    Jenis_produkri.append("rissoles ayam suir pedas")
                    Harga.append("4000   ")
                    Jumlah.append(Banyak_produkri[stock]*int("4000"))
                elif nomor[stock] == "2" :
                    Jenis_produkri.append("rissoles mayo lumer     ")
                    Harga.append("4000   ")
                    Jumlah.append(Banyak_produkri[stock]*int("4000"))
                else :
                    Jenis_produkri.append("Your Code Wrong")
                    Harga.append("0")
                    Jumlah.append(Banyak_produkri[stock]*int("0"))
                
                stock = stock + 1

            print('=================================================================')
            print("                       RINCIAN PEMBELIAN                         ")
            print('=================================================================')
            print("|No.|Nama produk             |Harga    |jumlah    |Jumlah        ")
            print("|   |                        |         |pembelian |              ")
            print('=================================================================')

            Jumlah_bayar=0
            Order=0
            while Order < Banyak_jenisri:
                Jumlah_bayar += Jumlah[Order]
                print("|%i  |%s|%s  |%i         |%i"%(Order+1,Jenis_produkri[Order],Harga[Order],Banyak_produkri[Order],Jumlah[Order]))
                Order= Order + 1

            pajak= Jumlah_bayar * 0.3
            total_bayar = Jumlah_bayar + pajak

            print('=================================================================')
            print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
            print(            "Pajak admin  Rp.",+int(pajak)                     )
            print(            "Total bayar  Rp.",+int(total_bayar)               )
            print('=================================================================')

            makmin=input("anda ingin lanjut membayar rincian pembelian (y/n) : ")

            if makmin=='y':
                if saldoal<total_bayar :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
                elif saldoal >= total_bayar: 
                    print('=================================================================')
                    print("                   STRUK PEMBELIAN RISSOLES 69                   ")
                    print('=================================================================')
                    print("|No.|Nama produk             |Harga    |jumlah    |Jumlah        ")
                    print("|   |                        |         |pembelian |              ")
                    print('=================================================================')
                    Jumlah_bayar=0
                    Order=0
                    while Order < Banyak_jenisri:
                        Jumlah_bayar += Jumlah[Order]
                        print("|%i  |%s|%s  |%i         |%i"%(Order+1,Jenis_produkri[Order],Harga[Order],Banyak_produkri[Order],Jumlah[Order]))
                        Order= Order + 1

                    pajak= Jumlah_bayar * 0.3
                    total_bayar = Jumlah_bayar + pajak


                    print('=================================================================')
                    print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
                    print(            "Pajak admin  Rp.",+int(pajak)                     )
                    print(            "Total bayar  Rp.",+int(total_bayar)               )
                    print(            "saldo saku   Rp.",+int(saldoal)                   )
                    saldoal=saldoal-total_bayar
                    print(            "sisa saku    Rp.",+int(saldoal)                   )
                    print('=================================================================')

        elif makmin == '2':
            print('+=+=+=++================================++=+=+=+')
            print('|___________Menu sabung pried ciken____________|')
            print('+=+=+=++================================++=+=+=+')
            print('|No |jenis potongan           |Harga           |')
            print('|1. |Dada ayam                |Rp.5000         |')
            print('|2. |Paha ayam                |Rp.4500         |')
            print('|3. |sayap ayam               |Rp.3500         |')
            print('|4. |kulit ayam               |Rp.1000         |')
            print('|5. |ceker ayam               |Rp.1000         |')
            print('+=+=+=++================================++=+=+=+')
            print()

            Banyak_jenis    = int(input("Masukan Banyak Jenis Yang Ingin Di Beli : "))
            nomor           = []
            Banyak_potongan = []
            Jenis_potongan  = []
            Harga           = []
            Jumlah          = []

            print('+=+=+=++================================++=+=+=+')

            stock=0
            while stock<Banyak_jenis:
                print("Jenis ke - ",stock +1)
                nomor.append(str(input("No Potongan  : ")))
                try:
                    Banyak_potongan.append(int(input("Banyak Potongan : ")))
                except ValueError:
                    print(" salah ")
                    continue
                if nomor[stock] == "1" :
                    Jenis_potongan.append("dada ayam               ")
                    Harga.append("5000     ")
                    Jumlah.append(Banyak_potongan[stock]*int("5000"))
                elif nomor[stock] == "2" :
                    Jenis_potongan.append("paha ayam               ")
                    Harga.append("4500     ")
                    Jumlah.append(Banyak_potongan[stock]*int("4500"))
                elif nomor[stock] == "3" :
                    Jenis_potongan.append("sayap ayam              ")
                    Harga.append("4500     ")
                    Jumlah.append(Banyak_potongan[stock]*int("3500"))
                elif nomor[stock] == "4" :
                    Jenis_potongan.append("kulit ayam              ")
                    Harga.append("1000     ")
                    Jumlah.append(Banyak_potongan[stock]*int("1000"))
                elif nomor[stock] == "5" :
                    Jenis_potongan.append("ceker ayam              ")
                    Harga.append("1000     ")
                    Jumlah.append(Banyak_potongan[stock]*int("1000"))
                else :
                    Jenis_potongan.append("Your Code Wrong")
                    Harga.append("0")
                    Jumlah.append(Banyak_potongan[stock]*int("0"))
                
                stock = stock + 1

            print('=================================================================')
            print("                       RINCIAN PEMBELIAN                         ")
            print('=================================================================')
            print("|No.|Nama produk             |Harga    |jumlah    |Jumlah        ")
            print("|   |                        |         |pembelian |              ")
            print('=================================================================')

            Jumlah_bayar=0
            Order=0
            while Order < Banyak_jenis:
                Jumlah_bayar += Jumlah[Order]
                print("|%i  |%s|%s|%i         |%i   "%(Order+1,Jenis_potongan[Order],Harga[Order],Banyak_potongan[Order],Jumlah[Order]))
                Order= Order + 1

            pajak= Jumlah_bayar * 0.3
            total_bayar = Jumlah_bayar + pajak

            print('=================================================================')
            print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
            print(            "Pajak admin  Rp.",+int(pajak)                     )
            print(            "Total bayar  Rp.",+int(total_bayar)               )
            print('=================================================================')

            makmin=input("anda ingin lanjut membayar rincian pembelian (y/n) : ")

            if makmin=='y':
                if saldoal<total_bayar :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
                elif saldoal >= total_bayar: 
                    print('=================================================================')
                    print("              STRUK PEMBELIAN SABUNG PRIED CHICKEN               ")
                    print('=================================================================')
                    print("|No.|Nama produk             |Harga    |jumlah    |Jumlah        ")
                    print("|   |                        |         |pembelian |              ")
                    print('=================================================================')

                    Jumlah_bayar=0
                    Order=0
                    while Order < Banyak_jenis:
                        Jumlah_bayar += Jumlah[Order]
                        print("|%i  |%s|%s|%i         |%i   "%(Order+1,Jenis_potongan[Order],Harga[Order],Banyak_potongan[Order],Jumlah[Order]))
                        Order= Order + 1

                    pajak= Jumlah_bayar * 0.3
                    total_bayar = Jumlah_bayar + pajak


                    print('==================================================================')
                    print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
                    print(            "Pajak admin  Rp.",+int(pajak)                     )
                    print(            "Total bayar  Rp.",+int(total_bayar)               )
                    print(            "saldo saku   Rp.",+int(saldoal)                   )
                    saldoal=saldoal-total_bayar
                    print(            "sisa saku    Rp.",+int(saldoal)                   )
                    print('==================================================================')
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")

        elif makmin == '3':
            print('+=+=+=++================================++=+=+=+')
            print('|________________Menu burhotbab________________|')
            print('+=+=+=++================================++=+=+=+')
            print('|No |jenis Produk             |Harga           |')
            print('|1. |Burger ligma             |Rp.7000         |')
            print('|2. |Hotdog fuad              |Rp.6500         |')
            print('|3. |Kebab dimas              |Rp.8000         |')
            print('+=+=+=++================================++=+=+=+')
            print()

            Banyak_jenisbur  = int(input("Masukan Banyak Jenis Yang Ingin Di Beli : "))
            nomor            = []
            Banyak_produkbur = []
            Jenis_produkbur  = []
            Harga            = []
            Jumlah           = []

            print('+=+=+=++================================++=+=+=+')

            stock=0
            while stock<Banyak_jenisbur:
                print("Jenis ke - ",stock +1)
                nomor.append(str(input("No Produk  : ")))
                try:
                    Banyak_produkbur.append(int(input("Banyak Produk yang ingin anda beli : ")))
                except ValueError:
                    print(" salah ")
                    continue
                if nomor[stock] == "1" :
                    Jenis_produkbur.append("Burger ligma      ")
                    Harga.append("7000   ")
                    Jumlah.append(Banyak_produkbur[stock]*int("7000"))
                elif nomor[stock] == "2" :
                    Jenis_produkbur.append("hotdog Fuad       ")
                    Harga.append("6500   ")
                    Jumlah.append(Banyak_produkbur[stock]*int("6500"))
                elif nomor[stock] == "3" :
                    Jenis_produkbur.append("Kebab dimas       ")
                    Harga.append("8000   ")
                    Jumlah.append(Banyak_produkbur[stock]*int("8000"))
                else :
                    Jenis_produkbur.append("Your Code Wrong")
                    Harga.append("0")
                    Jumlah.append(Banyak_produkbur[stock]*int("0"))
                
                stock = stock + 1

            print('=================================================================')
            print("                       RINCIAN PEMBELIAN                         ")
            print('=================================================================')
            print("|No.|Nama produk       |Harga  |jumlah    |Jumlah                ")
            print("|   |                  |       |pembelian |                      ")
            print('=================================================================')

            Jumlah_bayar=0
            Order=0
            while Order < Banyak_jenisbur:
                Jumlah_bayar += Jumlah[Order]
                print("|%i  |%s|%s|%i         |%i   "%(Order+1,Jenis_produkbur[Order],Harga[Order],Banyak_produkbur[Order],Jumlah[Order]))
                Order= Order + 1

            pajak= Jumlah_bayar * 0.3
            total_bayar = Jumlah_bayar + pajak
            print('=================================================================')
            print(            "Jumlah bayar Rp.",Jumlah_bayar                        )
            print(            "Pajak admin  Rp.",+int(pajak)                         )
            print(            "Total bayar  Rp.",+int(total_bayar)                   )
            print('=================================================================')

            makmin=input("anda ingin lanjut membayar rincian pembelian (y/n) : ")

            if makmin=='y':
                if saldoal<total_bayar :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
                elif saldoal >= total_bayar: 
                    print('=================================================================')
                    print("                    STRUK PEMBELIAN BURHOTBAB                    ")
                    print('=================================================================')
                    print("|No.|Nama produk       |Harga  |jumlah    |Jumlah                ")
                    print("|   |                  |       |pembelian |                      ")
                    print('=================================================================')


                    Jumlah_bayar=0
                    Order=0
                    while Order < Banyak_jenisbur:
                        Jumlah_bayar += Jumlah[Order]
                        print("|%i  |%s|%s|%i         |%i   "%(Order+1,Jenis_produkbur[Order],Harga[Order],Banyak_produkbur[Order],Jumlah[Order]))
                        Order= Order + 1

                    pajak= Jumlah_bayar * 0.3
                    total_bayar = Jumlah_bayar + pajak

                    print('=================================================================')
                    print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
                    print(            "Pajak admin  Rp.",+int(pajak)                     )
                    print(            "Total bayar  Rp.",+int(total_bayar)               )
                    print(            "saldo saku   Rp.",+int(saldoal)                   )
                    saldoal=saldoal-total_bayar
                    print(            "sisa saku    Rp.",+int(saldoal)                    )
                    print('=================================================================')
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
                    
        elif makmin == '4':
            print('+=+=+=++================================++=+=+=+')
            print('|_____________Menu sugmadik fresh______________|')
            print('+=+=+=++================================++=+=+=+')
            print('|No |jenis Minuman            |Harga           |')
            print('|1. |Es teh jawir             |Rp.3000         |')
            print('|2. |Es jeruk                 |Rp.4500         |')
            print('|3. |Es Buah                  |Rp.6000         |')
            print('+=+=+=++================================++=+=+=+')
            print()

            Banyak_jenissug  = int(input("Masukan Banyak Jenis Yang Ingin Di Beli : "))
            nomor            = []
            Banyak_produksug = []
            Jenis_produksug  = []
            Harga            = []
            Jumlah           = []

            print('+=+=+=++================================++=+=+=+')

            stock=0
            while stock<Banyak_jenissug:
                print("Jenis ke - ",stock +1)
                nomor.append(str(input("No Produk  : ")))
                try:
                    Banyak_produksug.append(int(input("Anda ingin beli berapa banyak : ")))
                except ValueError:
                    print(" salah ")
                    continue
                if nomor[stock] == "1" :
                    Jenis_produksug.append("Es teh jawir      ")
                    Harga.append("3000 ")
                    Jumlah.append(Banyak_produksug[stock]*int("3000"))
                elif nomor[stock] == "2" :
                    Jenis_produksug.append("Es jeruk          ")
                    Harga.append("4500 ")
                    Jumlah.append(Banyak_produksug[stock]*int("4500"))
                elif nomor[stock] == "3" :
                    Jenis_produksug.append("Es buah           ")
                    Harga.append("6000 ")
                    Jumlah.append(Banyak_produksug[stock]*int("6000"))
                else :
                    Jenis_produksug.append("Your Code Wrong")
                    Harga.append("0")
                    Jumlah.append(Banyak_produksug[stock]*int("0"))
                    
                stock = stock + 1

            print('=================================================================')
            print("                       RINCIAN PEMBELIAN                         ")
            print('=================================================================')
            print("|No.|Nama produk       |Harga  |jumlah    |Jumlah                ")
            print("|   |                  |       |pembelian |                      ")
            print('=================================================================')

            Jumlah_bayar=0
            Order=0
            while Order < Banyak_jenissug:
                Jumlah_bayar += Jumlah[Order]
                print("|%i  |%s|%s  |%i         |%i"%(Order+1,Jenis_produksug[Order],Harga[Order],Banyak_produksug[Order],Jumlah[Order]))
                Order= Order + 1

            pajak= Jumlah_bayar * 0.3
            total_bayar = Jumlah_bayar + pajak

            print('=============================================================')
            print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
            print(            "Pajak admin  Rp.",+int(pajak)                     )
            print(            "Total bayar  Rp.",+int(total_bayar)               )
            print('=============================================================')

            makmin=input("anda ingin lanjut membayar rincian pembelian (y/n) : ")

            if makmin=='y':
                if saldoal<total_bayar :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
                elif saldoal >= total_bayar: 
                    print('=================================================================')
                    print("                  STRUK PEMBELIAN SUGMADIK FRESH                 ")
                    print('=================================================================')
                    print("|No.|Nama produk       |Harga  |jumlah    |Jumlah                ")
                    print("|   |                  |       |pembelian |                      ")
                    print('=================================================================')


                    Jumlah_bayar=0
                    Order=0
                    while Order < Banyak_jenissug:
                        Jumlah_bayar += Jumlah[Order]
                        print("|%i  |%s|%s  |%i         |%i"%(Order+1,Jenis_produksug[Order],Harga[Order],Banyak_produksug[Order],Jumlah[Order]))
                        Order= Order + 1

                    pajak= Jumlah_bayar * 0.3
                    total_bayar = Jumlah_bayar + pajak


                    print('=============================================================')
                    print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
                    print(            "Pajak admin  Rp.",+int(pajak)                     )
                    print(            "Total bayar  Rp.",+int(total_bayar)               )
                    print(            "saldo saku   Rp.",+int(saldoal)                   )
                    saldoal=saldoal-total_bayar
                    print(            "sisa saku    Rp.",+int(saldoal)                   )
                    print('=============================================================')
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")

        elif makmin == '5':
            print('+=+=+=++================================++=+=+=+')
            print('|_________________Menu moonbuck________________|')
            print('+=+=+=++================================++=+=+=+')
            print('|No |jenis potongan           |Harga           |')
            print('|1. |Coffee cykablyat         |Rp.9000         |')
            print('|2. |Coffee americano         |Rp.7500         |')
            print('|3. |Coffee Latte             |Rp.6500         |')
            print('+=+=+=++================================++=+=+=+')
            print()

            Banyak_jenismoo  = int(input("Masukan Banyak Jenis Yang Ingin Di Beli : "))
            nomor            = []
            Banyak_produkmoo = []
            Jenis_produkmoo  = []
            Harga            = []
            Jumlah           = []

            print('+=+=+=++================================++=+=+=+')

            stock=0
            while stock<Banyak_jenismoo:
                print("Jenis ke - ",stock +1)
                nomor.append(str(input("No Potongan  : ")))
                try:
                    Banyak_produkmoo.append(int(input("mau beli berapa banyak produk : ")))
                except ValueError:
                    print(" salah ")
                    continue
                if nomor[stock] == "1" :
                    Jenis_produkmoo.append("Coffee cykablyat  ")
                    Harga.append("9000   ")
                    Jumlah.append(Banyak_produkmoo[stock]*int("9000"))
                elif nomor[stock] == "2" :
                    Jenis_produkmoo.append("Coffee americano  ")
                    Harga.append("7500   ")
                    Jumlah.append(Banyak_produkmoo[stock]*int("7500"))
                elif nomor[stock] == "3" :
                    Jenis_produkmoo.append("Coffee Latte      ")
                    Harga.append("6500   ")
                    Jumlah.append(Banyak_produkmoo[stock]*int("6500"))
                else :
                    Jenis_produkmoo.append("Your Code Wrong")
                    Harga.append("0")
                    Jumlah.append(Banyak_produkmoo[stock]*int("0"))
                
                stock = stock + 1

            print('=================================================================')
            print("                       RINCIAN PEMBELIAN                         ")
            print('=================================================================')
            print("|No.|Nama produk       |Harga  |jumlah    |Jumlah                ")
            print("|   |                  |       |pembelian |                      ")
            print('=================================================================')

            Jumlah_bayar=0
            Order=0
            while Order < Banyak_jenismoo:
                Jumlah_bayar += Jumlah[Order]
                print("|%i  |%s|%s|%i         |%i"%(Order+1,Jenis_produkmoo[Order],Harga[Order],Banyak_produkmoo[Order],Jumlah[Order]))
                Order= Order + 1

            pajak= Jumlah_bayar * 0.3
            total_bayar = Jumlah_bayar + pajak

            print('=================================================================')
            print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
            print(            "Pajak admin  Rp.",+int(pajak)                     )
            print(            "Total bayar  Rp.",+int(total_bayar)               )
            print('=================================================================')

            makmin=input("anda ingin lanjut membayar rincian pembelian (y/n) : ")

            if makmin=='y':
                if saldoal<total_bayar :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
                elif saldoal >= total_bayar: 
                    print('=================================================================')
                    print("                    STRUK PEMBELIAN MOONBUCK                     ")
                    print('=================================================================')
                    print("|No.|Nama produk       |Harga  |jumlah    |Jumlah                ")
                    print("|   |                  |       |pembelian |                      ")
                    print('=================================================================')

                    Jumlah_bayar=0
                    Order=0
                    while Order < Banyak_jenismoo:
                        Jumlah_bayar += Jumlah[Order]
                        print("|%i  |%s|%s|%i         |%i"%(Order+1,Jenis_produkmoo[Order],Harga[Order],Banyak_produkmoo[Order],Jumlah[Order]))
                        Order= Order + 1

                    pajak= Jumlah_bayar * 0.3
                    total_bayar = Jumlah_bayar + pajak


                    print('=================================================================')
                    print(            "Jumlah bayar Rp.",Jumlah_bayar                        )
                    print(            "Pajak admin  Rp.",+int(pajak)                         )
                    print(            "Total bayar  Rp.",+int(total_bayar)                   )
                    print(            "saldo saku   Rp.",+int(saldoal)                       )
                    saldoal=saldoal-total_bayar
                    print(            "sisa saku    Rp.",+int(saldoal)                       )
                    print('=================================================================')
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")

        elif makmin == '6':
            print('+=+=+=++================================++=+=+=+')
            print('|_____________Menu Ice wallow come_____________|')
            print('+=+=+=++================================++=+=+=+')
            print('|No |jenis potongan           |Harga           |')
            print('|1. |ice cream cone           |Rp.3000         |')
            print('|2. |ice float chocolate      |Rp.5500         |')
            print('|3. |ice bucket creamy 1L     |Rp.10000        |')
            print('+=+=+=++================================++=+=+=+')
            print()

            Banyak_jenisice  = int(input("Masukan Banyak Jenis Yang Ingin Di Beli : "))
            nomor            = []
            Banyak_produkice = []
            Jenis_produkice  = []
            Harga            = []
            Jumlah           = []

            print('+=+=+=++================================++=+=+=+')

            stock=0
            while stock<Banyak_jenisice:
                print("Jenis ke - ",stock +1)
                nomor.append(str(input("No Produk  : ")))
                try:
                    Banyak_produkice.append(int(input("Anda ingin beli berapa banyak : ")))
                except ValueError:
                    print(" salah ")
                    continue
                if nomor[stock] == "1" :
                    Jenis_produkice.append("ice cream cone       ")
                    Harga.append("3000   ")
                    Jumlah.append(Banyak_produkice[stock]*int("3000"))
                elif nomor[stock] == "2" :
                    Jenis_produkice.append("ice float chocolate  ")
                    Harga.append("5500   ")
                    Jumlah.append(Banyak_produkice[stock]*int("5500"))
                elif nomor[stock] == "3" :
                    Jenis_produkice.append("ice bucket creamy 1L ")
                    Harga.append("10000  ")
                    Jumlah.append(Banyak_produkice[stock]*int("10000"))
                else :
                    Jenis_produkice.append("Your Code Wrong")
                    Harga.append("0")
                    Jumlah.append(Banyak_produkice[stock]*int("0"))
                
                stock = stock + 1

            print('=================================================================')
            print("                       RINCIAN PEMBELIAN                         ")
            print('=================================================================')
            print("|No.|Nama produk          |Harga  |jumlah    |Jumlah             ")
            print("|   |                     |       |pembelian |                   ")
            print('=================================================================')

            Jumlah_bayar=0
            Order=0
            while Order < Banyak_jenisice:
                Jumlah_bayar += Jumlah[Order]
                print("|%i  |%s|%s|%i         |%i"%(Order+1,Jenis_produkice[Order],Harga[Order],Banyak_produkice[Order],Jumlah[Order]))
                Order= Order + 1

            pajak= Jumlah_bayar * 0.3
            total_bayar = Jumlah_bayar + pajak

            print('=================================================================')
            print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
            print(            "Pajak admin  Rp.",+int(pajak)                     )
            print(            "Total bayar  Rp.",+int(total_bayar)               )
            print('=================================================================')

            makmin=input("anda ingin lanjut membayar rincian pembelian (y/n) : ")

            if makmin=='y':
                if saldoal<total_bayar :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
                elif saldoal >= total_bayar: 
                    print('=================================================================')
                    print("                 STRUK PEMBELIAN ICE WALLOW CUM                  ")
                    print('=================================================================')
                    print("|No.|Nama produk          |Harga  |jumlah    |Jumlah             ")
                    print("|   |                     |       |pembelian |                   ")
                    print('=================================================================')

                    Jumlah_bayar=0
                    Order=0
                    while Order < Banyak_jenisice:
                        Jumlah_bayar += Jumlah[Order]
                        print("|%i  |%s|%s|%i         |%i"%(Order+1,Jenis_produkice[Order],Harga[Order],Banyak_produkice[Order],Jumlah[Order]))
                        Order= Order + 1

                    pajak= Jumlah_bayar * 0.3
                    total_bayar = Jumlah_bayar + pajak

                    print('=================================================================')
                    print(            "Jumlah bayar Rp.",Jumlah_bayar                    )
                    print(            "Pajak admin  Rp.",+int(pajak)                     )
                    print(            "Total bayar  Rp.",+int(total_bayar)               )
                    print(            "saldo saku   Rp.",+int(saldoal)                   )
                    saldoal=saldoal-total_bayar
                    print(            "sisa saku    Rp.",+int(saldoal)                    )
                    print('=================================================================')
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")

        elif makmin == '7':

            pilihan=input('anda ingin kembali ke menu awal (y/n) : ')
        
        else :
            print('input salah')
        
    elif menu == '5' :
        print('+=+=+=++======================================================++=+=+=+')
        print('|________________________List jadwal penerbangan_____________________|')
        print('+=+=+=++======================================================++=+=+=+')
        print('|Kode penerbangan  |pesawat        |tujuan     |Harga tiket          |')
        print('|101               |Garuda Air     |sulsel     |Rp.200000            |')
        print('|102               |Batavia        |sumut      |Rp.155000            |')
        print('|103               |Sriwijaya      |NTT        |Rp.403500            |')
        print('|104               |Airasia        |NTB        |Rp.350000            |')
        print('|105               |Citilink       |papua      |Rp.410000            |')
        print('+=+=+=++======================================================++=+=+=+')
        print('Ada diskon di setiap pembelian 2 orang/10% ,3 orang/50% ,4 orang/80%  ')
        print('+=+=+=++======================================================++=+=+=+')
        print()
            
        namapem         = input("Nama pembeli : ")
        nomor           = input("Nomor Handphone : ")
        asal            = input("Asal kota : ")
        kode            = input("kode tujuan penerbangan : ")
        pesawat         = []
        tujuan          = []
        hargape         = []

        if kode == "101":
            pesawat.append("Garuda Air")
            tujuan.append("Sulawesi Selatan")
            hargape = 200000
        elif kode == "102":
            pesawat.append("Garuda Air")
            tujuan.append("Sumatra Utara")
            hargape = 155000
        elif kode == "103":
            pesawat.append("Garuda Air")
            tujuan.append("Nusa Tenggara Timur")
            hargape = 403500
        elif kode == "104":
            pesawat.append("Garuda Air")
            tujuan.append("Nusa Tenggara Barat")
            hargape = 350000
        elif kode == "105":
            pesawat.append("Garuda Air")
            tujuan.append("Papua")
            hargape = 410000
        else:
            tujuan.append("kode salah")

        jumlahpen=int(input("jumlah pembelian : "))
        print()
        if jumlahpen == 2 :
            disko =(jumlahpen*hargape)*0.1
        elif jumlahpen == 3 :
            disko =(jumlahpen*hargape)*0.5
        elif jumlahpen >= 4 :
            disko =(jumlahpen*hargape)*0.8
        else:
            disko = 0

        totalpen = int(jumlahpen*hargape-disko)
        pajak = totalpen*0.05
        pembay=totalpen+pajak
        print('=================================================================')
        print("|                Struk pembelian ticket pesawat                 |")
        print('=================================================================')
        print("Nama Pembeli     :", namapem                                      )
        print("Nomor Handphone  :", nomor                                        )
        print("Asal Negara      :", asal                                         )
        print("Kode Penerbangan :", kode                                         )
        print("pesawat          :", pesawat                                      )
        print("Negara Tujuan    :", tujuan                                       )
        print("Jumlah Beli      :", jumlahpen                                    )
        print('=================================================================')
        print("Harga Ticket     :", hargape                                      )
        print("Diskon           :", disko                                        )
        print("PPN 10%          :", pajak                                        )
        print("Total Pembayaran :", pembay                                       )
        print('=================================================================')

        pembayaranPEN=input("Anda ingin melanjutkan pembayaran ticket pesawat(y/n) : ")

        if pembayaranPEN == 'y' :
            if saldoal<pembay :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            elif saldoal>pembay :
                saldoal=saldoal - pembay
                print('=================================================================')
                print("|                Struk pembelian ticket pesawat                 |")
                print('=================================================================')
                print("Nama Pembeli     :", namapem                                      )
                print("Nomor Handphone  :", nomor                                        )
                print("Asal Negara      :", asal                                         )
                print("Kode Penerbangan :", kode                                         )
                print("Pesawat          :", pesawat                                      )
                print("Negara Tujuan    :", tujuan                                       )
                print("Jumlah Beli      :", jumlahpen                                    )
                print('=================================================================')
                print("Harga Ticket     :", hargape                                      )
                print("Diskon           :", disko                                        )
                print("PPN 10%          :", pajak                                        )
                print("Total Pembayaran :", pembay                                       )
                print('=================================================================')
                print("Total sakusakaw anda :", saldoal,"                               ")
                print('=================================================================')
                print('            Kode pengambilan ticket pesawat anda                 ')
                print(random.randint(0000000000, 9999999999)) 
                print('=================================================================')
                print("|  masukan kode tiket pesawat anda di mesin pengambilan ticket  |")
                print('=================================================================')
                print("|       TERIMA KASIH SUDAH MENGGUNAKAN LAYANAN SAKUSAKAW        |")
                print("|               ENJOY YOUR FLIGHT SAFE AND SOUND                |")
                print('=================================================================')
                pilihan = input("anda ingin kembali ke menu awal (y/n): ")

        elif pembayaranPEN == 'n' :
             pilihan = input("anda ingin kembali ke menu awal (y/n): ")

    elif menu == '7' :
        print('+=+=+=++==============================================================++=+=+=+')
        print('|_____________________________List jadwal kapal______________________________|')
        print('+=+=+=++==============================================================++=+=+=+')
        print('|Kode kapal        |nama kapal   |asal       |Tujuan     | Harga tiket       |')
        print('|201               |Dorolonda    |Sumatra    |Sulawesi   | Rp.125000         |')
        print('|202               |Umsni        |Jawa       |NTT        | Rp.135000         |')
        print('|203               |Dobonsolo    |Sulawesi   |Papua      | Rp.115000         |')
        print('|204               |Nggapulu     |NTB        |Kalimantan | Rp.125000         |')
        print('|205               |Kelud        |Kalimantan |Sumatra    | Rp.110000         |')
        print('+=+=+=++==============================================================++=+=+=+')
        print('     Ada diskon di setiap pembelian 2 orang/20% ,3 orang/40% ,4 orang/60%     ')
        print('+=+=+=++==============================================================++=+=+=+')

        print()
            
        namapemkap         = input("Nama pembeli : ")
        nomorkap           = input("Nomor Handphone : ")
        asalkap            = input("Asal kota : ")
        kodekap            = input("kode Kapal : ")
        namakap            = []
        asalkap            = []
        tujuankap          = []
        hargakap           = []

        if kodekap == "201":
            namakap.append("Dorolonda")
            asalkap.append("Sumatra")
            tujuankap.append("Sulawesi")
            hargakap = 125000
        elif kodekap == "202":
            namakap.append("Umsni")
            asalkap.append("Jawa")
            tujuankap.append("NTT")
            hargakap = 135000
        elif kode == "203":
            namakap.append("Dobonsolo")
            asalkap.append("Sulawesi")
            tujuankap.append("Papua")
            hargakap = 115000
        elif kodekap == "204":
            namakap.append("Nggapulu")
            asalkap.append("NTB")
            tujuankap.append("Kalimantan")
            hargakap = 125000
        elif kodekap == "205":
            namakap.append("Kelud")
            asalkap.append("Kalimantan")
            tujuankap.append("Sumatra")
            hargape = 110000
        else:
            tujuankap.append("kode salah")

        jumlahkap=int(input("jumlah pembelian : "))
        print()
        if jumlahkap == 2 :
            diskokap =(jumlahkap*hargakap)*0.2
        elif jumlahkap == 3 :
            diskokap =(jumlahkap*hargakap)*0.4
        elif jumlahkap >= 4 :
            diskokap =(jumlahkap*hargakap)*0.6
        else:
            diskokap = 0

        totalkap = int(jumlahkap*hargakap-diskokap)
        pajakkap = totalkap*0.05
        pembaykap=totalkap+pajakkap
        print('=================================================================')
        print("|                Rincian pembelian ticket kapal                 |")
        print('=================================================================')
        print("Nama pembeli     :", namapemkap                                   )
        print("Nomor handphone  :", nomorkap                                     )
        print("Asal Kota        :", asalkap                                      )
        print("Kode Kapal       :", kodekap                                      )
        print("Nama Kapal       :", namakap                                      )
        print("Negara tujuan    :", tujuankap                                    )
        print("Jumlah beli      :", jumlahkap                                    )
        print('=================================================================')
        print("Harga ticket     :", hargakap                                     )
        print("Diskon           :", diskokap                                     )
        print("PPN 10%          :", pajakkap                                     )
        print("Total Pembayaran :", pembaykap                                    )
        print('=================================================================')

        pembayaranKap=input("Anda ingin melanjutkan pembayaran ticket pesawat(y/n) : ")

        if pembayaranKap == 'y' :
            if saldoal < pembaykap :
                    print("maaf saldo saku anda tidak mencukupi untuk pembayaran ini silahkan top up terlebih dahulu")
                    pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            elif saldoal > pembaykap :
                saldoal=saldoal - pembaykap
                print('=================================================================')
                print("|                Rincian pembelian ticket kapal                 |")
                print('=================================================================')
                print("Nama pembeli     :", namapemkap                                   )
                print("Nomor handphone  :", nomorkap                                     )
                print("Asal negara      :", asalkap                                      )
                print("Kode Kapal       :", kodekap                                      )
                print("Nama Kapal       :", namakap                                      )
                print("Negara tujuan    :", tujuankap                                    )
                print("Jumlah beli      :", jumlahkap                                    )
                print('=================================================================')
                print("Harga ticket     :", hargakap                                     )
                print("Diskon           :", diskokap                                     )
                print("PPN 10%          :", pajakkap                                     )
                print("Total Pembayaran :", pembaykap                                    )
                print('=================================================================')
                print("total sakusakaw anda :", saldoal,"                               ")
                print('=================================================================')
                print('              Kode pengambilan ticket kapal anda                 ')
                print(random.randint(0000000000, 9999999999)) 
                print('=================================================================')
                print("|   masukan kode tiket Kapal anda di mesin pengambilan ticket   |")
                print('=================================================================')
                print("|       TERIMA KASIH SUDAH MENGGUNAKAN LAYANAN SAKUSAKAW        |")
                print('=================================================================')
                pilihan = input("anda ingin kembali ke menu awal (y/n): ")
            
    

    elif menu == '8' : 
        print("anda akan keluar dari program sakusakaw")
        pilihan = input('anda ingin kembali ke program sakusakaw (y/n):  ')
        if pilihan == 'n' :
            print("TERIMA KASIH SUDAH MENGGUNAKAN SAKUSAKAW")
            print()
            exit()                        