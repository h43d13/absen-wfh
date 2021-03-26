# Otomatisasi Absen dp-wfh/skemaraja
gunakan automatisasi web absen ini agar tidak lupa absen di jam yang ditentukan

*gunakan script ini pada crontab agar terabsen pagi siang dan sore
0 5,6,7,8,12,16,17 * * 1-5 export DISPLAY=:0 && /usr/bin/python3 /home/hadi/Documents/webdriver/absen.py >> /home/hadi/Desktop/test.log 2>&1
