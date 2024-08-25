from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Function to verify username and password
def check_auth(username, password):
    return username == 'admin' and password == '1234'

# Function to prompt for credentials
def authenticate():
    login_form = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Login Required</title>
      </head>
      <body>
        <h2>Login Required</h2>
        <form method="post" action="/auth-checker">
          <label for="username">Username:</label>
          <input type="text" id="username" name="username" required>
          <br>
          <label for="password">Password:</label>
          <input type="password" id="password" name="password" required>
          <br>
          <input type="submit" value="Login">
        </form>
      </body>
    </html>
    """
    return render_template_string(login_form)

@app.route('/auth-checker', methods=['GET', 'POST'])
def auth_checker():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if check_auth(username, password):
            # Set a cookie or session to mark the user as authenticated
            response = redirect('http://app2.bycontrolia.com')
            response.set_cookie('auth_token', 'authenticated')  # Set a dummy cookie for demonstration
            return response
        else:
            return authenticate()
    else:
        auth_token = request.cookies.get('auth_token')
        if auth_token == 'authenticated':
            return redirect('http://app2.bycontrolia.com')
        return authenticate()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
