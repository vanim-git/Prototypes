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

# Installing NetCat:
sudo apt update
sudo apt install netcat

nc localhost 8080

@vanim-git ➜ /workspaces/Prototypes (main) $ nc localhost 8080
Hello
Response from backend 5002: Hello
@vanim-git ➜ /workspaces/Prototypes (main) $

# Installing Flask (Web Framework) and mysql connector for Python:
1. pip install flask mysql-connector-python

2. Start mysql service as daemon:
sudo service mysql start

3. Check if mysql is running:
sudo service mysql status

4. sudo mysql -u root -p
Enter 'Vani@0306' when prompted for password.

Note: This password remains until I reinstall mysql in the codespace. 

5. at prompt 'mysql>' execute these sql commands to create the shards (databases)

CREATE DATABASE blog_db_0;
CREATE DATABASE blog_db_1;

6. Verify the Databases using:
SHOW DATABASES;

7. Exit mysql using:
EXIT;

# Modify app.run() to Listen on All Interfaces 

1. By default, Flask binds to 127.0.0.1, which is not accessible outside the container. Change your Blog_App.py to:

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

This allows external connections.

2. Start Flask App:

python3 Blog_App.py

# To check if Blog_App is running and accessible using external link:

cmd$ curl http://0.0.0.0:5000/ 
cmd$ ps aux | grep Blog_App 

will show the pid details of running Blog_App flask application

# If you see 404 issues:

✅ 3. Check for Port Forwarding Issues
VS Code automatically forwards ports, but you may need to manually check and expose it:

Open the Ports tab in VS Code (View → Ports).
Look for Port 5000.
If it's missing, add it manually:
Click "Forward a Port" and enter 5000.
If it's already there but not accessible, restart the Codespace.

✅ 4. Check Your Flask Routes
If Flask is running but you still get 404 Not Found, it may be because no route matches /.

Test by running:

curl http://0.0.0.0:5000/
If it returns 404, ensure you have a defined route in Blog_App.py:

@app.route("/")
def home():
    return "Hello, Flask in Codespaces!"


✅ Check the Port Forwarding in VS Code

Open the Ports tab in VS Code (View → Ports).
Look for Port 5000.
If missing, add it manually:
Click Forward a Port.
Enter 5000 and select Public access.

For port 5000: (Ensure this port is publicly visible and it is configured to use HTTP and not HTTPS)
1. right-click -> choose port visibility -> public
2. right-click -> choose port protocol -> HTTP

Now try refreshing the external link.

# Commands to create posts: create_post is a POST command. so use curl with -L as:
curl -X POST -L http://super-duper-umbrella-5grvv4pj6jv2p66g-5000.app.github.dev/create_post -H "Content-Type: application/json" -d '{"user_id": 2, "title": "My First Post", "content": "This is a test post - 5."}'

This will show below response if successful. Make sure the password in db_config is correct 

{
  "message": "Post created successfully"
}

Note: A browser sends GET requests by default, you need to send a POST request manually either by using CURL commands or using POSTMAN tool.

# After creating posts, verify the posts are added in the DB tasble posts, using these commands:

Change to use blog_db_0 database
mysql> use blog_db_0;
mysql> SELECT * FROM posts;

