from flask import Flask, request

from pytube import YouTube


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        try:
            youtube = YouTube(url)
            stream = youtube.streams.get_highest_resolution()
            stream.download()
            message = f'Successfully downloaded {youtube.title}!'
        except Exception as e:
            message = f'Error: {str(e)}'
        return '''
            <h1>YouTube Downloader</h1>
            <p>{}</p>
            <form method="GET" action="/">
                <button type="submit">Back</button>
            </form>
        '''.format(message)
    else:
        return '''
            <h1>YouTube Downloader</h1>
            <form method="POST" action="/">
                <input type="text" name="url" placeholder="Enter YouTube URL">
                <button type="submit">Download</button>
            </form>
        '''


if __name__ == '__main__':
    app.run()
