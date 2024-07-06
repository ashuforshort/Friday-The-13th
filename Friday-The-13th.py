import ssl
import streamlit as st
import urllib.request as url
from bs4 import BeautifulSoup
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

unverified_ssl_context = ssl._create_unverified_context()
f13_wikipedia_content = url.urlopen('https://en.wikipedia.org/wiki/Friday_the_13th',context=unverified_ssl_context)
soup = BeautifulSoup(f13_wikipedia_content,'html.parser')
all_p_tags = soup.find_all('p')
for i in all_p_tags:
        paragraph = i.get_text()
        if "until" in paragraph:
                paragraph = paragraph.replace("(refresh)","")
                break

st.set_page_config(
        page_title="Friday-The-13th",
        page_icon=":jack_o_lantern:",
        layout="wide",
        menu_items={
                'Get help': 'https://github.com/ashuforshort/Friday-The-13th',
                'Report a bug': 'https://github.com/ashuforshort/Friday-The-13th',
                'About': 'https://github.com/ashuforshort/Friday-The-13th'
        }
)

st.header(":jack_o_lantern: :red[Friday-The-13th]", divider='red')
st.sidebar.image("Friday-The-13th-Logo.jpg")
st.write(":open_book: \"Friday-The-13th\" is considered an unlucky day in Western superstition.")
st.write(":open_book: It occurs when the 13th day of the month in the Gregorian calendar falls on a Friday.")
st.write(":open_book: A month has a Friday-The-13th if and only if it begins on a Sunday.")
st.write(f":open_book: :red[{paragraph}]")
wiki_url = "https://en.wikipedia.org/wiki/Friday_the_13th"
st.write("*[Source: Wikipedia] [Friday the 13th](%s)*" % wiki_url)

sidebar_date_input = st.sidebar.date_input("Pick a date",format="DD-MM-YYYY",value="today")
sidebar_last_count = st.sidebar.slider("Count of Previous Friday-The-13ths",min_value=1,max_value=10)
sidebar_next_count = st.sidebar.slider("Count of Upcoming Friday-The-13ths",min_value=1,max_value=10)

st.divider()
st.write(":point_left: Pick a date from the sidebar and set the count of \"Previous\" and \"Upcoming\" Friday-The-13ths.")
st.write(":point_down: See the results here after you change the values.")
st.divider()

last_fridays_array = []
next_fridays_array = []

column_previous, column_current, column_upcoming = st.columns(3,gap="small",vertical_alignment="center")

with column_previous:
        column_previous.subheader("Last Friday-The-13ths")
        container_previous = st.container(border=True)
        if (((int(sidebar_date_input.strftime("%d")) == 13) and (int(sidebar_date_input.strftime("%w")) == 5)) or (int(sidebar_date_input.strftime("%d")) < 13)):
                previous_month_int = int((sidebar_date_input - relativedelta(months=1)).strftime("%m"))
                previous_year = int((sidebar_date_input - relativedelta(months=1)).strftime("%Y"))
        else:
                previous_month_int = int(sidebar_date_input.strftime("%m"))
                previous_year = int(sidebar_date_input.strftime("%Y"))

        p = 1

        while p <= sidebar_last_count:
                if ( int((date(previous_year, previous_month_int, 13)).strftime("%w")) == 5 ):
                        last_fridays_array.append("13-"+(date(previous_year, previous_month_int, 13)).strftime("%b")+"-"+str(previous_year))
                        p += 1

                match previous_month_int:
                        case 1:
                                previous_month_int = 12
                                previous_year -= 1
                        case 2:
                                previous_month_int = 1
                        case 3:
                                previous_month_int = 2
                        case 4:
                                previous_month_int = 3
                        case 5:
                                previous_month_int = 4
                        case 6:
                                previous_month_int = 5
                        case 7:
                                previous_month_int = 6
                        case 8:
                                previous_month_int = 7
                        case 9:
                                previous_month_int = 8
                        case 10:
                                previous_month_int = 9
                        case 11:
                                previous_month_int = 10
                        case 12:
                                previous_month_int = 11

        p = len(last_fridays_array) - 1

        while p >= 0 :
                container_previous.write(last_fridays_array[p])        
                p -= 1

with column_current:
        column_current.subheader("Date Selected")
        container_current = st.container(border=True)
        if ((int(sidebar_date_input.strftime("%d")) == 13) and (int(sidebar_date_input.strftime("%w")) == 5)):
                text = ''':red['''+sidebar_date_input.strftime("%d-%b-%Y")+''']'''
                container_current.markdown(text)
        else:
                text = ''':green['''+sidebar_date_input.strftime("%d-%b-%Y")+''']'''
                container_current.markdown(text)            

with column_upcoming:
        column_upcoming.subheader("Next Friday-The-13ths")
        container_upcoming = st.container(border=True)
        if (((int(sidebar_date_input.strftime("%d")) == 13) and (int(sidebar_date_input.strftime("%w")) == 5)) or (int(sidebar_date_input.strftime("%d")) > 13)):
                upcoming_month_int = int((sidebar_date_input + relativedelta(months=1)).strftime("%m"))
                upcoming_year = int((sidebar_date_input + relativedelta(months=1)).strftime("%Y"))
        else:
                upcoming_month_int = int(sidebar_date_input.strftime("%m"))
                upcoming_year = int(sidebar_date_input.strftime("%Y"))

        n = 1

        while n <= sidebar_next_count:
                selected_date_weekday_number = int((date(upcoming_year, upcoming_month_int, 13)).strftime("%w"))
                if ( selected_date_weekday_number == 5 ):
                        next_fridays_array.append("13-"+(date(upcoming_year, upcoming_month_int, 13)).strftime("%b")+"-"+str(upcoming_year))
                        n += 1

                match upcoming_month_int:
                        case 1:
                                upcoming_month_int = 2
                        case 2:
                                upcoming_month_int = 3
                        case 3:
                                upcoming_month_int = 4
                        case 4:
                                upcoming_month_int = 5
                        case 5:
                                upcoming_month_int = 6
                        case 6:
                                upcoming_month_int = 7
                        case 7:
                                upcoming_month_int = 8
                        case 8:
                                upcoming_month_int = 9
                        case 9:
                                upcoming_month_int = 10
                        case 10:
                                upcoming_month_int = 11
                        case 11:
                                upcoming_month_int = 12
                        case 12:
                                upcoming_month_int = 1
                                upcoming_year += 1

        n = 0

        while n < len(next_fridays_array) :
                container_upcoming.write(next_fridays_array[n])        
                n += 1