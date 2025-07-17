from flask import Flask
from flaskext.mysql import MySQL # 1. Impor library MySQL

# Impor blueprint yang sudah Anda buat
from routes.about import about_view
# Jika Anda punya blueprint lain, impor juga di sini
# from routes.books import books_view

# 2. Inisialisasi aplikasi Flask
app = Flask(__name__)

# 3. Konfigurasi koneksi ke database MySQL
#    Ganti nilainya sesuai dengan pengaturan XAMPP/MySQL Anda.
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root' # Biasanya 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' # Kosongkan jika tidak ada password
app.config['MYSQL_DATABASE_DB'] = 'lms_db' # Ganti dengan nama database Anda
app.config['SECRET_KEY'] = 'ini_kunci_rahasia_anda' # Diperlukan untuk session/flash message

# 4. Buat objek MySQL
mysql = MySQL()

# 5. Inisialisasi objek MySQL dengan aplikasi Flask Anda
#    INI ADALAH LANGKAH YANG KEMUNGKINAN BESAR TERLEWAT
mysql.init_app(app)

# 6. Daftarkan Blueprint Anda ke aplikasi utama
app.register_blueprint(about_view)
# app.register_blueprint(books_view)

# Running
if __name__ == "__main__":
    app.run(debug=True)