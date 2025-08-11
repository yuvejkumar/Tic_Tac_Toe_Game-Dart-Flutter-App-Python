import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: TicTacToePage(),
    );
  }
}

class TicTacToePage extends StatefulWidget {
  const TicTacToePage({super.key});

  @override
  State<TicTacToePage> createState() => _TicTacToePageState();
}

class _TicTacToePageState extends State<TicTacToePage> {
  List<String> board = List.filled(9, '');
  String currentPlayer = 'X';
  String winner = '';

  void handleTap(int index) {
    if (board[index] != '' || winner.isNotEmpty) return;

    setState(() {
      board[index] = currentPlayer;
      winner = checkWinner();
      if (winner.isEmpty) {
        currentPlayer = currentPlayer == 'X' ? 'O' : 'X';
      }
    });
  }

  String checkWinner() {
    final winPositions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];

    for (var pos in winPositions) {
      if (board[pos[0]] == board[pos[1]] &&
          board[pos[1]] == board[pos[2]] &&
          board[pos[0]] != '') {
        return board[pos[0]];
      }
    }

    if (!board.contains('')) return 'Tie';
    return '';
  }

  void resetGame() {
    setState(() {
      board = List.filled(9, '');
      currentPlayer = 'X';
      winner = '';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF57ccc0),
      appBar: AppBar(
        title: const Text('Yuvejkumar - Tic Tac Toe'),
        backgroundColor: const Color(0xFF57ccc0),
        elevation: 0,
        centerTitle: true,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            winner.isNotEmpty
                ? (winner == 'Tie'
                    ? 'Game Tied!'
                    : '🎉 Player $winner Wins!')
                : "Player $currentPlayer's turn",
            style: const TextStyle(
              fontSize: 22,
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 20),
          GridView.builder(
            shrinkWrap: true,
            itemCount: 9,
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 3,
              crossAxisSpacing: 5,
              mainAxisSpacing: 5,
            ),
            padding: const EdgeInsets.all(10),
            itemBuilder: (context, index) => GestureDetector(
              onTap: () => handleTap(index),
              child: Container(
                decoration: BoxDecoration(
                  color: const Color(0xFFab85a7),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Center(
                  child: Text(
                    board[index],
                    style: const TextStyle(
                      fontSize: 48,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
            ),
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF2ee43b),
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              ),
            ),
            onPressed: resetGame,
            child: const Text(
              'Restart Game',
              style: TextStyle(fontSize: 18, color: Colors.white),
            ),
          ),
        ],
      ),
    );
  }
}
