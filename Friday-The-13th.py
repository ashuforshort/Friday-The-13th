import time
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
        ##### Display banner #####
        print("\n\x1b[0;31m#################################\x1b[0m")
        print("\x1b[0;31m#\t\t\t\t#\x1b[0m")
        print("\x1b[0;31m#\tFRIDAY - THE - 13TH\t#\x1b[0m")
        print("\x1b[0;31m#\t\t\t\t#\x1b[0m")
        print("\x1b[0;31m#################################\x1b[0m")

        date_today = int((datetime.now()).strftime("%d"))
        weekday_int = int((datetime.now()).strftime("%w"))

        friday_flag_boolean = False
        last_fridays_array = []
        next_fridays_array = []

        ##### Print Today's date and message #####
        if ( date_today == 13 ):
                if ( weekday_int == 5 ):
                        print("\nIt's \x1b[0;31m"+(datetime.now()).strftime("%a %d %b %Y")+"\x1b[0m today. OMG! Another \x1b[0;31mFriday-The-13th\x1b[0m.")
                        friday_flag = True
                else:
                        print("\nIt's \x1b[0;32m"+(datetime.now()).strftime("%a %d %b %Y")+"\x1b[0m today. Thank God! It's not a Friday-The-13th. Phew!")
        else:
                print("\nIt's \x1b[0;32m"+(datetime.now()).strftime("%a %d %b %Y")+"\x1b[0m today. Thank God! It's not a Friday-The-13th. Phew!")

        print("\nTake a look at these previous and upcoming Friday-The-13ths:\n")

        ##### Previous Friday-The-13ths #####
        if ( friday_flag_boolean ):
                month_str = (datetime.now() - timedelta(month=1)).strftime("%b")
                month_int = int((datetime.now() - timedelta(month=1)).strftime("%m"))
                year = int((datetime.now() - timedelta(month=1)).strftime("%Y"))
        else:
                if ( date_today < 13 ):
                        month_str = (datetime.now() - timedelta(month=1)).strftime("%b")
                        month_int = int((datetime.now() - timedelta(month=1)).strftime("%m"))
                        year = int((datetime.now() - timedelta(month=1)).strftime("%Y"))
                else:
                        month_str = (datetime.now()).strftime("%b")
                        month_int = int((datetime.now()).strftime("%m"))
                        year = int((datetime.now()).strftime("%Y"))

        i = 1

        while i <= 6 :
                weekday_int = int((date(year, month_int, 13)).strftime("%w"))
                if ( weekday_int == 5 ):
                        last_fridays_array.append("13-"+month_str+"-"+str(year))
                        i += 1

                match month_str:
                        case "Jan":
                                month_str = "Dec"
                                month_int = 12
                                year -= 1
                        case "Feb":
                                month_str = "Jan"
                                month_int = 1
                        case "Mar":
                                month_str = "Feb"
                                month_int = 2
                        case "Apr":
                                month_str = "Mar"
                                month_int = 3
                        case "May":
                                month_str = "Apr"
                                month_int = 4
                        case "Jun":
                                month_str = "May"
                                month_int = 5
                        case "Jul":
                                month_str = "Jun"
                                month_int = 6
                        case "Aug":
                                month_str = "Jul"
                                month_int = 7
                        case "Sep":
                                month_str = "Aug"
                                month_int = 8
                        case "Oct":
                                month_str = "Sep"
                                month_int = 9
                        case "Nov":
                                month_str = "Oct"
                                month_int = 10
                        case "Dec":
                                month_str = "Nov"
                                month_int = 11

        print("\t\t\x1b[0;31m"+last_fridays_array[5]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+last_fridays_array[4]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+last_fridays_array[3]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+last_fridays_array[2]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+last_fridays_array[1]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+last_fridays_array[0]+"\x1b[0m")

        ##### Print Today's date again #####
        if ( friday_flag_boolean ):
                print("\t---\t\x1b[0;31m"+datetime.now().strftime("%d-%b-%Y")+"\x1b[0m\t---")
        else:
                print("\t---\t\x1b[0;32m"+datetime.now().strftime("%d-%b-%Y")+"\x1b[0m\t---")

        ##### Upcoming Friday-The-13ths #####
        if ( friday_flag_boolean ):
                month_str = (datetime.now() + relativedelta(months=1)).strftime("%b")
                month_int = int((datetime.now() + relativedelta(months=1)).strftime("%m"))
                year = int((datetime.now() + relativedelta(months=1)).strftime("%Y"))
        else:
                if ( date_today < 13 ):
                        month_str = (datetime.now()).strftime("%b")
                        month_int = int((datetime.now()).strftime("%m"))
                        year = int((datetime.now()).strftime("%Y"))
                else:
                        month_str = (datetime.now() + relativedelta(months=1)).strftime("%b")
                        month_int = int((datetime.now() + relativedelta(months=1)).strftime("%m"))
                        year = int((datetime.now() + relativedelta(months=1)).strftime("%Y"))

        i = 1

        while i <= 6 :
                weekday_int = int((date(year, month_int, 13)).strftime("%w"))
                if ( weekday_int == 5 ):
                        next_fridays_array.append("13-"+month_str+"-"+str(year))
                        i += 1

                match month_str:
                        case "Jan":
                                month_str = "Feb"
                                month_int = 2
                        case "Feb":
                                month_str = "Mar"
                                month_int = 3
                        case "Mar":
                                month_str = "Apr"
                                month_int = 4
                        case "Apr":
                                month_str = "May"
                                month_int = 5
                        case "May":
                                month_str = "Jun"
                                month_int = 6
                        case "Jun":
                                month_str = "Jul"
                                month_int = 7
                        case "Jul":
                                month_str = "Aug"
                                month_int = 8
                        case "Aug":
                                month_str = "Sep"
                                month_int = 9
                        case "Sep":
                                month_str = "Oct"
                                month_int = 10
                        case "Oct":
                                month_str = "Nov"
                                month_int = 11
                        case "Nov":
                                month_str = "Dec"
                                month_int = 12
                        case "Dec":
                                month_str = "Jan"
                                month_int = 1
                                year += 1

        print("\t\t\x1b[0;31m"+next_fridays_array[0]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+next_fridays_array[1]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+next_fridays_array[2]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+next_fridays_array[3]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+next_fridays_array[4]+"\x1b[0m")
        print("\t\t\x1b[0;31m"+next_fridays_array[5]+"\x1b[0m\n")