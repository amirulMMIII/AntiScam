from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/lapor', methods=['POST'])
def lapor():
    data = request.json
    mesej_scam = data.get('text')
    
    # Simpan laporan rakyat ke dalam database.csv secara automatik
    new_data = pd.DataFrame([[mesej_scam, 1]], columns=['text', 'label'])
    new_data.to_csv('database.csv', mode='a', header=False, index=False)
    
    return jsonify({"status": "Berjaya", "info": "Data disimpan untuk diproses AI."})

if __name__ == '__main__':
    app.run(debug=True)