invoiceList = [
    {
        'NOMOR NOTA': 'INV001',
        'CUSTOMER': 'Millo',
        'SKU BARANG': 'BAG001',
        'HARGA BARANG': '50000',
        'QTY': '2',
    },
    {
        'NOMOR NOTA': 'INV002',
        'CUSTOMER': 'Momo',
        'SKU BARANG': 'PEN003',
        'HARGA BARANG': '2000',
        'QTY': '5',
    },
]

def mainMenu():
    while(True):
        print("\n=======================Penjualan Barang Toko=======================")

        print('''
        1. Laporan Data Penjualan
        2. Tambah Data Penjualan
        3. Ubah Data Penjualan
        4. Hapus Data Penjualan
        5. Exit
        ''')

        inputMainMenu = input("Silakan Pilih Main Menu [1-5] : ")
        if (inputMainMenu == '1'):
            menuLaporan()
        elif (inputMainMenu == '2'):
            menuTambah()
        elif (inputMainMenu == '3'):
            menuUbah()
        elif (inputMainMenu == '4'):
            menuHapus()
        elif (inputMainMenu == '5'):
            print("Terima Kasih dan Sampai Jumpa!")
            break
        else:
            inputanSalah()

def menuLaporan():
    while(True):
        print("\n=======================Laporan Data Penjualan=======================")

        print('''
        1. Laporan Seluruh Data
        2. Laporan Data Tertentu
        3. Kembali ke Menu Utama
        ''')

        inputSubMenu = input("Silakan Pilih Sub Menu Laporan [1-3] : ")
        if (inputSubMenu == '1'):
            laporanAllData()
        elif (inputSubMenu == '2'):
            laporanByInv()
        elif (inputSubMenu == '3'):
            break
        else:
            inputanSalah()

def menuTambah():
    while(True):
        print("\n=======================Tambah Data Penjualan=======================")

        print('''
        1. Tambah Data Penjualan
        2. Kembali ke Menu Utama
        ''')

        inputSubMenu = input("Silakan Pilih Sub Menu Tambah Data [1-2] : ")
        if (inputSubMenu == '1'):
            insertData()
        elif (inputSubMenu == '2'):
            break
        else:
            inputanSalah()

def menuUbah():
    while(True):
        print("\n=======================Ubah Data Penjualan=======================")

        print('''
        1. Ubah Data Penjualan
        2. Kembali ke Menu Utama
        ''')

        inputSubMenu = input("Silakan Pilih Sub Menu Ubah Data [1-2] : ")
        if (inputSubMenu == '1'):
            updateData()
        elif (inputSubMenu == '2'):
            break
        else:
            inputanSalah()

def menuHapus():
    while(True):
        print("\n=======================Hapus Data Penjualan=======================")

        print('''
        1. Hapus Data Penjualan
        2. Kembali ke Menu Utama
        ''')

        inputSubMenu = input("Silakan Pilih Sub Menu Hapus Data [1-2] : ")
        if (inputSubMenu == '1'):
            deleteData()
        elif (inputSubMenu == '2'):
            break
        else:
            inputanSalah()

def inputanSalah():
    print("Pilihan yang Anda Masukkan Salah")

def dataNotFound():
    print("Data Tidak Ditemukan")

def laporanAllData():
    print("Laporan Penjualan : ")
    
    if not invoiceList:
        dataNotFound()
    else:
        printEnumerateInv(invoiceList)

def laporanByInv():
    inputNota = inputNotaFunc()
    print("Laporan Penjualan Dengan Nomor ",inputNota)
    filterInvoice = filterInvoiceFunc(inputNota)

    if not filterInvoice:
        dataNotFound()
    else:
        printEnumerateInv(filterInvoice)

def insertData():
    inputNoNota = inputNotaFunc()
    filterInvoice = filterInvoiceFunc(inputNoNota)
    
    if filterInvoice:
        print('Data Sudah Ada')
        
    else:
        inputCustomer = input("Masukkan Customer : ")
        inputSKU = input("Masukkan SKU Barang : ").upper()
        inputHarga = input("Masukkan Harga Barang : ")
        inputQty = input("Masukkan Jumlah Pembelian : ")

        while(True):
            inputConfirmation = input("Apakah Data Akan Disimpan? (Y/N) : ")
            if (inputConfirmation == 'Y' or inputConfirmation == 'y'):
                invoiceList.append(
                    {
                        'NOMOR NOTA': inputNoNota,
                        'CUSTOMER': inputCustomer,
                        'SKU BARANG': inputSKU,
                        'HARGA BARANG': inputHarga,
                        'QTY': inputQty,
                    }
                )
                print("Data Tersimpan")
                break
            elif (inputConfirmation == 'N' or inputConfirmation == 'n'):
                print("Data Tidak Tersimpan")
                break
            else:
                inputanSalah()

def updateData():
    inputNota = inputNotaFunc()
    filterInvoice = filterInvoiceFunc(inputNota)

    if not filterInvoice:
        dataNotFound()
    else:
        invIndex = -1
        for data in filterInvoice:
            invIndex = invoiceList.index(data)
            printInvFunc(data)

        while(True):
            inputConfirmation = input("Tekan Y jika ingin lanjut ubah data atau N jika ingin membatalkan perubahan data (Y/N) : ")
            if (inputConfirmation == 'Y' or inputConfirmation == 'y'):
                inputEditTarget = input("Masukkan Kolom yang Ingin Diubah : ").upper()
                isKeyExist = any(inputEditTarget in data for data in invoiceList)
                
                if (isKeyExist):
                    inputNewValue = input("Masukkan {} Baru : ".format(inputEditTarget.upper()))

                    while(True):
                        inputConfirmUpdate = input("Apakah Data Akan Diubah? (Y/N) : ")
                        if (inputConfirmUpdate == 'Y' or inputConfirmUpdate == 'y'):
                            invoiceList[invIndex][inputEditTarget] = inputNewValue
                            print("Data Terubah")
                            break
                        elif (inputConfirmUpdate == 'N' or inputConfirmUpdate == 'n'):
                            print("Data Tidak Terubah")
                            break
                        else:
                            inputanSalah()

                else:
                    inputanSalah()

                break
            elif (inputConfirmation == 'N' or inputConfirmation == 'n'):
                break
            else:
                inputanSalah()
        
def deleteData():
    inputNota = inputNotaFunc()
    filterInvoice = filterInvoiceFunc(inputNota)

    if not filterInvoice:
        dataNotFound()
    else:
        invIndex = -1
        for data in filterInvoice:
            invIndex = invoiceList.index(data)
            printInvFunc(data)
            
        while(True):
            inputConfirmation = input("Apakah Data Akan Dihapus? (Y/N) : ")
            if (inputConfirmation == 'Y' or inputConfirmation == 'y'):
                del invoiceList[invIndex]
                print("Data Terhapus")
                break
            elif (inputConfirmation == 'N'or inputConfirmation == 'n'):
                print("Data Tidak Terhapus")
                break
            else:
                inputanSalah()

def filterInvoiceFunc(inputNota):
    return list(filter(lambda n: n.get('NOMOR NOTA') == inputNota, invoiceList))

def inputNotaFunc():
    return input("Masukkan Nomor Nota : ").upper()

def printInvFunc(data):
    return print(*[str(k) + ' : ' + str(v) for k,v in data.items()], sep=", ")

def printEnumerateInv(listOfDict):
    for num, data in enumerate(listOfDict):
        print("{}".format(num+1), end=". ")
        printInvFunc(data)

mainMenu()
