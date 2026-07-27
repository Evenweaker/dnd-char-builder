# PHB core races with traits
RACES = {
    "Dwarf": {
        "ability_bonuses": {"Constitution": 2},
        "speed": 25,
        "size": "Medium",
        "languages": ["Common", "Dwarvish"],
        "traits": [
            "Darkvision 60 ft",
            "Dwarven Resilience (adv. vs poison, resistance to poison)",
            "Dwarven Combat Training (battleaxe, handaxe, light hammer, warhammer)",
            "Tool Proficiency (smith's, brewer's, or mason's tools)",
            "Stonecunning (double proficiency on History checks related to stonework)",
        ],
        "subraces": {
            "Hill Dwarf": {
                "ability_bonuses": {"Wisdom": 1},
                "traits": ["Dwarven Toughness (+1 HP per level)"],
            },
            "Mountain Dwarf": {
                "ability_bonuses": {"Strength": 2},
                "traits": ["Dwarven Armor Training (light & medium armor)"],
            },
        },
    },
    "Elf": {
        "ability_bonuses": {"Dexterity": 2},
        "speed": 30,
        "size": "Medium",
        "languages": ["Common", "Elvish"],
        "traits": [
            "Darkvision 60 ft",
            "Keen Senses (proficiency in Perception)",
            "Fey Ancestry (adv. vs charm, immune to magic sleep)",
            "Trance (4 hours meditation instead of sleep)",
        ],
        "subraces": {
            "High Elf": {
                "ability_bonuses": {"Intelligence": 1},
                "traits": [
                    "Elf Weapon Training (longsword, shortsword, shortbow, longbow)",
                    "Cantrip (one wizard cantrip; Int is spellcasting ability)",
                    "Extra language",
                ],
            },
            "Wood Elf": {
                "ability_bonuses": {"Wisdom": 1},
                "speed": 35,
                "traits": [
                    "Elf Weapon Training (longsword, shortsword, shortbow, longbow)",
                    "Fleet of Foot (speed 35 ft)",
                    "Mask of the Wild (can attempt to hide in natural phenomena)",
                ],
            },
            "Dark Elf (Drow)": {
                "ability_bonuses": {"Charisma": 1},
                "traits": [
                    "Superior Darkvision 120 ft",
                    "Sunlight Sensitivity",
                    "Drow Magic (dancing lights; faerie fire / darkness later)",
                    "Drow Weapon Training (rapier, shortsword, hand crossbow)",
                ],
            },
        },
    },
    "Halfling": {
        "ability_bonuses": {"Dexterity": 2},
        "speed": 25,
        "size": "Small",
        "languages": ["Common", "Halfling"],
        "traits": [
            "Lucky (reroll 1s on attack rolls, ability checks, saving throws)",
            "Brave (adv. vs frightened)",
            "Halfling Nimbleness (move through space of larger creatures)",
        ],
        "subraces": {
            "Lightfoot": {
                "ability_bonuses": {"Charisma": 1},
                "traits": ["Naturally Stealthy (hide behind creatures larger than you)"],
            },
            "Stout": {
                "ability_bonuses": {"Constitution": 1},
                "traits": ["Stout Resilience (adv. vs poison, resistance to poison)"],
            },
        },
    },
    "Human": {
        "ability_bonuses": {"all": 1},
        "speed": 30,
        "size": "Medium",
        "languages": ["Common"],
        "traits": ["Extra language"],
        "subraces": {},
    },
    "Dragonborn": {
        "ability_bonuses": {"Strength": 2, "Charisma": 1},
        "speed": 30,
        "size": "Medium",
        "languages": ["Common", "Draconic"],
        "traits": [
            "Draconic Ancestry (choose dragon type → damage type & breath weapon)",
            "Breath Weapon (action; 2d6, scales with level)",
            "Damage Resistance (matching your ancestry)",
        ],
        "subraces": {},
    },
    "Gnome": {
        "ability_bonuses": {"Intelligence": 2},
        "speed": 25,
        "size": "Small",
        "languages": ["Common", "Gnomish"],
        "traits": [
            "Darkvision 60 ft",
            "Gnome Cunning (adv. on Int/Wis/Cha saves vs magic)",
        ],
        "subraces": {
            "Forest Gnome": {
                "ability_bonuses": {"Dexterity": 1},
                "traits": [
                    "Natural Illusionist (minor illusion cantrip)",
                    "Speak with Small Beasts",
                ],
            },
            "Rock Gnome": {
                "ability_bonuses": {"Constitution": 1},
                "traits": [
                    "Artificer's Lore (double proficiency on History related to magic items, alchemical objects, tech)",
                    "Tinker (construct a tiny clockwork device)",
                ],
            },
        },
    },
    "Half-Elf": {
        "ability_bonuses": {"Charisma": 2},
        "speed": 30,
        "size": "Medium",
        "languages": ["Common", "Elvish"],
        "traits": [
            "Darkvision 60 ft",
            "Fey Ancestry (adv. vs charm, immune to magic sleep)",
            "Skill Versatility (two skill proficiencies of your choice)",
            "Extra language",
        ],
        "subraces": {},
    },
    "Half-Orc": {
        "ability_bonuses": {"Strength": 2, "Constitution": 1},
        "speed": 30,
        "size": "Medium",
        "languages": ["Common", "Orc"],
        "traits": [
            "Darkvision 60 ft",
            "Menacing (proficiency in Intimidation)",
            "Relentless Endurance (once per long rest, drop to 1 HP instead of 0)",
            "Savage Attacks (extra weapon die on critical hits with melee weapons)",
        ],
        "subraces": {},
    },
    "Tiefling": {
        "ability_bonuses": {"Intelligence": 1, "Charisma": 2},
        "speed": 30,
        "size": "Medium",
        "languages": ["Common", "Infernal"],
        "traits": [
            "Darkvision 60 ft",
            "Hellish Resistance (resistance to fire)",
            "Infernal Legacy (thaumaturgy; hellish rebuke / darkness later)",
        ],
        "subraces": {},
    },
}
