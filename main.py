# Gas Price Calculator
# Copyright (c) 2025 Gas Price Calculator Project
# Licensed under CC BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/

from gas_calculator import GasCalculator


# Example values
lenght_in_km = 150.0
liters_per_100km = 6.5
price_per_liter = 1.45
num_people = 3

# Create an instance of GasCalculator
calculator = GasCalculator(
    lenght_in_km,
    liters_per_100km,
    price_per_liter,
    num_people,
    language="english",
)

# Print the results
print(calculator.generate_report(language="english"))
