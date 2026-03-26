# Remote SSH dari AWS EC2 Server

1. unduh dan Install Putty di https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

![alt text](image1b.png)

2. Konversi ekstensi Private Key dari .pem menjadi .ppk - Buka Putty Gen - Load Private Key .pem - Klik Save Private Key menjadi ekstensi File .ppk
   ![alt text](image-9.png)

3. Setting-Up Remote SSH dengan Putty
   - isi Ipv4 addres Public data berasal dari instance masing2
   - port SSH (22)
   - load private key .ppk di menu Connection->SSH->Auth->Credential
   - user dari instance masing-masing (ubuntu)

![alt text](image-10.png)

4. Setiap awal Remote kita lakukan Patching OS

- sudo apt-get update && sudo apt-get upgrade

5. coba lakukan instalasi Web Server
   dalam keadaan Kosong
   ![alt text](image-11.png)
   instal salah satu web server
   sudo apt install nginx
   ![alt text](image-12.png)
