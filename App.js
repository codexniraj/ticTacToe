import React, { useState } from "react";
import "./App.css";

function App() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [player, setPlayer] = useState("X");
  const [winner, setWinner] = useState(null);

  const handleClick = (position) => {
    if (board[position] === null && winner === null) {
      const newBoard = [...board];
      newBoard[position] = player;
      setBoard(newBoard);
      if (player === "X") {
        setPlayer("O");
      } else {
        setPlayer("X");
      }
    }
  };

  return (
    <div className="App">
      <div className="board">
        {board.map((value, index) => (
          <div
            key={index}
            className={`cell ${value}`}
            onClick={() => handleClick(index)}
          >
            {value}
          </div>
        ))}
      </div>
      {winner ? <div className="winner">{winner} wins!</div>
  : board.every((cell) => cell !== null) ? (
      <div className="winner">It's a tie!</div>
    ) : (
      <div className="player">{player}'s turn</div>
    )}
</div>
);
}
