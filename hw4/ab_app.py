import multiprocessing
import threading
import time
import codecs
from datetime import datetime


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


def process_a(input_queue, intermediate_queue):
    def forward_messages():
        while True:
            if not input_queue.empty():
                msg = input_queue.get()
                lower_msg = msg.lower()
                intermediate_queue.put(lower_msg)
                log(f"Process A forwarded: {lower_msg.strip()}")
            time.sleep(5)

    threading.Thread(target=forward_messages, daemon=True).start()
    while True:
        time.sleep(1)


def process_b(intermediate_queue, output_queue):
    while True:
        if not intermediate_queue.empty():
            msg = intermediate_queue.get()
            encoded = codecs.encode(msg, "rot_13")
            log(f"Process B output: {encoded.strip()}")
            output_queue.put(encoded)
        time.sleep(1)


if __name__ == "__main__":
    input_queue = multiprocessing.Queue()
    intermediate_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    proc_a = multiprocessing.Process(
        target=process_a, args=(input_queue, intermediate_queue)
    )
    proc_b = multiprocessing.Process(
        target=process_b, args=(intermediate_queue, output_queue)
    )

    proc_a.start()
    proc_b.start()

    try:
        while True:
            user_input = input(
                f"[{datetime.now().strftime('%H:%M:%S')}] Enter message: "
            )
            input_queue.put(user_input)
            
    except KeyboardInterrupt:
        log("Shutting down...")
        proc_a.terminate()
        proc_b.terminate()
        proc_a.join()
        proc_b.join()
