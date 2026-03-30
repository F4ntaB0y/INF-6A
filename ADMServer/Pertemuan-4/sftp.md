# Migrasi Data Lokal ke Cloud SFTP dan Manajemen Hak Akses Web

1. Unduh dan Install FileZilla di https://filezilla-project.org/
   ![alt text](image.png)
   ![alt text](image1.png)

2. Running Instance EC2 di AWS (instance -> start Instance)
   ![alt text](image2.png)

3. Buka FileZilla dan masukkan data berikut: - Host: [IP_ADDRESS] - Username: ubuntu - Password: [PASSWORD] - Port: 22 - Klik Connect
   ![alt text](image3.png)
   ![alt text](image4.png)

4. Remote SSH via PowerShell Windows
   - masuk folder penyimpanan private key
   - open with -> powershell
   - masukan command (ssh -i nama file-Private-Key.pem ubuntu@[IP_ADDRESS])
     ![alt text](image5.png)

5. DIrectori Folder Cloud arahakan ke Folder Web Services Area
   - Keluar dari directori /home/ubuntu
   - Masuk ke direktori /var/www/html
   - buka file index.html dengan code editor
   - akan gagal melakukan editing - Permission denied
   - karena kita masuk user ubuntu tidak punya akses untuk write

6. Ubah Hak Akses Folder Web Services Area
   - ke Terminal PowerShell
   - masukan command (sudo chown -R ubuntu:ubuntu /var/www/html)
   - cek kembali hak akses folder dengan command (ls -l /var/www/html)
     ![alt text](image6.png)

7. kita lakukan editing di file index.html setelah hak akses folder sudah diubah
   ![alt text](image7.png)
8. Pastikan Design Responsive
   ![alt text](image8.png)
