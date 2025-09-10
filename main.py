# Завдання 1
class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination


# Завдання 2
class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        time = distance / self.speed
        print(f"Рух до {destination}. Відстань: {distance} км. Час у дорозі: {time:.2f} год.")


# Завдання 3
class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.capacity = capacity
        self.passengers = []

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Пасажир {passenger.name} сів у автобус, їде до {passenger.destination}.")
        else:
            print(f"Автобус переповнений. Пасажир {passenger.name} не може сісти.")

    def move(self, destination, distance):
        exiting_passengers = [p for p in self.passengers if p.destination == destination]
        self.passengers = [p for p in self.passengers if p.destination != destination]

        print(f"Автобус прибув до {destination}. Висаджено пасажирів: {len(exiting_passengers)}.")
        if exiting_passengers:
            print("Висаджені пасажири:")
            for p in exiting_passengers:
                print(f" - {p.name}")
        else:
            print("Ніхто не вийшов на цій зупинці.")

        super().move(destination, distance)


bus = Bus(speed=60, capacity=3)

bus.board_passenger(Passenger("Олег", "Львів"))
bus.board_passenger(Passenger("Анна", "Київ"))
bus.board_passenger(Passenger("Іван", "Львів"))
bus.board_passenger(Passenger("Марія", "Одеса"))  # Перевищує місткість

bus.move("Львів", 120)

bus.move("Київ", 300)

