import pandas as pd
import datetime
import win10toast

bday = False

if __name__ == "__main__":
    notifier = win10toast.ToastNotifier()
    dates = pd.read_excel("bdaydates.xlsx")
    # print (dates)
    today = datetime.datetime.now().strftime("%d-%m")
    # print (now)
    for index, item in dates.iterrows():
        bDate = item['Date'].strftime("%d-%m")
        # print(bDate)

        if (today==bDate):
            notifier.show_toast('Python', item['Name'], duration = 10)
            bday = True

    if bday==False:
        notifier.show_toast('Python', "No Birthday Today", duration = 10)
                