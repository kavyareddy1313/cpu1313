def adjust_cpu_frequency_and_voltage(self, task):
        if task.priority > 7:
            self.cpu_frequency = 3.5  # High priority -> Increase frequency
            self.voltage = 1.3
        elif task.priority > 4:
            self.cpu_frequency = 2.5  # Medium priority -> Moderate frequency
            self.voltage = 1.2
        else:
            self.cpu_frequency = 1.5  # Low priority -> Lower frequency to save energy
            self.voltage = 1.1
        print(f"CPU Frequency adjusted to: {self.cpu_frequency} GHz, Voltage adjusted to: {self.voltage} V")