# Gas Price Calculator

Calculate fuel costs for trips and split them among multiple people in different languages.

## Usage

```python
from gas_calculator import GasCalculator

calculator = GasCalculator(
    lenght_in_km=150.0,
    liters_per_100km=6.5,
    price_per_liter=1.45,
    num_people=3,
    language="english"
)

print(calculator.pretty_print("english", "Happy Road Trip!"))
```

Output:
```
=== Happy Road Trip! ===
Total distance: 150.0 km
Vehicle consumption: 6.5 L/100km
Price per liter: 1.45 €
Total cost: 14.18 €
People: 3
*Cost per person: 4.73 €*
```

## Supported Languages

- `"english"`, `"french"`, `"catalan"`

## Run

```bash
python main.py
```
