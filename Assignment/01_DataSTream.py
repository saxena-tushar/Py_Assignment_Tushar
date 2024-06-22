"""Problem #1 - Data Stream Ingestion
In a data stream, data is read in consecutive chunks - so you only have access to a certain portion of data at a given time. This is in contrast to having an entire sequence available at once. For example, Netflix and Youtube use streaming to allow users to watch chunks of video, rather than have user wait for the entire video to load - before they can start watching.

Design a system that receives a stream of strings along with timestamps. Each unique string should be printed at most every 5 seconds (i.e.,  string printed at timestamp t will prevent the same message from being printed until t + 5 seconds have passed).

All strings will be received in chronological order. Several strings may arrive at the same time.

Implement the DataStream class:
•	DataStream creates a data_stream object
•	bool should_output_data_str(int timestamp, str data_str) returns  true if the data_string should be printed in the provided timestamp, otherwise returns false
"""
class DataStream:
    def __init__(self) -> None:
        self.print_log = {}

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        if data_string not in self.print_log or timestamp - self.print_log[data_string] >= 5:
            self.print_log[data_string] = timestamp
            return True
        return False

def main():
    data_stream = DataStream()
    inputs = [
        (0, "hello"),
        (1, "world"),
        (4, "hello"),
        (7, "hello"),
        (8, "world")
    ]

    results = [data_stream.should_output_data_str(timestamp, data_string) for timestamp, data_string in inputs]
    print(results)

if __name__ == "__main__":
    main()
