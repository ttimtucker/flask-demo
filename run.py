from flaskblog import app

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)


