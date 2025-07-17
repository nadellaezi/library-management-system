from Models.AboutDAO import AboutDAO

class AboutManager:
    def __init__(self):
        # Membuat instance dari AboutDAO untuk digunakan oleh method lain di kelas ini
        self.about_dao = AboutDAO()

    def get_about_information(self):
        try:
            # Memanggil method dari objek DAO untuk mendapatkan data
            about_data = self.about_dao.get_information()
            return about_data
        except Exception as e:
            # Penanganan error
            print(f"Error di AboutManager saat mengambil informasi: {e}")
            return None