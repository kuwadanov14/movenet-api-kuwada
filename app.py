from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    video_url = data.get("video_url")

    # 仮のレスポンス（後で本物のAI分析に差し替える）
    return jsonify({
        "status": "ok",
        "message": "Received video",
        "video_url": video_url
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
