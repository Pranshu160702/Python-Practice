import time
from win10toast import ToastNotifier

while(True):
    time.sleep(10)
    toast = ToastNotifier()
    toast.show_toast("Drink Your Water Hooman!", "Please Drink it Now!!!!", duration=2)