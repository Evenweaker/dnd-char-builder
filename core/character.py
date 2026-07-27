from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional
import json
from pathlib import Path

ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

@dataclass
class Character:
    name: str = ""
    race: str = ""
    subrace: str = ""
    class_name: str = ""
    level: int = 1
    background: str = ""
    alignment: str = ""
    abilities: Dict[str, int] = field(default_factory=lambda: {a: 10 for a in ABILITIES})
    ability_mods: Dict[str, int] = field(default_factory=dict)
    proficiency_bonus: int = 2
    hit_points: int = 0
    hit_die: int = 8
    speed: int = 30
    size: str = "Medium"
    skills: List[str] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    traits: List[str] = field(default_factory=list)
    equipment: List[str] = field(default_factory=list)
    notes: str = ""

    def calc_modifiers(self):
        for ab in ABILITIES:
            score = self.abilities.get(ab, 10)
            self.ability_mods[ab] = (score - 10) // 2

    def calc_hp(self):
        con_mod = self.ability_mods.get("Constitution", 0)
        self.hit_points = self.hit_die + con_mod
        if self.hit_points < 1:
            self.hit_points = 1

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def preview(self) -> str:
        name = self.name or "???"
        race = self.race or "—"
        if self.subrace:
            race = f"{self.race} ({self.subrace})"
        cls = self.class_name or "—"
        bg = self.background or "—"
        align = self.alignment or "—"

        def row(text: str) -> str:
            content = text[:46].ljust(46)
            return f"│ {content} │"

        lines = []
        lines.append("┌─ LIVE SHEET " + "─" * 36 + "┐")
        lines.append(row(name))
        lines.append(row(f"Lv{self.level}  {race}  {cls}"))
        lines.append(row(f"BG: {bg}   Align: {align}"))
        lines.append("├" + "─" * 48 + "┤")

        parts = []
        for ab in ABILITIES:
            score = self.abilities.get(ab, 10)
            mod = self.ability_mods.get(ab, (score - 10) // 2)
            sign = "+" if mod >= 0 else ""
            parts.append(f"{ab[:3]}{score}({sign}{mod})")
        lines.append(row("  ".join(parts[:3])))
        lines.append(row("  ".join(parts[3:])))

        lines.append("├" + "─" * 48 + "┤")
        hp = self.hit_points if self.hit_points else "—"
        lines.append(row(f"HP: {hp}   HD: d{self.hit_die}   Speed: {self.speed} ft   Size: {self.size}"))

        if self.skills:
            lines.append(row("Skills: " + ", ".join(self.skills)))
        if self.languages:
            lines.append(row("Lang: " + ", ".join(self.languages)))
        if self.traits:
            shown = self.traits[:2]
            for t in shown:
                lines.append(row("• " + t))
            if len(self.traits) > 2:
                lines.append(row(f"  … +{len(self.traits)-2} more traits/features"))
        if self.equipment:
            eq = self.equipment[0]
            extra = f" (+{len(self.equipment)-1} more)" if len(self.equipment) > 1 else ""
            lines.append(row(f"Gear: {eq}{extra}"))

        lines.append("└" + "─" * 48 + "┘")
        return "\n".join(lines)

    def summary(self) -> str:
        lines = []
        lines.append("=" * 50)
        lines.append(f"  {self.name.upper()}")
        lines.append(f"  Level {self.level} {self.race} {self.subrace + ' ' if self.subrace else ''}{self.class_name}")
        lines.append(f"  Background: {self.background}  |  Alignment: {self.alignment or '—'}")
        lines.append("=" * 50)
        lines.append("")
        lines.append("ABILITY SCORES")
        for ab in ABILITIES:
            score = self.abilities.get(ab, 10)
            mod = self.ability_mods.get(ab, 0)
            sign = "+" if mod >= 0 else ""
            lines.append(f"  {ab[:3].upper():3}  {score:2}  ({sign}{mod})")
        lines.append("")
        lines.append(f"Proficiency Bonus: +{self.proficiency_bonus}")
        lines.append(f"Hit Points: {self.hit_points}   Hit Die: 1d{self.hit_die}")
        lines.append(f"Speed: {self.speed} ft   Size: {self.size}")
        lines.append("")
        if self.skills:
            lines.append("Skills: " + ", ".join(self.skills))
        if self.languages:
            lines.append("Languages: " + ", ".join(self.languages))
        if self.traits:
            lines.append("")
            lines.append("Traits / Features:")
            for t in self.traits:
                lines.append(f"  • {t}")
        if self.equipment:
            lines.append("")
            lines.append("Equipment:")
            for e in self.equipment:
                lines.append(f"  • {e}")
        if self.notes:
            lines.append("")
            lines.append(f"Notes: {self.notes}")
        lines.append("=" * 50)
        return "\n".join(lines)
