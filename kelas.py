#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import library
import pandas as pd


#membuat class utama
class mahasiswa():
    __nilai = 0
    __formatif = 0.4
    __uts = 0.3
    __uas = 0.3

    def nama(self):
        self.nama = input('Masukkan nama mahasiswa \t: ')
        # self.nim = input('Masukkan nim mahasiswa \t: ')
        return self.nama

    def nim(self):
        self.nim = input('Masukkan nim mahasiswa \t\t: ')
        return self.nim

    def formatif(self):
        self.__nilai_formatif = input('Masukkan nilai formatif \t: ')
        self.__nilai_formatif = int(self.__nilai_formatif)
        # self.__nilai += float(0.4 * self.nilai)
        return self.__nilai_formatif

    def uts(self):
        self.__nilai_uts = input('Masukkan nilai uts \t\t: ')
        self.__nilai_uts = int(self.__nilai_uts)
        # self.__nilai += float(0.3 * self.nilai)
        return self.__nilai_uts

    def uas(self):
        self.__nilai_uas = input('Masukkan nilai uas \t\t: ')
        self.__nilai_uas = int(self.__nilai_uas)
        # self.__nilai += float(0.3 * self.nilai)
        return self.__nilai_uas

    def akhir(self):
        self.__nilai = (0.4 * self.__nilai_formatif) + (0.3 * self.__nilai_uts) + (0.3 * self.__nilai_uas)
        return self.__nilai

    def huruf(self):
        if self.__nilai <= 50:
            self.huruf = 'E'
        elif self.__nilai <= 60:
            self.huruf = 'D'
        elif self.__nilai <= 70:
            self.huruf = 'C'
        elif self.__nilai <= 80:
            self.huruf = 'B'
        else:
            self.huruf = 'A'
        return self.huruf


class data(mahasiswa):

    def tabel(self):
        self.kolom = ['NIM', 'Nama', 'Formatif', 'UTS', 'UAS', 'Nilai Akhir', 'Huruf']
        self.df = pd.DataFrame(columns=self.kolom)
        self.df = self.df.fillna(0)
        return self.df

    def baris(self):
        self.__baris = input('Masukkan banyaknya data yang ingin dimasukkan : ')
        self.__baris = int(self.__baris)
        self.df = self.df
        for n in range(self.__baris):
            nama = super().nama()
            nim = super().nim()
            formatif = super().formatif()
            uts = super().uts()
            uas = super().uas()
            nilai = super().akhir()
            huruf = super().huruf()
            data_nilai = [nim, nama, formatif, uts, uas, nilai, huruf]
            df_len = len(self.df)
            self.df.loc[df_len] = data_nilai
        return nama, nim, formatif, uts, uas, nilai, huruf, data_nilai, df_len, self.df
    
    def cetak_tabel(self):
        return self.df
    
    def simpan(self):
        self.name = input('Tabel akan disimpan dalam file dengan nama \t: ')
        self.tabel = self.df.to_excel('{}.xlsx'.format(self.name), index=False)
        return self.tabel

