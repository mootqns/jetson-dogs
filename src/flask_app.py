from flask import send_from_directory, Flask
import os

app = Flask(__name__)

# register the serve_uploaded_file function as a route
@app.route('/media/<filename>', methods=['GET'])
def serve_uploaded_file(filename):
    media_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
    return send_from_directory(media_folder, filename)

if __name__ == '__main__':
    app.run()
