import datetime

def receive_money():
  name = input("ชื่อผู้ส่ง :")
  moneys = float(input("จำนวนเงิน:"))
  dat = datetime.datetime.now()
  with open("payments_log.txt", "a") as t:
        t.write(f"{dat} | {name} | ${moneys:.2f}\n")
  print(f"received ${moneys:.2f} from {name} on {dat.strftime("%d/%m/%Y %H:%M:%S")}")

