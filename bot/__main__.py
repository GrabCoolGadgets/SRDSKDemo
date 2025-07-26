from bot import Bot

if __name__ == '__main__':
    Bot().run()

    # Dummy Flask server for Render
    import os
    from flask import Flask
    import threading

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Bot is running fine."

    def run():
        port = int(os.environ.get("PORT", 8080))
        app.run(host="0.0.0.0", port=port)

    threading.Thread(target=run).start()
