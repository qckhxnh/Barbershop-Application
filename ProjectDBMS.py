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

def log_in(): 
    email = input('Enter your email: ')
    while not re.search('.+@.+\..+', email):
        email = input('Enter your email in correct format: ')
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM customer where email ='{email}'")
    customers = cur.fetchone()
    if customers is not None: 
        customer_id, name, email, phone_number = customers
        print(f"Logged in successfully as {name}")
    else:
        print('Your login information is not found, please create a new account!')
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        cur.execute(
            "INSERT INTO customer (name, email, phone_number) VALUES (%s, %s, %s) RETURNING id",(name, email, phone_number))
        conn.commit()
        customer_id = cur.fetchone()[0]
        print("Account created successfully!")
        cur.execute("SELECT name, email, phone_number FROM customer WHERE id = %s",(customer_id,))
        name, email, phone_number = cur.fetchone()
    conn.close()
    return customer_id, name, email, phone_number

def list_barbers():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from barber join barber_working_time on barber.id = barber_working_time.barber_id")
    barbers = cur.fetchall()
    for row in barbers:
        print(f"Barber ID: {row[0]}; Barber Name:{row[1]}; Email:{row[2]}; Phone Number:{row[3]}; Working Time: {row[5]}")
    conn.close()

def list_services():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM service")
    barbers = cur.fetchall()
    for row in barbers:
        print(f"Service ID: {row[0]}; Service Name: {row[1]}; Price(Eur): {row[2]}")
    conn.close()

def set_appointment(customer_id):
    barber = int(input('Enter ID number of the barber you want to book: '))
    service = int(input('Enter ID number of the service you want to book: '))
    appointmentDate = input('Enter the date of your appointment: ')
    appointmentTime = input('Enter the time of your appointment(Morning/Afternoon/Evening): ')
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"select * from appointment where barber_id= {barber} and appointmentdate='{appointmentDate}' and appointmenttime='{appointmentTime}'")
    exist_app = cur.fetchone()
    while exist_app:
        print('The barber you book is not available at that time, please try again!')
        barber = int(input('Enter ID number of the barber you want to book: '))
        service = int(input('Enter ID number of the service you want to book: '))
        appointmentDate = input('Enter the date of your appointment: ')
        appointmentTime = input('Enter the time of your appointment(Morning/Afternoon/Evening): ')
        conn = connect()
        cur = conn.cursor()
        cur.execute(f"select * from appointment where barber_id= {barber} and appointmentdate='{appointmentDate}' and appointmenttime='{appointmentTime}'")
        exist_app = cur.fetchone()    
    else: 
        cur.execute(f"INSERT INTO appointment(customer_id, barber_id, service_id, appointmentdate, appointmenttime) VALUES ({customer_id},{barber},{service}, '{appointmentDate}','{appointmentTime}')")
        conn.commit()
        print("Your appointment has been booked!")

def cancel_appointment():
    appointment = int(input('Enter your appointment id: '))
    conn = connect()
    cur = conn.cursor()
    cur.execute(f'Select * from appointment where appointment.id = {appointment}')
    exist_app = cur.fetchone()
    while exist_app is None: 
        print('The appointment ID you provided does not exist! Please try again.')
        appointment = int(input('Enter your appointment id: '))
        conn = connect()
        cur = conn.cursor()
        cur.execute(f'Select * from appointment where appointment.id = {appointment}')
        exist_app = cur.fetchone()
    else: 
        cur.execute(f'Delete from appointment where appointment.id = {appointment}')
        conn.commit()
        conn.close()
        print('Your appointment has been cancelled!')

def list_appointment(customer_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f'select customer.name, appointment.id, barber.name, appointmentdate, appointmenttime, service.name, service.price from appointment join service on appointment.service_id = service.id join customer on appointment.customer_id = customer.id join barber on appointment.barber_id = barber.id where customer.id={customer_id}')
    app_list = cur.fetchall()
    if app_list is None:
        print('You have no appointment yet!')
    else:
        for row in app_list:
            print(f"Customer Name: {row[0]}; Appointment ID: {row[1]}; Barber Name: {row[2]}; Appointment Date: {row[3]}; Appointment Time: {row[4]}; Service: {row[5]}; Price: {row[6]}")

def update_appointment(customer_id):
    conn = connect()
    cur = conn.cursor()
    app_id = int(input("Enter the ID of the appointment you want to update: "))
    cur.execute(f"select customer.name, appointment.id, barber.name, appointmentdate, appointmenttime, service.name, service.price from appointment join service on appointment.service_id = service.id join customer on appointment.customer_id = customer.id join barber on appointment.barber_id = barber.id where appointment.id={app_id}")
    app_list = cur.fetchall()
    while app_list is None:
        print("This is not a valid appointment ID, try again!")
        app_id = int(input("Enter the ID of the appointment you want to update: "))
        cur.execute(cur.execute(f'select customer.name, appointment.id, barber.name, appointmentdate, appointmenttime, service.name, service.price from appointment join service on appointment.service_id = service.id join customer on appointment.customer_id = customer.id join barber on appointment.barber_id = barber.id where appointment.id={app_id}'))
        app_list = cur.fetchall()
    else:
        for row in app_list:
            app_id = row[1]
            print("This your appointment information:")
            print(f"Customer Name: {row[0]}; Appointment ID: {row[1]}; Barber Name: {row[2]}; Appointment Date: {row[3]}; Appointment Time: {row[4]}; Service: {row[5]}; Price: {row[6]}")
            print("Please re-enter the information of this appointment!")
            barber = int(input('Enter ID number of the barber you want to book: '))
            service = (input('Enter ID number of the service you want to book: '))
            appointmentDate = input('Enter the date of your appointment: ')
            appointmentTime = input('Enter the time of your appointment(Morning/Afternoon/Evening): ')
            cur.execute(f"select * from appointment where barber_id={barber} and appointmentdate='{appointmentDate}' and appointmenttime='{appointmentTime}'")
            exist_app = cur.fetchone()
            while exist_app:
                print('The barber you book is not available at that time, please try again!')
                barber = int(input('Enter ID number of the barber you want to book: '))
                service = int(input('Enter ID number of the service you want to book: '))
                appointmentDate = input('Enter the date of your appointment: ')
                appointmentTime = input('Enter the time of your appointment(Morning/Afternoon/Evening): ')
                conn = connect()
                cur = conn.cursor()
                cur.execute(f"select * from appointment where barber_id=1 and appointmentdate='{appointmentDate}' and appointmenttime='{appointmentTime}'")
                exist_app = cur.fetchone()
            else:
                cur.execute(f"Update appointment set barber_id = {barber}, service_id = {service}, appointmentdate ='{appointmentDate}', appointmenttime ='{appointmentTime}' where appointment.id={app_id}")
                conn.commit()
                print("Your appointment has been updated!")

#Main  
customer_id, name, email, phone_number = log_in()
command = int(input(f'Available actions:\n1. Barbers list\n2. Services list\n3. Book_appointment\n4. Cancel your appointment\n5. List your appointment(s)\n6. Update your appointment\nChoose your action: '))
if command == 1:
    list_barbers()
elif command == 2:
    list_services()
elif command == 3:
    set_appointment(customer_id)
elif command == 4:
    cancel_appointment()
elif command == 5:
    list_appointment(customer_id)
elif command == 6:
    update_appointment(customer_id)
conti = (input('Do you want to continue?(Y/N)')).upper()
while conti == 'Y':
    command = int(input(f'Available actions:\n1. Barbers list\n2. Services list\n3. Book_appointment\n4. Cancel your appointment\n5. List your appointment(s)\n6. Update your appointment\nChoose your action: '))
    if command == 1:
        list_barbers()
    elif command == 2:
        list_services()
    elif command == 3:
        set_appointment(customer_id)
    elif command == 4:
        cancel_appointment()
    elif command == 5:
        list_appointment(customer_id)
    elif command == 6:
        update_appointment(customer_id)
    conti = (input('Do you want to continue?(Y/N)')).upper()
else: 
    print("Goodbye!")
    
    