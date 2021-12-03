from flask import Flask, Response, request


guitar = {
    'Classical': "https://www.youtube.com/embed/1SuUe4HC0T4?start=114", 
    'R&B': "https://www.youtube.com/embed/6BN-e_HwSQo?start=114", 
    'Jazz': "https://www.youtube.com/embed/HHUBkPb0ytQ?start=114", 
    'Blues': "https://www.youtube.com/embed/kpC69qIe02E?start=114", 
    'Reggae': "https://www.youtube.com/embed/wu3tZ4XiCII"}

piano = {
    'Classical': "https://www.youtube.com/embed/VUCI-1vIbUo?start=114", 
    'R&B': "https://www.youtube.com/embed/GS2Y_CkaXP0?start=114", 
    'Jazz': "https://www.youtube.com/embed/Uu9FfXQs4-A?start=114", 
    'Blues': "https://www.youtube.com/embed/qpB33AHHseg?start=114", 
    'Reggae': "https://www.youtube.com/embed/tlQn8_I6pjY?start=114"}

saxophone = {
    'Classical': "https://www.youtube.com/embed/Wn0wvLCnd3U", 
    'R&B': "https://www.youtube.com/embed/hiZp8bTAWbU", 
    'Jazz': "https://www.youtube.com/embed/_qTsxMS2PpA?start=114", 
    'Blues': "https://www.youtube.com/embed/xzpXw5hgMAU", 
    'Reggae': "https://www.youtube.com/embed/KviYubngius?start=114"}

violin = {
    'Classical': "https://www.youtube.com/embed/iEBX_ouEw1I", 
    'R&B': "https://www.youtube.com/embed/GAPsO-Im42g", 
    'Jazz': "https://www.youtube.com/embed/ysOITu9GukE", 
    'Blues': "https://www.youtube.com/embed/5_jN2xC6XuM?start=114", 
    'Reggae': "https://www.youtube.com/embed/4Zu-ku7d-1U"}

dicts = {'Guitar': guitar, 'Piano': piano, 'Saxophone': saxophone, 'Violin': violin}


app = Flask(__name__)


@app.route('/video', methods=['POST'])
def video():
    json_data = request.get_json()
    instrument = json_data['instrument']
    genre = json_data['genre']

    #Checks for instrument in dict, if found assigns value to video variable
    if instrument in dicts.keys():
        video = dicts[instrument]

    #Checks for genre in video variable and if found reassigns it to be the embed link rather than a dictionary
    if genre in video:
        video.keys()
        video = video[genre]

    return Response(video, mimetype='text/plain')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
