km = 10
phut = 42
giay = 42
tong_giay = phut * 60 + giay
tong_mile = km / 1.61
pace_giay = tong_giay / tong_mile
pace_phut = pace_giay //60
pace_giay_phut = pace_giay - pace_phut * 60
gio = tong_giay / 3600
toc_do = tong_mile / gio
print("toc do la: ", f"{toc_do: .2f}")
print("pace la : ", pace_phut, "phut", f"{pace_giay_phut: .2f}", "giay")
