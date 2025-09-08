class ModelBasedReflexAgent:
    def __init__(self,temperature):
        self.fixed_temp=temperature
        self.last_action=None

    def sensor(self,temperature):
        self.current_temp=temperature

    def performance(self):
        if self.current_temp <self.fixed_temp:
            action="Turn on Heater"
        else:
            action="Turn off Heater"

        if action == self.last_action:
            action="No Change"

        self.last_action = action if action != "No Change" else self.last_action
        return action
    
    
    def actuator(self):
        action = self.performance()
        print(self.current_temp,"C => Action:",action)
    
rooms={
    "Drawing Room":20,
    "Living Room":22,
    "Kitchen":30,
    "Bedroom":23,
}

# print("=== Simple Reflex Agent")
# simple_agent=SimpleReflexAgent(22)
# for room, temperature in rooms.items():
#  print(room,end=' :\t')
#  simple_agent.sensor(temperature)
#  simple_agent.actuator()

print("=== Model Reflex Agent")
model_agent=ModelBasedReflexAgent(22)
for room, temp in rooms.items():
 print(room,end=' :\t')
 model_agent.sensor(temp)
 model_agent.actuator()

print("\n === Repeated Sensor Reading")
model_agent.sensor(22)
model_agent.actuator()
model_agent.sensor(22)
model_agent.actuator()