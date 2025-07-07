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

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

[![CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)

**You are free to:**
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

**Under the following terms:**
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** — You may not use the material for commercial purposes.

**No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For more details, see the [LICENSE](LICENSE) file.
