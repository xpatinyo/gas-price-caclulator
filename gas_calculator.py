# Gas Price Calculator
# Copyright (c) 2025 Gas Price Calculator Project
# Licensed under CC BY-NC 4.0: https://creativecommons.org/licenses/by-nc/4.0/

import json
import os


class GasCalculator:
    def __init__(
        self,
        lenght_in_km: float,
        liters_per_100km: float,
        price_per_liter: float,
        num_people: int | None,
        language: str = "english",
    ):
        self.lenght_in_km = lenght_in_km
        self.liters_per_100km = liters_per_100km
        self.price_per_liter = price_per_liter
        self.num_people = num_people
        self.language = language
        self.total_cost = self.calculate_total_cost()
        self.cost_per_person = self.total_cost / self.num_people if self.num_people and self.num_people >= 2 else None
        self.translations = self._load_translations()

    def _load_translations(self) -> dict:
        """Load language translations from JSON file"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "languages.json")
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_translation(self, language: str, key: str) -> str:
        """Get translation for a specific key in a specific language"""
        if language in self.translations:
            return self.translations[language].get(key, key)
        # Fallback to English if language not found
        return self.translations.get("english", {}).get(key, key)

    def calculate_total_cost(self) -> float:
        total_liters = (self.lenght_in_km / 100) * self.liters_per_100km
        total_cost = total_liters * self.price_per_liter

        return total_cost

    def generate_report(self, language: str, title: str | None = None) -> str:
        # Use provided title or default translation for the specified language
        display_title = title if title else self.get_translation(language, "default_title")

        # Build basic report information
        report_lines = [
            f"*{display_title}*",
            f"{self.get_translation(language, 'total_distance')}: {self.lenght_in_km} km",
            f"{self.get_translation(language, 'vehicle_consumption')}: {self.liters_per_100km} L/100km",
            f"{self.get_translation(language, 'price_per_liter')}: {self.price_per_liter} €",
        ]

        # Add people-specific information if applicable
        if not self.num_people or self.num_people < 2:
            report_lines.append(f"{self.get_translation(language, 'total_cost')}: *{self.total_cost:.2f} €*")
        else:
            report_lines.extend(
                [
                    f"{self.get_translation(language, 'people')}: {self.num_people}",
                    f"{self.get_translation(language, 'total_cost')}: {self.total_cost:.2f} €",
                    f"{self.get_translation(language, 'cost_per_person')}: *{self.cost_per_person:.2f} €*",
                ]
            )

        return "\n".join(report_lines)
