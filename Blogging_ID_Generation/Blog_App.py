from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configurations for two shards
db_config = {
    0: {"host": "localhost", "user": "root", "password": "password", "database": "blog_db_0"},
    1: {"host": "localhost", "user": "root", "password": "password", "database": "blog_db_1"},
}

def get_db_connection(user_id):
    """Determine which shard to connect to based on user_id"""
    db_index = user_id % 2
    return mysql.connector.connect(**db_config[db_index])

@app.route("/create_post", methods=["POST"])
def create_post():
    data = request.json
    user_id = data.get("user_id")
    title = data.get("title")
    content = data.get("content")
    
    if not all([user_id, title, content]):
        return jsonify({"error": "Missing fields"}), 400
    
    conn = get_db_connection(user_id)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            title VARCHAR(255),
            content TEXT
        )
    """)
    
    cursor.execute("INSERT INTO posts (user_id, title, content) VALUES (%s, %s, %s)", (user_id, title, content))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Post created successfully"})

@app.route("/get_posts/<int:user_id>", methods=["GET"])
def get_posts(user_id):
    conn = get_db_connection(user_id)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM posts WHERE user_id = %s", (user_id,))
    posts = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
