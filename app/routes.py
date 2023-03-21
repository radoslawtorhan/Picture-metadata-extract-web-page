from pathlib import Path



from app import app
from flask import request, redirect, render_template, flash, session
from . image_metadata import get_metadata_from_file

app.config['UPLOAD_FOLDER'] = Path(__file__).parent / "static"
app.config['SECRET_KEY'] = 'sdsdadds'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',  methods=['GET', 'POST'])
def index():
    data = {}
    if request.method == "POST":
        file = request.files['filename']
        filename = "image.jpg"
        path: Path = app.config['UPLOAD_FOLDER'] / "images"
        if not path.exists():
            path.mkdir(parents=True)
        file_path = path / filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('File must be an image')
            return redirect(request.url)
        try:
            file.save(file_path)
            flash("succesfully uploaded image file")
        except Exception as e:
            print("file save error", e)
        print("file path is: ", file_path)
        imd = get_metadata_from_file(file_path)
        data['device'] = imd.device
        data['width'] = imd.width_px
        data['height'] = imd.height_px
        data['date taken'] = imd.datetime
        data['latitude'] = imd.latitude
        data['longitude'] = imd.longitude
        return render_template("main.html", data=data, image=filename)
    # Clear any flashed messages from the session before rendering the template
    session.pop('_flashes', None)
    return render_template("main.html")