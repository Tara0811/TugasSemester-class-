#jadi ini adalah program yang mampu mempermudah perhitungan harga serta diskon yang ada pada toko komputer
import os

class TokoSparePart:
    def __init__(self):
        self.barang = []
        self.total_harga = 0
        self.diskon = 0
        self.diskon_barang = {
            'prosesor + vga': {'diskon': 0, 'barang_gratis': 'ram'},  
            'motherboard + vga': {'diskon': 0, 'barang_gratis': 'ssd'},  
            'motherboard + vga + prosesor': {'diskon': 1, 'barang_gratis': 'power supply'},  
        }
        self.harga_barang = {
            'prosesor': 10000000,
            'vga': 8000000,
            'ram': 1000000,
            'motherboard': 5000000,
            'ssd': 800000,
            'power supply': 1000000
        }

    def tambah_barang(self, barang):
        """Menambah barang dan hitung harga"""
        if barang in self.harga_barang:
            self.barang.append(barang)
            self.total_harga += self.harga_barang[barang]
            print(f"{barang} ditambah ke keranjang, total harga: Rp {self.total_harga}")
        else:
            print("Barangnya Gak Ada")

    def cek_diskon(self):
        """Periksa kombinasi barang dan beri diskon atau hadiah"""
        kombinasi = set(self.barang)
        diskon_info_list = []  
        
        for kombi, diskon_info in self.diskon_barang.items():
            item_kombi = set(kombi.split(' + '))
            if item_kombi.issubset(kombinasi):

                if diskon_info['barang_gratis']:
                    diskon_info_list.append(f"Anda dapat {diskon_info['barang_gratis']} GRATIS karena beli {kombi}.")
                    self.barang.append(diskon_info['barang_gratis']) 
                if diskon_info['diskon']:
                    diskon_amount = self.harga_barang['power supply'] * diskon_info['diskon']
                    diskon_info_list.append(f"Diskon {diskon_info['diskon']*100}% untuk Power Supply. Diskon: Rp {diskon_amount}")
                    self.total_harga -= diskon_amount  

        return diskon_info_list  

    def tampilkan_total(self):
        """Tampilkan total belanja dan diskon"""
        diskon_info_list = self.cek_diskon()
        
        if diskon_info_list:
            print("\nDiskon/Hadiah:")
            for info in diskon_info_list:
                print(info)
        else:
            print("Gak ada diskon/hadiah")
        
        print("\nBarang yang Dibeli:")
        for barang in self.barang:
            print(f"- {barang}")
        print(f"Total: Rp {self.total_harga}")

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    toko = TokoSparePart()
    
    print("Selamat datang di Toko Spare Part Komputer")
    while True:
        print("\nDaftar Barang Tersedia: ")
        for barang in toko.harga_barang:
            print(f"- {barang} (Rp {toko.harga_barang[barang]})")
        
        barang_pilihan = input("\nMasukkan barang yang ignin dibeli (atau ketik 'selesai' untuk keluar): ")
        
        if barang_pilihan.lower() == 'selesai':
            break
        else:
            bersihkan_layar()  
            toko.tambah_barang(barang_pilihan)
    
    toko.tampilkan_total()

if __name__ == "__main__":
    main()
