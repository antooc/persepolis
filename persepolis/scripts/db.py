# -*- coding: utf-8 -*-
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sqlite3



# download manager data_base path .
if os_type == 'Linux' or os_type == 'FreeBSD' or os_type == 'OpenBSD':
    data_base_path = os.path.join(
        str(home_address), ".config/persepolis_download_manager/persepolis.db")
elif os_type == 'Darwin':
    data_base_path = os.path.join(
        str(home_address), "Library/Application Support/persepolis_download_manager/persepolis.db")
elif os_type == 'Windows':
    data_base_path = os.path.join(
        str(home_address), 'AppData', 'Local', 'persepolis_download_manager', 'persepolis.db')


sqlite_connection = sqlite3.connect(data_base_path)
sqlite_cursor = sqlite_connection.cursor()

def createTables():
# download table contains download table download items information
    sqlite_cursor.execute("""CREATE TABLE IF NOT EXISTS download_table(
                                                                                ID INTEGER PRIMARY KEY,
                                                                                file_name TEXT,
                                                                                status TEXT,
                                                                                size TEXT,
                                                                                downloaded_size TEXT,
                                                                                percent TEXT,
                                                                                connections TEXT,
                                                                                rate TEXT,
                                                                                estimate_time_left TEXT,
                                                                                gid TEXT,
                                                                                firs_try_date TEXT,
                                                                                last_try_date TEXT
                                                                                )""")


# add_link_table contains addlink window download information
    sqlite_cursor.execute("""CREATE TABLE IF NOT EXISTS addlink(
                                                                            ID INTEGER PRIMARY KEY,
                                                                            gid TEXT,
                                                                            last_try_date TEXT,
                                                                            firs_try_date TEXT,
                                                                            out TEXT,
                                                                            final_download_path TEXT,
                                                                            start_hour TEXT,
                                                                            start_minute TEXT,
                                                                            end_hour TEXT,
                                                                            end_minute TEXT,
                                                                            link TEXT,
                                                                            ip TEXT,
                                                                            port TEXT,
                                                                            proxy_user TEXT,
                                                                            proxy_passwd TEXT,
                                                                            download_user TEXT,
                                                                            download_passwd TEXT,
                                                                            connections TEXT,
                                                                            limit TEXT,
                                                                            download_path TEXT
                                                                            )""") 
# queues_list contains name of categories
    sqlite_cursor.execute("""CREATE TABLE IF NOT EXISTS queues_list(
                                                                queue_name
                                                                )""")


