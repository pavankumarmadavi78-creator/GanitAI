from flask import Flask, render_template_string, request, send_file
from gtts import gTTS
import os
import tempfile

app = Flask(__name__)

formulas = {
    "tribhuj": {
        "naam": "त्रिकोण क्षेत्रफळ",
        "formula": "½ × base × height",
        "marathi": "अर्धा गुणिले पाया गुणिले उंची",
        "udaharan": "पाया = 6cm, उंची = 4cm → ½ × 6 × 4 = 12 cm²",
        "audio_text": "त्रिकोणाचे क्षेत्रफळ काढण्याचा फॉर्म्युला आहे, अर्धा गुणिले पाया गुणिले उंची. उदाहरण, पाया सहा सेंटीमीटर आणि उंची चार सेंटीमीटर असेल तर, क्षेत्रफळ बारा चौरस सेंटीमीटर होईल.",
        "emoji": "📐"
    },
    "chaukas": {
        "naam": "चौरस क्षेत्रफळ",
        "formula": "side × side",
        "marathi": "बाजू गुणिले बाजू",
        "udaharan": "बाजू = 5cm → 5 × 5 = 25 cm²",
        "audio_text": "चौरसाचे क्षेत्रफळ काढण्यासाठी बाजू गुणिले बाजू करायचे. उदाहरण, बाजू पाच सेंटीमीटर असेल तर, पाच गुणिले पाच म्हणजे पंचवीस चौरस सेंटीमीटर.",
        "emoji": "⬛"
    },
    "vartul": {
        "naam": "वर्तुळ क्षेत्रफळ",
        "formula": "π × r²",
        "marathi": "पाई गुणिले त्रिज्या चा वर्ग",
        "udaharan": "त्रिज्या = 7cm → 3.14 × 7 × 7 = 153.86 cm²",
        "audio_text": "वर्तुळाचे क्षेत्रफळ काढण्यासाठी पाई गुणिले त्रिज्येचा वर्ग करायचा. उदाहरण, त्रिज्या सात सेंटीमीटर असेल तर, तीन दशांश एक चार गुणिले सात गुणिले सात म्हणजे एकशे त्रेपन्न दशांश सहासष्ट चौरस सेंटीमीटर.",
        "emoji": "🔵"
    },
    "pythagorean": {
        "naam": "पायथागोरस प्रमेय",
        "formula": "a² + b² = c²",
        "marathi": "काटकोन त्रिकोणात कर्ण² = बाजू² + बाजू²",
        "udaharan": "a=3, b=4 → c² = 9+16 = 25 → c = 5",
        "audio_text": "पायथागोरस प्रमेयानुसार, काटकोन त्रिकोणात कर्णाचा वर्ग हा इतर दोन बाजूंच्या वर्गांच्या बेरजेइतका असतो. उदाहरण, एक बाजू तीन आणि दुसरी बाजू चार असेल तर कर्ण पाच असेल.",
        "emoji": "📏"
    },
    "algebra": {
        "naam": "द्विघात समीकरण",
        "formula": "ax² + bx + c = 0",
        "marathi": "x = (-b ± √(b²-4ac)) / 2a",
        "udaharan": "x² - 5x + 6 = 0 → x = 2 किंवा x = 3",
        "audio_text": "द्विघात समीकरण सोडवण्यासाठी, x बरोबर उणे b अधिक किंवा वजा b चा वर्ग उणे चार a c चे वर्गमूळ, भागिले दोन a. उदाहरण, x वर्ग उणे पाच x अधिक सहा बरोबर शून्य असेल तर x दोन किंवा तीन येईल.",
        "emoji": "🔢"
    },
    "vyaaj": {
        "naam": "साधे व्याज",
        "formula": "V = (M × D × V) / 100",
        "marathi": "मुद्दल गुणिले दर गुणिले वेळ भागिले 100",
        "udaharan": "₹1000, 5%, 2 वर्षे → (1000×5×2)/100 = ₹100",
        "audio_text": "साध्या व्याजाचा फॉर्म्युला आहे, मुद्दल गुणिले दर गुणिले वेळ भागिले शंभर. उदाहरण, एक हजार रुपये मुद्दल, पाच टक्के दर आणि दोन वर्षे असेल तर व्याज शंभर रुपये येईल.",
        "emoji": "💰"
    }
}

HOME = '''
<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>गणित गुरु AI</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea, #764ba2); min-height:100vh; padding:20px; }
        .container { background:white; border-radius:20px; padding:30px; max-width:600px; margin:0 auto; text-align:center; }
        .emoji { font-size:70px; }
        h1 { color:#4a0080; font-size:1.8em; margin:10px 0; }
        .subtitle { color:#666; margin-bottom:25px; }
        .cards { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:20px 0; }
        .card { background:linear-gradient(135deg, #667eea, #764ba2); color:white; padding:20px 10px; border-radius:15px; text-decoration:none; display:block; transition:transform 0.2s; }
        .card:hover { transform:scale(1.05); }
        .card-emoji { font-size:35px; }
        .card h3 { margin-top:8px; font-size:0.95em; }
        .footer { margin-top:20px; color:#999; font-size:0.85em; }
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">🎓</div>
        <h1>गणित गुरु AI</h1>
        <p class="subtitle">मराठी AI गणित शिक्षक - दहावी विद्यार्थ्यांसाठी</p>
        <div class="cards">
            <a href="/formula/tribhuj" class="card"><div class="card-emoji">📐</div><h3>त्रिकोण क्षेत्रफळ</h3></a>
            <a href="/formula/chaukas" class="card"><div class="card-emoji">⬛</div><h3>चौरस क्षेत्रफळ</h3></a>
            <a href="/formula/vartul" class="card"><div class="card-emoji">🔵</div><h3>वर्तुळ क्षेत्रफळ</h3></a>
            <a href="/formula/pythagorean" class="card"><div class="card-emoji">📏</div><h3>पायथागोरस</h3></a>
            <a href="/formula/algebra" class="card"><div class="card-emoji">🔢</div><h3>द्विघात समीकरण</h3></a>
            <a href="/formula/vyaaj" class="card"><div class="card-emoji">💰</div><h3>साधे व्याज</h3></a>
        </div>
        <div class="footer">24/7 उपलब्ध • मराठीत शिकवतो • Free</div>
    </div>
</body>
</html>
'''

FORMULA_PAGE = '''
<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ f.naam }}</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea, #764ba2); min-height:100vh; padding:20px; }
        .container { background:white; border-radius:20px; padding:30px; max-width:600px; margin:0 auto; }
        .back { color:#667eea; text-decoration:none; font-size:0.9em; }
        .header { text-align:center; margin:20px 0; }
        .emoji { font-size:60px; }
        h1 { color:#4a0080; font-size:1.5em; margin-top:10px; }
        .box { background:#f5f0ff; border-radius:15px; padding:20px; margin:15px 0; }
        .box h3 { color:#4a0080; margin-bottom:10px; }
        .formula { font-size:1.4em; font-weight:bold; color:#667eea; text-align:center; padding:10px; background:white; border-radius:10px; margin:10px 0; }
        .marathi { color:#555; font-size:1em; }
        .udaharan { background:#e8f5e9; border-radius:10px; padding:15px; margin:15px 0; }
        .udaharan h3 { color:#2e7d32; margin-bottom:8px; }
        .audio-btn { display:block; background:linear-gradient(135deg, #ff6b6b, #ee5a24); color:white; text-align:center; padding:15px; border-radius:50px; text-decoration:none; margin:10px 0; font-size:1em; cursor:pointer; border:none; width:100%; }
        .btn { display:block; background:linear-gradient(135deg, #667eea, #764ba2); color:white; text-align:center; padding:15px; border-radius:50px; text-decoration:none; margin-top:10px; font-size:1em; }
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back">← मागे जा</a>
        <div class="header">
            <div class="emoji">{{ f.emoji }}</div>
            <h1>{{ f.naam }}</h1>
        </div>
        <div class="box">
            <h3>📝 Formula:</h3>
            <div class="formula">{{ f.formula }}</div>
            <p class="marathi">{{ f.marathi }}</p>
        </div>
        <div class="udaharan">
            <h3>✏️ उदाहरण:</h3>
            <p>{{ f.udaharan }}</p>
        </div>
        <button class="audio-btn" onclick="playAudio()">🔊 मराठीत ऐका</button>
        <audio id="audioPlayer" style="display:none"></audio>
        <a href="/" class="btn">🏠 मुख्य पानावर जा</a>
    </div>
    <script>
        function playAudio() {
            var audio = document.getElementById('audioPlayer');
            audio.src = '/audio/{{ topic }}';
            audio.play();
            document.querySelector('.audio-btn').textContent = '⏳ लोड होत आहे...';
            audio.oncanplay = function() {
                document.querySelector('.audio-btn').textContent = '🔊 ऐकत आहे...';
            }
            audio.onended = function() {
                document.querySelector('.audio-btn').textContent = '🔊 मराठीत ऐका';
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return HOME

@app.route('/formula/<topic>')
def formula(topic):
    f = formulas.get(topic)
    if not f:
        return '<h1>Formula सापडला नाही</h1>'
    return render_template_string(FORMULA_PAGE, f=f, topic=topic)

@app.route('/audio/<topic>')
def audio(topic):
    f = formulas.get(topic)
    if not f:
        return 'Not found', 404
    tts = gTTS(text=f['audio_text'], lang='mr')
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(tmp.name)
    return send_file(tmp.name, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
