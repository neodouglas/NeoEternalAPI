from flask import *
import os
import aminofix
os.system('set FLASK_ENV=development')
app = Flask(__name__)


@app.route('/api/login')
def get_timezone():
  data = request.form
  login = data.get("login")
  password = data.get("password")
  device = data.get("device")
  print(login)
  client = aminofix.Client(device)
  client.login(email = login, password = password)
  return f"{client.sid}"

if __name__ == '__main__':
  app.run("0.0.0.0", 5000)
