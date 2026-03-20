import time
current_time = time.time()
ngay = int(current_time // 86400)
giay_trong_ngay = current_time % 86400
gio = int(giay_trong_ngay //3600)
giay_trong_gio = giay_trong_ngay % 3600
phut = int(giay_trong_gio //60)
giay_con_lai = int(giay_trong_gio % 60)
print(f"Thời gian hiện tại: {gio:02d}:{phut:02d}:{giay_con_lai:05.2f}")
print(f"so ngay ke tu epoch: {ngay}")
