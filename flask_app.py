from flask import send_from_directory, Flask

app = Flask(__name__)

# Register the serve_uploaded_file function as a route
@app.route('/media/<filename>', methods=['GET'])
def serve_uploaded_file(filename):
    media_folder = './media'
    return send_from_directory(media_folder, filename)

if __name__ == '__main__':
    app.run()
