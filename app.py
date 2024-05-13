from flask import Flask
from print_page import gen_from_text
app = Flask(__name__)

@app.route('/')
def home():
    input_text = "人生到處知何似應似飛鴻踏雪泥泥上偶然留指爪鴻飛哪復計東西老僧已死成新塔壞壁無由見舊題往日崎嶇還記否路長人困蹇驢嘶"
    gen_all = gen_from_text(input_text)
    return '\n'.join(gen_all)

if __name__ == '__main__':
    app.run()

