print ("Program OOP ")

class RekeningBank :

  def __init__(self,tabungan):
    self.tabungan = tabungan

  def CekSaldo(self):
    print(f"sisa saldo anda {self.tabungan}")

  def Menabung(self):
    tambah_tabungan = int(input("Masukan Jumlah yang ingin ditabungkan : "))
    tambah_tabungan += self.tabungan

  def Menarik(self):
    kurang_tabungan = int(input("Jumlah tunai yang akan ditarik : "))
    if self.tabungan < kurang_tabungan  :
      print(f"Saldo tersisa Rp.{self.tabungan}.Penarikan tunai tidak dapat dilakukan.")

    else :
      self.tabungan -= kurang_tabungan


rekeningsaya = RekeningBank()
rekeningsaya.CekSaldo()
rekeningsaya.Menabung()
rekeningsaya.Menarik()

      
      
  
