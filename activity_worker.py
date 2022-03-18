import asyncio

from temporalio.client import Client
from temporalio.worker import Worker
import chess.engine

TEMPORAL_ADDRESS = "http://127.0.0.1:11111"
TEMPORAL_NAMESPACE = "default"


class Bot:
    def __init__(self) -> None:
        self.engine = chess.engine.SimpleEngine.popen_uci("stockfish")

    def play(self, fen: str) -> str:
        board = chess.Board(fen)
        play = self.engine.play(board, chess.engine.Limit(time=0.250))
        return play.move.uci()


async def play(fen: str) -> str:
    bot = Bot()
    result = bot.play(fen)
    print("Generated move", result)
    return result


async def main():
    client = await Client.connect(TEMPORAL_ADDRESS, namespace=TEMPORAL_NAMESPACE)
    print("Client connected as", client.identity)
    worker = Worker(
        client,
        task_queue="queue",
        activities={"play": play},
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
