from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize game state
board = [""] * 9
current_player = "X"

def check_winner(b):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if b[pos[0]] == b[pos[1]] == b[pos[2]] != "":
            return b[pos[0]]
    if "" not in b:
        return "Tie"
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global board, current_player
    data = request.json
    index = data['index']

    if board[index] == "":
        board[index] = current_player
        winner = check_winner(board)
        response = {
            'board': board,
            'winner': winner,
            'player': current_player
        }
        current_player = "O" if current_player == "X" else "X"
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid move'}), 400

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)
