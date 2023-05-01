from flask import Flask, request, jsonify
from board import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app
.route("/move", methods=["POST"])
def move():
data = request.json
row = data["row"]
col = data["col"]
player = data["player"]
result = game.move(row, col, player)
if result == "invalid":
return jsonify({"error": "Invalid move"}), 400
elif result == "win":
return jsonify({"winner": player})
elif result == "tie":
return jsonify({"winner": "tie"})
else:
return jsonify({"player": result})

if name == "main":
app.run(debug=True)
 
 

