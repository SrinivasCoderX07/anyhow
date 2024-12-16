from flask import Flask, request, jsonify
from models.hybrid_model import hybrid_recommend

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id'))
    recommendations = hybrid_recommend(user_id)
    return jsonify({"user_id": user_id, "recommendations": list(recommendations)})

if __name__ == "__main__":
    app.run(debug=True)