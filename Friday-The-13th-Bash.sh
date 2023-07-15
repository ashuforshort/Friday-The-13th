#!/bin/bash

clear; 

##### Display banner #####
echo -e "\n\e[1;31m#################################\e[0m";
echo -e "\e[1;31m#\t\t\t\t#\e[0m";
echo -e "\e[1;31m#\e[0m\t\e[1;31mFRIDAY - THE - 13TH\e[0m\t\e[1;31m#\e[0m";
echo -e "\e[1;31m#\t\t\t\t#\e[0m";
echo -e "\e[1;31m#################################\e[0m";

date_today=$(date +%d);
weekday=$(date +%w);

friday_flag=0;
last_array=();
next_array=();

##### Print Today's date and message #####
if [[ $date_today -eq 13 ]]
then
        if [[ $weeday -eq 5 ]]
        then
                echo -e "\nIt's \e[1;31m`date \"+%a %d %b %Y\"`\e[0m today. Ohh God! Another \e[1;31mFriday-The-13th\e[0m.";
                friday_flag=1;
        else
                echo -e "\nIt's \e[1;32m`date \"+%a %d %b %Y\"`\e[0m today. Thank God! It's not a Friday-The-13th.";         
        fi
else
        echo -e "\nIt's \e[1;32m`date \"+%a %d %b %Y\"`\e[0m today. Thank God! It's not a Friday-The-13th.";
fi

echo -e "\nTake a look at these six last and next Friday-The-13ths.\n"

##### Last Friday-The-13ths #####
if [[ $friday_flag -eq 1 ]]
then
        month=$(date --date="last month" +%b);
        year=$(date --date="last month" +%Y);
else
        month=$(date +%b);
        year=$(date +%Y);
fi

i=1;

while [[ $i<=6 ]]
do
        weekday=$(date --date="13 $month $year" +%w);
        if [[ $weekday -eq 5 ]]
        then
                last_array+=(`date "+13-$month-$year"`);
                i=`expr $i + 1`;
        fi
        case $month in
                "Jan")  month="Dec";
                        year=`expr $year - 1`;
                        ;;
                "Feb")  month="Jan";
                        ;;
                "Mar")  month="Feb";
                        ;;
                "Apr")  month="Mar";
                        ;;
                "May")  month="Apr";
                        ;;
                "Jun")  month="May";
                        ;;
                "Jul")  month="Jun";
                        ;;
                "Aug")  month="Jul";
                        ;;
                "Sep")  month="Aug";
                        ;;
                "Oct")  month="Sep";
                        ;;
                "Nov")  month="Oct";
                        ;;
                "Dec")  month="Nov";
                        ;;
        esac
done

echo -e "\t   \e[1;31m${last_array[5]}\e[0m";
echo -e "\t   \e[1;31m${last_array[4]}\e[0m";
echo -e "\t   \e[1;31m${last_array[3]}\e[0m";
echo -e "\t   \e[1;31m${last_array[2]}\e[0m";
echo -e "\t   \e[1;31m${last_array[1]}\e[0m";
echo -e "\t   \e[1;31m${last_array[0]}\e[0m";

##### Print Today's date again #####
if [[ $friday_flag -eq 1 ]]
then
        echo -e "\t-- \e[1;31m`date +%d-%b-%Y`\e[0m --";
else
        echo -e "\t-- \e[1;32m`date +%d-%b-%Y`\e[0m --";
fi

##### Next Friday-The-13ths #####
if [[ $friday_flag -eq 1 ]]
then
        month=$(date --date="next month" +%b);
        year=$(date --date="next month" +%Y);
else
        month=$(date +%b);
        year=$(date +%Y);
fi

i=1;

while [[ $i<=6 ]]
do
        weekday=$(date --date="13 $month $year" +%w);
        if [[ $weekday -eq 5 ]]
        then
                next_array+=(`date "+13-$month-$year"`);
                i=`expr $i + 1`;
        fi
        case $month in
                "Jan")  month="Feb";
                        ;;
                "Feb")  month="Mar";
                        ;;
                "Mar")  month="Apr";
                        ;;
                "Apr")  month="May";
                        ;;
                "May")  month="Jun";
                        ;;
                "Jun")  month="Jul";
                        ;;
                "Jul")  month="Aug";
                        ;;
                "Aug")  month="Sep";
                        ;;
                "Sep")  month="Oct";
                        ;;
                "Oct")  month="Nov";
                        ;;
                "Nov")  month="Dec";
                        ;;
                "Dec")  month="Jan";
                        year=`expr $year + 1`;
                        ;;
        esac
done

echo -e "\t   \e[1;31m${next_array[0]}\e[0m";
echo -e "\t   \e[1;31m${next_array[1]}\e[0m";
echo -e "\t   \e[1;31m${next_array[2]}\e[0m";
echo -e "\t   \e[1;31m${next_array[3]}\e[0m";
echo -e "\t   \e[1;31m${next_array[4]}\e[0m";
echo -e "\t   \e[1;31m${next_array[5]}\e[0m\n";
