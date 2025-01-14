#fsc_tin_10
# Dự án 10: Ứng dụng web đơn giản
#Phải cài đặt Flask: pip install flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Xin chào, thế giới!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
