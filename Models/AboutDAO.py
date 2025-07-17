from .DAO import DAO
class AboutDAO(DAO):
    def __init__(self):
        # 1. Memanggil constructor dari kelas induk (DAO).
        # Langkah ini sangat penting untuk menginisialisasi koneksi database
        # yang kemungkinan besar di-handle oleh kelas DAO.
        super().__init__()

        # 2. Menetapkan nama tabel spesifik untuk kelas ini.
        # Atribut ini mendefinisikan tabel mana yang akan diakses oleh AboutDAO.
        # Nama tabel 'users' sepertinya kurang cocok untuk 'About',
        # jadi saya ganti dengan 'app_info' sebagai contoh yang lebih relevan.
        self.table = "app_info"

    def get_information(self):
        try:
            # Menjalankan query untuk mengambil semua data dari tabel.
            # 'self.query' adalah method yang kemungkinan diwarisi dari kelas induk DAO
            # untuk menjalankan perintah SQL dengan aman.
            # Menggunakan LIMIT 1 jika Anda hanya butuh satu baris informasi aplikasi.
            query_string = f"SELECT * FROM {self.table} LIMIT 1"

            # 'self.fetch_one' juga diasumsikan berasal dari parent DAO
            result = self.fetch_one(query_string)
            return result
        except Exception as e:
            # Penanganan error jika query gagal
            print(f"Terjadi error saat mengambil data 'about': {e}")
            return None