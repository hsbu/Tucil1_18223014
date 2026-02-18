# LinkedIn Queens Solver

## Deskripsi Program
Program merupakan solver untuk permainan **LinkedIn Queens** menggunakan algoritma brute force. LinkedIn Queens adalah variasi dari N-Queens puzzle di mana queen harus ditempatkan pada papan berukuran n×n dengan aturan:
- Setiap baris dan kolom hanya boleh ditempati oleh 1 queen
- Setiap daerah warna hanya boleh ditempati oleh 1 queen

Program akan mencoba semua kombinasi penempatan queen secara sistematis hingga menemukan solusi yang valid atau sampai semua kemungkinan habis.

## Requirements
- **Python 3.x** (Python 3.6 atau lebih tinggi direkomendasikan)

## Instalasi
1. Pastikan Python 3 sudah terinstal di sistem Anda. Cek dengan menjalankan:
   ```bash
   python --version
   ```
   atau
   ```bash
   python3 --version
   ```

2. Clone repositori ini:
   ```bash
   git clone https://github.com/hsbu/Tucil1_18223014.git
   cd Tucil1_18223014
   ```

## Run Program

### Opsi 1: Run dengan script

#### Windows (PowerShell/Command Prompt)
```bash
cd src
python main.py
```

#### Linux/macOS
```bash
cd src
python3 main.py
```

### Opsi 2: Run dengan file executable

```bash
cd bin
.\main.exe
```

## Cara Menggunakan Program

1. Jalankan program dengan perintah di atas
2. Masukkan path file input permasalahan:
   ```
   Masukkan file permasalahan: input1.txt
   ```

3. Program akan mencari solusi dan menampilkan:
   - Solusi yang ditemukan (jika ada)
   - Jumlah kasus yang diperiksa
   - Waktu pencarian dalam milidetik

4. Jika solusi ditemukan, program akan menanyakan apakah Anda ingin menyimpan:
   ```
   Apakah Anda ingin menyimpan solusi? (Ya/Tidak):
   ```
   - Ketik `ya` untuk menyimpan, lalu masukkan nama file
   - Ketik `tidak` untuk keluar tanpa menyimpan

## Format File Input
File input harus berupa matriks karakter yang merepresentasikan warna pada setiap sel papan. Contoh untuk papan 4×4:
```
ABCD
EFGH
IJKL
MNOP
```

Setiap karakter mewakili warna yang berbeda. File input contoh tersedia di folder `src/`:
- `input1.txt`
- `input2.txt`
- `input3.txt`
- `input4.txt`
- `input5.txt`

## Struktur Folder
```
Tucil1_18223014/
├── bin/          # Folder untuk executable (jika ada)
├── doc/          # Dokumentasi
├── src/          # Source code
│   ├── main.py   # Program utama
│   ├── input1.txt - input5.txt  # File input contoh
├── test/         # File solusi untuk testing
│   ├── solution1.txt - solution5.txt
└── README.md     # File ini
```

## Author
**Nama**: Muhamad Hasbullah Faris </br>
**NIM**: 18223014  