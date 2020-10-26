from src.chat import *
import csv


def read_csv(file):
    """reads in the data for abbott and costello"""
    conn = connect()
    cur = conn.cursor()
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if row[0] == 'Both':
                send_message('Abbott', 'N/A', row[1], '4', row[2], row[3])
                send_message('Costello', 'N/A', row[1], '5', row[2], row[3])
            elif row[0] == 'Abbott':
                send_message('Abbott', 'N/A', row[1], '4', row[2], row[3])
            else:
                send_message('Costello', 'N/A', row[1], '5', row[2], row[3])

    conn.commit()
    conn.close()


def load_user_csv(file):
    """loads in the user via csv"""
    conn = connect()
    cur = conn.cursor()
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if row[0] == 'OG-stoog':
                add_user(row[0], row[1], row[2])
                add_to_community('1', '1')
                add_to_community('1', '2')
            elif row[0] == 'Lar-mar78':
                add_user(row[0], row[1], row[2])
                add_to_community('2', '1')
                add_to_community('2', '2')
            elif row[0] == 'curls4gurls':
                add_user(row[0], row[1], row[2])
                add_to_community('3', '1')
                add_to_community('3', '2')
            elif row[0] == 'The-Ab-God':
                add_user(row[0], row[1], row[2])
                add_to_community('4', '3')
            else:
                add_user(row[0], row[1], row[2])
                add_to_community('5', '3')
    conn.commit()
    conn.close()


def load_messages(file):
    """loads in messages from larry curly and moe via csv """
    conn = connect()
    cur = conn.cursor()
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if row[0] == 'Larry':
                send_message(row[0], 'N/A', row[1], '2', row[2], row[3])
            elif row[0] == 'Curly':
                send_message(row[0], 'N/A', row[1], '3', row[2], row[3])
            elif row[0] == 'Moe':
                send_message(row[0], 'N/A', row[1], '1', row[2], row[3])

    conn.commit()
    conn.close()



