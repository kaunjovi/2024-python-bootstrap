class StackFrontier():
    def __init__(self):
        print("Constructor??")
        self.frontier = []


class QueueFrontier (StackFrontier):
    def sayhello():
        print(f"Hello, from QueueFrontier.")


if __name__ == '__main__':
    print("Hello world from maze.")
    sf = StackFrontier()
    qf = QueueFrontier()
    # qf.sayhello()
