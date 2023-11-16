class Car:
    def __init__(self, speed, enginePower, color, name):
        self.speed = speed
        self.enginePower = enginePower
        self.color = color
        self.name = name
        self.is_running = False
        self.current_gear = 0

    def start(self):
        if not self.is_running:
            print(f"{self.name} starts.")
            self.is_running = True
        else:
            print(f"{self.name} is already running.")

    def stop(self):
        if self.is_running:
            print(f"{self.name} stops.")
            self.is_running = False
        else:
            print(f"{self.name} is already stopped.")

    def change_gear(self, new_gear):
        self.current_gear = new_gear
        print(f"{self.name} changes gear to {self.current_gear}.")
    
    def info(self) : 
        print(f"Car Name: {self.name}, Color: {self.color}, Speed: {self.speed} km/h, Engine Power: {self.enginePower}, Gear: {self.current_gear}, Running: {self.is_running}")

# Example Test
car1 = Car(0, 200, "Blue", "Car1")

car1.info()
car1.start()
car1.change_gear(1)
car1.stop()
