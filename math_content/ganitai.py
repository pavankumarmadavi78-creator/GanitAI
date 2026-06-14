from gtts import gTTS
import os

def samjav(text):
    print(f"\n🎓 गणित गुरु: {text}\n")
    tts = gTTS(text=text, lang='mr')
    tts.save("output.mp3")
    os.system("mpv output.mp3 --really-quiet")

def formula_shikhav(topic):
    formulas = {
        "1": {
            "naam": "त्रिकोण क्षेत्रफळ",
            "formula": "½ × base × height",
            "text": "त्रिकोणाचे क्षेत्रफळ काढण्याचा फॉर्म्युला आहे अर्धा गुणिले पाया गुणिले उंची"
        },
        "2": {
            "naam": "चौरस क्षेत्रफळ",
            "formula": "side × side",
            "text": "चौरसाचे क्षेत्रफळ काढण्यासाठी बाजू गुणिले बाजू करायचे"
        },
        "3": {
            "naam": "वर्तुळ क्षेत्रफळ",
            "formula": "π × r²",
            "text": "वर्तुळाचे क्षेत्रफळ काढण्यासाठी पाई गुणिले त्रिज्या चा वर्ग करायचा"
        }
    }

    if topic in formulas:
        f = formulas[topic]
        print(f"📐 Formula: {f['formula']}")
        samjav(f['text'])
    else:
        samjav("माफ करा, हा topic अजून शिकवायचा आहे!")

while True:
    print("\n" + "="*40)
    print("🎓 गणित गुरु AI - दहावी गणित")
    print("="*40)
    print("1. त्रिकोण क्षेत्रफळ")
    print("2. चौरस क्षेत्रफळ")
    print("3. वर्तुळ क्षेत्रफळ")
    print("0. बाहेर पडा")
    print("="*40)

    choice = input("तुम्हाला काय शिकायचे आहे? (1/2/3/0): ")

    if choice == "0":
        samjav("धन्यवाद! उद्या पुन्हा या!")
        break
    else:
        formula_shikhav(choice)
