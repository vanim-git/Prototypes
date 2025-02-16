# Prototypes
A repo of all the practice prototypes

To install mysql:

vanim-git: how do i install mysql server?

GitHub Copilot: To install MySQL Server on a Linux machine, you can follow these steps:

1. **Update your package index:**
   ```bash
   sudo apt update
   ```

2. **Install MySQL Server:**
   ```bash
   sudo apt install mysql-server
   ```

1. **Start a service:**
   ```bash
   sudo service <service_name> start
   ```

   Example:
   ```bash
   sudo service mysql start
   ```

2. **Stop a service:**
   ```bash
   sudo service <service_name> stop
   ```

   Example:
   ```bash
   sudo service mysql stop
   ```

3. **Restart a service:**
   ```bash
   sudo service <service_name> restart
   ```

   Example:
   ```bash
   sudo service mysql restart
   ```

4. **Reload a service's configuration:**
   ```bash
   sudo service <service_name> reload
   ```

   Example:
   ```bash
   sudo service mysql reload
   ```

5. **Check the status of a service:**
   ```bash
   sudo service <service_name> status
   ```

   Example:
   ```bash
   sudo service mysql status
   ```


Note that on modern Linux distributions, the `systemctl` command is often preferred over the `service` command for managing services. However, the `service` command is still available and can be used in the same way.

To import MySQL connector: pip install mysql-connector-python

# To reset the root password:

@vanim-git ➜ /workspaces/Prototypes/Connection_Pool (main) $ sudo mysql

        mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Vani@0306';FLUSH PRIVILEGES;
        Query OK, 0 rows affected (0.01 sec)

        Query OK, 0 rows affected (0.00 sec)

        mysql> EXIT

@vanim-git ➜ /workspaces/Prototypes/Connection_Pool (main) $ sudo service mysql restart

After resetting the password, check the login:

sudo mysql -u root -p
Pwd: Vani@0306


