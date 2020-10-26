from src.swen344_db_utils import connect

"""
file: chat.py
author: Quincy Myles Jr. 
description: Database project
"""


def drop_tables():
    """drops all the tables if they already exist"""
    conn = connect()
    cur = conn.cursor()
    tables = """
        DROP TABLE IF EXISTS communities CASCADE; 
        DROP TABLE IF EXISTS channels CASCADE; 
        DROP TABLE IF EXISTS users CASCADE;
        DROP TABLE IF EXISTS moderators; 
        DROP TABLE IF EXISTS suspended_users; 
        DROP TABLE IF EXISTS messages; 
        DROP TABLE IF EXISTS communities_in; 
        DROP TABLE IF EXISTS channels_in; 
    """
    cur.execute(tables)
    conn.commit()
    conn.close()


def create_community_table():
    """creates table for the communities"""
    conn = connect()
    cur = conn.cursor()
    community = """
        CREATE TABLE communities(
            id SERIAL PRIMARY KEY, 
            comm_name VARCHAR(40) NOT NULL
        ); 
    """
    cur.execute(community)
    conn.commit()
    conn.close()


def create_channel_table():
    """creates the channel table"""
    conn = connect()
    cur = conn.cursor()
    channel = """
        CREATE TABLE channels(
            id SERIAL PRIMARY KEY, 
            chan_name VARCHAR(40) NOT NULL,
            comm_id INT, 
            FOREIGN KEY (comm_id) REFERENCES communities(id) ON DELETE CASCADE 
        ); 
    """
    cur.execute(channel)
    conn.commit()
    conn.close()


def create_user_table():
    """creates the table for the user info"""
    conn = connect()
    cur = conn.cursor()
    create_users = """
            CREATE TABLE users(
                user_id SERIAL PRIMARY KEY,
                display_name VARCHAR(40) NOT NULL,
                first_name VARCHAR(40) NOT NULL DEFAULT '',
                email VARCHAR(40) NOT NULL

            );  
        """
    cur.execute(create_users)
    conn.commit()
    conn.close()


def create_suspension_table():
    """creates the table with the suspended users"""
    conn = connect()
    cur = conn.cursor()
    create_suspension = """
          CREATE TABLE suspended_users(
              display_name VARCHAR(40) NOT NULL, 
              first_name VARCHAR(40) NOT NULL DEFAULT '',
              suspension_end_date VARCHAR(40) NOT NULL,
              user_id INT, 
              comm_id INT, 
              FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE, 
              FOREIGN KEY (comm_id) REFERENCES communities(id) ON DELETE CASCADE 
          );
      """
    cur.execute(create_suspension)
    conn.commit()
    conn.close()


def create_message_table():
    """creates the table with all the messages"""
    conn = connect()
    cur = conn.cursor()
    create_message = """
           CREATE TABLE messages( 
               first_name VARCHAR(40) NOT NULL, 
               message VARCHAR(8000) NOT NULL, 
               time_stamp VARCHAR(40) NOT NULL,
               user_id INT , 
               comm_id INT, 
               chan_id INT, 
               FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE, 
               FOREIGN KEY (comm_id) REFERENCES communities(id) ON DELETE CASCADE, 
               FOREIGN KEY (chan_id) REFERENCES channels(id) ON DELETE CASCADE 
           );
       """
    cur.execute(create_message)
    conn.commit()
    conn.close()


def create_mod_table():
    """creates the table of the moderators"""
    conn = connect()
    cur = conn.cursor()
    moderators = """
        CREATE TABLE moderators(
            first_name VARCHAR(40) NOT NULL, 
            user_id INT, 
            comm_id INT, 
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE, 
            FOREIGN KEY (comm_id) REFERENCES communities(id) ON DELETE CASCADE 
        ); 
    """
    cur.execute(moderators)
    conn.commit()
    conn.close()


def create_users_in_communities():
    """creates a table define what communties each user is apart of"""
    conn = connect()
    cur = conn.cursor()
    users_in = """
        CREATE TABLE communities_in(
            user_id INT, 
            comm_id INT,
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE, 
            FOREIGN KEY (comm_id) REFERENCES communities(id) ON DELETE CASCADE  
    ); 
    """
    cur.execute(users_in)
    conn.commit()
    conn.close()


def create_private_channel_users():
    """creates a table that defines users in a private channel"""
    conn = connect()
    cur = conn.cursor()
    private = """
        CREATE TABLE channels_in(
            user_id INT, 
            chan_id INT, 
            comm_id INT, 
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
            FOREIGN KEY(chan_id) REFERENCES channels(id) ON DELETE CASCADE,  
            FOREIGN KEY (comm_id) REFERENCES communities(id) ON DELETE CASCADE 
    );  
    """
    cur.execute(private)
    conn.commit()
    conn.close()


def add_community(comm_name):
    conn = connect()
    cur = conn.cursor()
    comm = """
        INSERT INTO communities(id, comm_name) VALUES 
            (DEFAULT, %s)
    """
    cur.execute(comm, (comm_name,))
    conn.commit()
    conn.close()


def add_to_community(user_id, comm_id):
    conn = connect()
    cur = conn.cursor()
    add = """
        INSERT INTO communities_in(user_id, comm_id)VALUES 
            (%s, %s)
    """
    cur.execute(add, (user_id, comm_id))
    conn.commit()
    conn.close()


def add_channel(chan_name, community):
    conn = connect()
    cur = conn.cursor()
    chan = """
        INSERT INTO channels(id, chan_name, comm_id) VALUES 
            (DEFAULT, %s, %s)
    """
    cur.execute(chan, (chan_name, community))
    conn.commit()
    conn.close()


def add_to_channel(user_id, chan_id, comm_id):
    conn = connect()
    cur = conn.cursor()
    add = """
        INSERT INTO channels_in(user_id, chan_id, comm_id)VALUES
            (%s, %s, %s)
    """
    cur.execute(add, (user_id, chan_id, comm_id))
    conn.commit()
    conn.close()


def add_user(display_name, first_name, email):
    """adds a new user to the chat system"""
    conn = connect()
    cur = conn.cursor()
    create_user = """
        INSERT INTO users ( user_id, display_name, first_name, email) VALUES
            (DEFAULT, %s, %s, %s)
            """
    user = (display_name, first_name, email)
    cur.execute(create_user, user)
    conn.commit()
    conn.close()


def update_user_info(user_id, display_name=None, first_name=None, email=None):
    """updated any info of the user"""
    conn = connect()
    cur = conn.cursor()
    info = (display_name, first_name, email, user_id)
    update_info = """
        UPDATE users SET
            display_name = COALESCE(%s, display_name),
            first_name = COALESCE(%s, first_name),
            email = COALESCE(%s, email)
            WHERE user_id= %s  
    """
    cur.execute(update_info, info)
    conn.commit()
    conn.close()


def suspend_user(display_name, first_name, suspension_end_date, user_id, comm_id):
    """suspends a user in the system"""
    conn = connect()
    cur = conn.cursor()
    user = (display_name, first_name, suspension_end_date, user_id, comm_id)
    create_suspend = """
        INSERT INTO suspended_users(display_name, first_name, suspension_end_date, user_id, comm_id)VALUES 
            (%s, %s, %s, %s, %s); 
    """
    cur.execute(create_suspend, user)
    print("User " + first_name + " is suspended until: " + suspension_end_date)
    conn.commit()
    conn.close()


def send_message(first_name, time_stamp, message, user_id, comm_id, chan_id):
    """allows a user to send a message in not suspended"""
    """FOR THIS METHOD ALSO CHECK THE COMMUNITY"""
    conn = connect()
    cur = conn.cursor()
    user = (first_name, time_stamp, message, user_id, comm_id, chan_id)
    user_comun = (user_id, comm_id)
    create_message = """
        INSERT INTO messages(first_name, time_stamp, message, user_id, comm_id, chan_id)VALUES
            (%s, %s, %s, %s, %s, %s)
    """
    suspension_check = """
        SELECT * FROM suspended_users
            WHERE first_name= %s
    """
    community_check = """
        SELECT * FROM communities_in
            WHERE user_id= %s
            AND comm_id= %s
    """
    cur.execute(suspension_check, (first_name,))
    if cur.fetchall():

        print("User " + first_name + " is suspended, we cannot send your message at this time.")

    else:
        cur.execute(community_check, user_comun)
        if cur.fetchall():
            cur.execute(create_message, user)
        else:
            print("User " + first_name + " is not part of this community")
    conn.commit()
    conn.close()


def delete_message(first_name, message, comm_id, chan_id):
    """deletes message from a channel"""
    conn = connect()
    cur = conn.cursor()
    message_info = (first_name, message, comm_id, chan_id)
    remove_mess = """
        DELETE FROM messages 
            WHERE first_name = %s
            AND message = %s
            AND comm_id = %s
            AND chan_id = %s
    """
    cur.execute(remove_mess, message_info)
    conn.commit()
    conn.close()


def delete_user(first_name):
    """deletes a user from the system"""
    conn = connect()
    cur = conn.cursor()
    remove_user = """
        DELETE FROM users
            WHERE first_name = %s
    """
    cur.execute(remove_user, (first_name,))
    conn.commit()
    conn.close()


def find_message_with_word(user_id, word):
    """finds the message, returns a list of tuples"""
    conn = connect()
    cur = conn.cursor()
    info = (user_id, word)
    find_mess = """
        SELECT * FROM messages
            WHERE user_id = %s
            AND message LIKE %s
    """
    cur.execute(find_mess, info)
    fetch = cur.fetchall()
    conn.commit()
    conn.close()
    return fetch


def add_moderator(first_name, user_id, comm_id):
    conn = connect()
    cur = conn.cursor()
    mod = (first_name, user_id, comm_id)
    add_mod = """
        INSERT INTO moderators(first_name, user_id, comm_id)VALUES
            (%s, %s, %s)
    """
    cur.execute(add_mod, mod)
    conn.commit()
    conn.close()


def moderator_privileges(mod_name, first_name=None, user_id=None, message=None, comm_id=None, chan_id=None,
                         display_name=None, suspension_end_date=None):
    """gives the moderator the ability to delete and suspend"""
    conn = connect()
    cur = conn.cursor()
    find_mod = """
        SELECT first_name FROM moderators 
            WHERE first_name = %s
    """
    cur.execute(find_mod, (mod_name,))
    if cur.fetchall():
        if message is not None:
            delete_message(first_name, message, comm_id, chan_id)
            print(mod_name + " has deleted user " + first_name + "'s message.")
        else:
            suspend_user(display_name, first_name, suspension_end_date, user_id, comm_id)
            print(mod_name + " has suspended user " + first_name + " until " + suspension_end_date)
    else:
        print(mod_name + " is not a moderator and cannot delete messages or suspend users.")


def user_privileges(first_name, chan_name=None, user_id=None, chan_id=None, comm_id=None):
    if chan_name is not None:
        add_channel(chan_name, comm_id)
        print(first_name + " has created " + chan_name + " channel to community #" + comm_id)
        if user_id is not None:
            add_to_channel(user_id, chan_id, comm_id)
            print("user with id# " + user_id + " has been added.")
    else:
        add_to_channel(user_id, chan_id, comm_id)
        print("user with id# " + user_id + " has been added.")


def read_message(first_name, chan_id, user_id, user_id_message, word):
    """allows a user to read a message if part of channel"""
    conn = connect()
    cur = conn.cursor()
    info = (user_id, chan_id)
    find_user = """
    SELECT * FROM channels_in
        WHERE user_id = %s
        AND chan_id = %s
    """
    cur.execute(find_user, info)
    if cur.fetchall():
        find_message_with_word(user_id_message, word)
        print(first_name + " is reading messages")
    else:
        print(first_name + " is not part of this channel")
    conn.commit()
    conn.close()


def build_tables():
    """builds the tables with data"""
    drop_tables()
    create_community_table()
    create_channel_table()
    create_user_table()
    create_mod_table()
    create_suspension_table()
    create_message_table()
    create_users_in_communities()
    create_private_channel_users()


def build_chat():
    """creates the chat system with communities and channels"""
    add_community('SWEN-331')
    add_community('SWEN-440')
    add_community('SWEN-344')

    """channels for SWEN-331"""
    add_channel('General', '1')
    add_channel('TA', '1')
    add_channel('Random', '1')

    """channels for SWEN-440"""
    add_channel('General', '2')
    add_channel('TA', '2')
    add_channel('Random', '2')

    """channels for SWEN-344"""
    add_channel('General', '3')
    add_channel('TA', '3')
    add_channel('Random', '3')


def build_system():
    """builds the entire chat system """
    build_tables()
    build_chat()


def main():
    build_system()
    print("the tables have been built sire!")


main()
