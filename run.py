from pipe import app, socket


if __name__ == '__main__':
    app.run()
    socket.run(app)
