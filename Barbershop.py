import PySimpleGUI as sg
import psycopg2
import re

def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="barbershop",
        user="postgres",
        password="Quockhanh2004@"
    )
    return conn

def list_barbers():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from barber join barber_working_time on barber.id = barber_working_time.barber_id")
    barbers = cur.fetchall()
    conn.close()
    return barbers

headers = ['Barber ID', 'Barber Name', 'Email', 'Phone Number', 'Working Time']
data = []
barbers = list_barbers()
for row in barbers:
    data.append([row[0], row[1], row[2], row[3], row[5]])

def list_services():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM service")
    service = cur.fetchall()
    conn.close()
    return service

headers1 = ["Service ID", "Service Name", "Price(EUR)"]
data1 = []
service = list_services()
for row in service:
    data1.append([row[0], row[1], row[2]])


list_barber_layout = [
    [sg.Table(
        values=data,
        headings=headers,
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        key='-TABLE-'
    )]

]

list_service_layout = [
    [sg.Table(
        values=data1,
        headings=headers1,
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        key='-TABLE1-'
    )]
]

make_an_appointment_layout = [
    [sg.Text("Enter ID number of the barber you want to book")],
    [sg.Input(key="BARBER ID")],
    [sg.Text("Enter ID number of the service you want to book")],
    [sg.Input(key="SERVICE ID")],
    [sg.Text("Enter the date of your appointment")],
    [sg.Input(key="APPOINTMENT DATE")],
    [sg.Text("Enter the time of your appointment(Morning/ Afternoon/ Evening)")],
    [sg.Input(key="APPOINTMENT TIME")],
    [sg.Button("Book")],
    [sg.Text("", key = '-RESULT2-', size=(80,1), text_color="red")],

]

edit_your_appointment_layout = [
    [sg.Text("Enter your appointment ID")],
    [sg.Input(key='-APPOINTEMENT ID-')],   
    [sg.Text("Enter ID number of the barber you want to book")],
    [sg.Input(key="BARBER ID 2")],
    [sg.Text("Enter ID number of the service you want to book")],
    [sg.Input(key="SERVICE ID 2")],
    [sg.Text("Enter the date of your appointment")],
    [sg.Input(key="APPOINTMENT DATE 2")],
    [sg.Text("Enter the time of your appointment(Morning/ Afternoon/ Evening)")],
    [sg.Input(key="APPOINTMENT TIME 2")],
    [sg.Button("Confirm")],
    [sg.Text("", key = '-RESULT3-', size=(80,1), text_color="red")],

]

cancel_your_appointment_layout = [
    [sg.Text("Enter your appointment ID")],
    [sg.Input(key='-APPOINTEMENT ID 2-')], 
    [sg.Button("Cancel")],
    [sg.Text("", key = '-RESULT4-', size=(60,1), text_color="red")],
]

def list_appointment():
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"Select id from customer where email = '{email}'")
    customer_id = cur.fetchone()[0]
    cur.execute("CREATE INDEX cust_name ON customer(customer.name)")
    cur.execute(f'select customer.name, appointment.id, barber.name, appointmentdate, appointmenttime, service.name, service.price from appointment join service on appointment.service_id = service.id join customer on appointment.customer_id = customer.id join barber on appointment.barber_id = barber.id where customer.id={customer_id}')
    app_list = cur.fetchall()
    if app_list is not None:
        conn.close()
        return app_list
    
headers2 = ['Customer Name', 'Appointment ID', 'Barber Name', 'Appointment Date', 'Appointment Time', 'Service', 'Price']
data2 = []

list_your_appointment_layout = [
    [sg.Text('Please enter your customer ID')],
        [sg.InputText(key = "-CUS ID-")],
        [sg.Button("Search")],
    [sg.Table(
        values=data2,
        headings=headers2,
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        key='-TABLE2-'
    )],
    [sg.Text("", key = '-RESULT5-', size=(60,1), text_color="red")]
]

def login_layout():
    layout = [
        [sg.Text('Please enter your email to continue')],
        [sg.InputText(key = "-PASSWORD-")],
        [sg.Button("Login"), sg.Button("New customer")],
        [sg.Text("", key = '-RESULT-', size=(60,1), text_color="red")]
    ]
    return layout

def create_password_layout():
    layout = [
        [sg.Text('Become a new customer')],
        [sg.Text('Enter your name')],
        [sg.InputText(key='-NEW NAME-')],
        [sg.Text('Enter your phone number')],
        [sg.InputText(key='-NEW PHONE NUM-')],
        [sg.Text('Enter your email')],
        [sg.InputText(key='-NEW EMAIL-')],
        [sg.Text("", key = '-RESULT1-', size=(60,1), text_color="red")],
        [sg.Button('Create')]
    ]
    return layout


def main_layout():
    layout = [
    [sg.Text("Welcome to the Grooming shop")],
    [sg.Button("List barber"), sg.Button("List service"), sg.Button("Make an appointment"), sg.Button("Edit your appointment"), sg.Button("Cancel your appointment"), sg.Button("List your appointment")],
    [
    sg.Column(list_barber_layout, visible=False, key='-COL2-'),
    sg.Column(list_service_layout, visible=False, key='-COL3-'),
    sg.Column(make_an_appointment_layout, visible=False, key='-COL4-'),
    sg.Column(edit_your_appointment_layout, visible=False, key='-COL5-'),
    sg.Column(cancel_your_appointment_layout , visible=False, key='-COL6-'),
    sg.Column(list_your_appointment_layout , visible=False, key='-COL7-')]
]
    return layout



login_window = sg.Window("Login", login_layout())
while True:
    event, values = login_window.read()
    if event == sg.WIN_CLOSED:
            break
    elif event == "New customer":
        login_window.close()
        new_p_window = sg.Window("Become a customer of us", create_password_layout())
        while True: 
            event, values = new_p_window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Create":
                conn = connect()
                cur = conn.cursor()
                name = values["-NEW NAME-"]
                email = values["-NEW EMAIL-"]
                phone_number = values["-NEW PHONE NUM-"]
                cur.execute(f"SELECT * FROM customer where email ='{email}'")
                customers = cur.fetchone()
                if '@' not in email or '.' not in email:
                    new_p_window['-RESULT1-'].update('Enter your email in correct format')
                elif customers is not None:
                    new_p_window['-RESULT1-'].update('Your gmail already exists in the system.')
                else:
                    cur.execute(
                        "INSERT INTO customer (name, email, phone_number) VALUES (%s, %s, %s) RETURNING id",(name, email, phone_number))
                    conn.commit()
                    customer_id = cur.fetchone()[0]
                    new_p_window['-RESULT1-'].update("Account created successfully! PLease exit the app and log in again")

    elif event == 'Login':
        email = values["-PASSWORD-"]
        if '@' not in email or '.' not in email:
            login_window['-RESULT-'].update('Enter your email in correct format')
        else:
            conn = connect()
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM customer where email ='{email}'")
            customers = cur.fetchone()
            if customers is None:
                login_window['-RESULT-'].update('Your data doesn\'t exit. Please try again or create a new account')
            elif customers is not None: 
                customer_id, name, email, phone_number = customers
                login_window.close()
                window = sg.Window(f"Hi {name} (Your ID: {customer_id}), wellcome to the barber shop", main_layout())
                
                temp = 2
                while True:
                    event, values = window.read()
                    print(event, values)
                    if event == sg.WIN_CLOSED:
                        break
                    elif event == "List barber":
                        window[f'-COL{temp}-'].update(visible = False)
                        window['-COL2-'].update(visible=True)
                        conn = connect()
                        cur = conn.cursor()
                        cur.execute("select * from barber join barber_working_time on barber.id = barber_working_time.barber_id")
                        barbers = cur.fetchall()
                        barbers = list_barbers()
                        text = []
                        for row in barbers:
                            text.append([row[0], row[1], row[2], row[3], row[5]])
                            window['-TABLE-'].update(values=text)
                        temp = 2

                    elif event == "List service":
                        window[f'-COL{temp}-'].update(visible = False)
                        window["-COL3-"].update(visible= True)
                        conn = connect()
                        cur = conn.cursor()
                        cur.execute("SELECT * FROM service")
                        service = cur.fetchall()

                        service = list_services()
                        data1=[]
                        for row in service:
                            data1.append([row[0], row[1], row[2]])
                            window['-TABLE1-'].update(values=data1)
                        temp = 3

                    elif event == "Make an appointment":
                        window[f'-COL{temp}-'].update(visible = False)
                        window["-COL4-"].update(visible= True)
                        conn = connect()
                        cur = conn.cursor()
                        cur.execute(f"Select id from customer where email = '{email}'")
                        customer_id = cur.fetchone()[0]    
                        temp = 4
                    elif event == "Book":
                        barber = values["BARBER ID"]
                        service = values["SERVICE ID"]
                        appointmentDate = values["APPOINTMENT DATE"]
                        appointmentTime = values["APPOINTMENT TIME"]
                        cur.execute(f"select * from appointment where barber_id= {barber} and appointmentdate='{appointmentDate}' and appointmenttime='{appointmentTime}'")
                        ketqua = cur.fetchone()
                        window['-RESULT2-'].update(visible= False)
                        if ketqua is not None:
                            window['-RESULT2-'].update(visible= True)
                            window['-RESULT2-'].update('The barber you book is not available at that time, please try again!')
                        else:
                            window['-RESULT2-'].update(visible= False)
                            cur.execute(f"INSERT INTO appointment(customer_id, barber_id, service_id, appointmentdate, appointmenttime) VALUES ({customer_id},{barber},{service}, '{appointmentDate}','{appointmentTime}')")
                            conn.commit()
                            window['-RESULT2-'].update(visible= True)
                            window['-RESULT2-'].update("Your appointment has been booked!")

                    elif event == "Edit your appointment":
                        window[f'-COL{temp}-'].update(visible = False)
                        window["-COL5-"].update(visible= True)
                        conn = connect()
                        cur = conn.cursor()
                        temp = 5
                    elif event  == "Confirm":
                        app_id = values['-APPOINTEMENT ID-']
                        cur.execute(f"select customer.name, appointment.id, barber.name, appointmentdate, appointmenttime, service.name, service.price from appointment join service on appointment.service_id = service.id join customer on appointment.customer_id = customer.id join barber on appointment.barber_id = barber.id where appointment.id={app_id}")
                        app_list = cur.fetchall()
                        cur.execute(f"select * from appointment where id = {app_id} ")
                        check = cur.fetchone()
                        if check is None:
                            window['-RESULT3-'].update(visible= True)
                            window['-RESULT3-'].update("This is not a valid appointment ID, try again!")
                        else:
                            cur.execute(f"Select id from customer where email = '{email}'")
                            customer_id = cur.fetchone()[0]
                            window['-RESULT3-'].update(visible= False)
                            barber2 = values["BARBER ID 2"]
                            service2 = values["SERVICE ID 2"]
                            appointmentDate2 = values["APPOINTMENT DATE 2"]
                            appointmentTime2 = values["APPOINTMENT TIME 2"]
                            cur.execute(f"select * from appointment where barber_id= {barber2} and appointmentdate='{appointmentDate2}' and appointmenttime='{appointmentTime2}'")
                            ketqua2 = cur.fetchone() 
                            if ketqua2 is not None:
                                window['-RESULT3-'].update(visible= True)
                                window['-RESULT3-'].update('The barber you book is not available at that time, please try again!')
                            else:
                                window['-RESULT3-'].update(visible= False)
                                cur.execute(f"Update appointment set barber_id = {barber2}, service_id = {service2}, appointmentdate ='{appointmentDate2}', appointmenttime ='{appointmentTime2}' where appointment.id={app_id}")
                                conn.commit()
                                window['-RESULT3-'].update(visible= True)
                                window['-RESULT3-'].update('Your appointment has been updated!')

                    elif event == "Cancel your appointment":
                        window[f'-COL{temp}-'].update(visible = False)
                        window["-COL6-"].update(visible= True)
                        temp = 6
                    elif event == "Cancel":
                        window['-RESULT4-'].update(visible= False)
                        app_id2 = values['-APPOINTEMENT ID 2-']
                        conn = connect()
                        cur = conn.cursor()
                        cur.execute(f'Select * from appointment where appointment.id = {app_id2}')
                        exist_app = cur.fetchone()
                        temp = 6
                        if exist_app is None:
                            window['-RESULT4-'].update(visible= True)
                            window['-RESULT4-'].update("The appointment ID you provided does not exist! Please try again!")
                        else:
                            window['-RESULT4-'].update(visible= False)
                            cur.execute(f'Delete from appointment where appointment.id = {app_id2}')
                            conn.commit()
                            conn.close()
                            window['-RESULT4-'].update(visible= True)
                            window['-RESULT4-'].update("Your appointment has been cancelled!")

                    elif event == "List your appointment":
                        window[f'-COL{temp}-'].update(visible = False)
                        window["-COL7-"].update(visible= True)
                        conn = connect()
                        cur = conn.cursor()
                        temp = 7
                    elif event == "Search":
                        cus_id = values["-CUS ID-"]
                        cur.execute(f'select customer.name, appointment.id, barber.name, appointmentdate, appointmenttime, service.name, service.price from appointment join service on appointment.service_id = service.id join customer on appointment.customer_id = customer.id join barber on appointment.barber_id = barber.id where customer.id={cus_id}')
                        app_list = cur.fetchall()
                        cur.execute(f'select customer_id from appointment where customer_id = {cus_id}')
                        check = cur.fetchone()
                        data2 = []
                        window['-RESULT5-'].update(visible= False)
                        if check is None:
                            window['-TABLE2-'].update(visible= False)
                            window['-RESULT5-'].update(visible= True)
                            window['-RESULT5-'].update("You have no appointment yet!")
                        else:
                            window['-RESULT5-'].update(visible= False)
                            window['-TABLE2-'].update(visible= True)
                            for row in app_list:
                                data2.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
                                window['-TABLE2-'].update(values=data2)
                window.close()