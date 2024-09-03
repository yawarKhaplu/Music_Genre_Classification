from flask import Flask, render_template,request, redirect, jsonify
from werkzeug.utils import secure_filename
import os
import ClassifyGenre
app = Flask(__name__)

genres = ClassifyGenre.GENRES
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MUSIC_FOLDER'] = 'static/music'
recent_uploads = []  # List to keep track of recently uploaded music

@app.route('/')
def index():
    return render_template('index.html',recent_uploads=recent_uploads)

@app.route('/add_music', methods=['POST', 'GET'])
def add_music():
    try:
        if request.method == 'POST':
            if 'music_file' not in request.files:
                return jsonify({'message': 'No file part in the request', 'saved_files': []}), 400

            uploaded_files = request.files.getlist('music_file')
            saved_files = []

            for file in uploaded_files:
                if file and allowed_files(file.filename):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    
                    # Save the file to the 'uploads' folder
                    file.save(filepath)
                    
                    # Check if the file exists in the 'uploads' folder
                    if not os.path.exists(filepath):
                        return jsonify({'message': f'Error: File {filename} was not found in the uploads folder.'}), 500
                    
                    saved_files.append(filename)

                    # Continue processing the file...
                    genre = ClassifyGenre.predict_genre(filepath)

                    # Create genre folder and move the file
                    genre_folder = os.path.join('static/music', genre)
                    if not os.path.exists(genre_folder):
                        os.makedirs(genre_folder)

                    genre_filepath = os.path.join(genre_folder, filename)
                    os.rename(filepath, genre_filepath)
                    genre_folder = os.path.join('music', genre)
                    # Add recent uploads
                    recent_uploads.append({
                        'filename': filename,
                        'genre': genre,
                        'filepath': os.path.join(genre_folder, filename).replace('\\','/')
                    })

            return jsonify({"saved_files": saved_files, "message": "File uploaded and moved to the " + genre + " Category."})
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

    return render_template('add_music.html')


@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/genre')
def genre():
    return render_template('classfic.html', genre=genre)

@app.route('/genre/<genre_name>')
def genre_page(genre_name):
    if genre_name in genres:
        # Path to the music directory for the genre
        genre_path = os.path.join('static', 'music', genre_name)
        
        # Check if the directory exists
        if os.path.exists(genre_path):
            # List all mp3 files in the genre's directory
            songs = [
                {"title": os.path.splitext(song)[0], "filepath": f"music/{genre_name}/{song}"}
                for song in os.listdir(genre_path) if song.endswith('.mp3')
            ]
        else:
            # If the directory doesn't exist, return an empty list
            songs = []

        return render_template('genre.html', genre=genre_name, songs=songs)
    else:
        return render_template('404.html'), 404  # Handle unknown genres

def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'wav','mp3','ogg'}
if __name__ == '__main__':
    app.run(debug=True)
