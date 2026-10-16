class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       self.current = start

   def set_max(self, max_value):
        self.max_value = max_value

   def set_min(self, min_value):
       self.min_value = min_value

   def step_up(self):
       if self.current >= self.min_value:
           raise ValueError("досянуто максимум")
   def step_down(self):
        if self.current <= self.max_value:
           raise ValueError("досянуто мінімум")
        self.current -= 1

   def get_current(self):
       return self.current

counter = Counter()
counter.set_current(9)
print(counter.get_current())
try:
    counter.step_up()
    print({counter.get_current()})

    counter.step_down()
except ValueError as e:
    print(e) # Достигнут максимум
    print(counter.get_current())

counter.set_min(5)
counter.set_current(6)

try:
    counter.step_down()  # ValueError
    print({counter.get_current()})

    counter.step_up()
except ValueError as e:
    print(e) # Достигнут минимум
print(counter.get_current())
