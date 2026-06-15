from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>गणित गुरु AI</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            max-width: 600px;
            width: 90%;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        .emoji { font-size: 80px; margin-bottom: 20px; }
        h1 {
            color: #4a0080;
            font-size: 2em;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #666;
            font-size: 1.1em;
            margin-bottom: 30px;
        }
        .cards {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 30px 0;
        }
        .card {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 15px;
            cursor: pointer;
            transition: transform 0.3s;
        }
        .card:hover { transform: scale(1.05); }
        .card-emoji { font-size: 40px; }
        .card h3 { margin-top: 10px; font-size: 1em; }
        .btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 1.1em;
            cursor: pointer;
            margin-top: 20px;
            width: 100%;
        }
        .btn:hover { opacity: 0.9; }
        .footer {
            margin-top: 30px;
            color: #999;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">🎓</div>
        <h1>गणित गुरु AI</h1>
        <p class="subtitle">मराठी AI गणित शिक्षक - दहावी विद्यार्थ्यांसाठी</p>

        <div class="cards">
            <div class="card">
                <div class="card-emoji">📐</div>
                <h3>भूमिती</h3>
            </div>
            <div class="card">
                <div class="card-emoji">🔢</div>
                <h3>बीजगणित</h3>
            </div>
            <div class="card">
                <div class="card-emoji">📊</div>
                <h3>सांख्यिकी</h3>
            </div>
            <div class="card">
                <div class="card-emoji">🔵</div>
                <h3>त्रिकोणमिती</h3>
            </div>
        </div>

        <button class="btn">🚀 शिकणे सुरू करा</button>

        <div class="footer">
            <p>24/7 उपलब्ध • मराठीत शिकवतो • Free</p>
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
