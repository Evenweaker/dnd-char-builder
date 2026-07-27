# Auto-split for upload
CLASSES_A = {
  "Barbarian": {
    "hit_die": 12,
    "primary": [
      "Strength"
    ],
    "saving_throws": [
      "Strength",
      "Constitution"
    ],
    "armor_prof": [
      "Light",
      "Medium",
      "Shields"
    ],
    "weapon_prof": [
      "Simple",
      "Martial"
    ],
    "skills": [
      "Animal Handling",
      "Athletics",
      "Intimidation",
      "Nature",
      "Perception",
      "Survival"
    ],
    "num_skills": 2,
    "equipment_options": [
      [
        "Greataxe",
        "Two handaxes"
      ],
      [
        "Explorer's pack",
        "Dungeoneer's pack"
      ],
      [
        "Four javelins"
      ]
    ],
    "features": [
      "Rage (2/long rest)",
      "Unarmored Defense (10 + Dex + Con)"
    ]
  },
  "Bard": {
    "hit_die": 8,
    "primary": [
      "Charisma"
    ],
    "saving_throws": [
      "Dexterity",
      "Charisma"
    ],
    "armor_prof": [
      "Light"
    ],
    "weapon_prof": [
      "Simple",
      "Hand Crossbow",
      "Longsword",
      "Rapier",
      "Shortsword"
    ],
    "skills": [
      "Acrobatics",
      "Animal Handling",
      "Arcana",
      "Athletics",
      "Deception",
      "History",
      "Insight",
      "Intimidation",
      "Investigation",
      "Medicine",
      "Nature",
      "Perception",
      "Performance",
      "Persuasion",
      "Religion",
      "Sleight of Hand",
      "Stealth",
      "Survival"
    ],
    "num_skills": 3,
    "equipment_options": [
      [
        "Rapier",
        "Longsword",
        "Any simple weapon"
      ],
      [
        "Diplomat's pack",
        "Entertainer's pack"
      ],
      [
        "Lute",
        "Any other musical instrument"
      ],
      [
        "Leather armor",
        "Dagger"
      ]
    ],
    "features": [
      "Spellcasting (Bard)",
      "Bardic Inspiration (d6, Cha mod / long rest)"
    ]
  },
  "Cleric": {
    "hit_die": 8,
    "primary": [
      "Wisdom"
    ],
    "saving_throws": [
      "Wisdom",
      "Charisma"
    ],
    "armor_prof": [
      "Light",
      "Medium",
      "Shields"
    ],
    "weapon_prof": [
      "Simple"
    ],
    "skills": [
      "History",
      "Insight",
      "Medicine",
      "Persuasion",
      "Religion"
    ],
    "num_skills": 2,
    "equipment_options": [
      [
        "Mace",
        "Warhammer (if proficient)"
      ],
      [
        "Scale mail",
        "Leather armor",
        "Chain mail (if proficient)"
      ],
      [
        "Light crossbow + 20 bolts",
        "Any simple weapon"
      ],
      [
        "Priest's pack",
        "Explorer's pack"
      ],
      [
        "Shield",
        "Holy symbol"
      ]
    ],
    "features": [
      "Spellcasting (Cleric)",
      "Divine Domain (choose domain)"
    ]
  },
  "Druid": {
    "hit_die": 8,
    "primary": [
      "Wisdom"
    ],
    "saving_throws": [
      "Intelligence",
      "Wisdom"
    ],
    "armor_prof": [
      "Light",
      "Medium (non-metal)",
      "Shields (non-metal)"
    ],
    "weapon_prof": [
      "Clubs",
      "Daggers",
      "Darts",
      "Javelins",
      "Maces",
      "Quarterstaffs",
      "Scimitars",
      "Sickles",
      "Slings",
      "Spears"
    ],
    "skills": [
      "Arcana",
      "Animal Handling",
      "Insight",
      "Medicine",
      "Nature",
      "Perception",
      "Religion",
      "Survival"
    ],
    "num_skills": 2,
    "equipment_options": [
      [
        "Wooden shield",
        "Any simple weapon"
      ],
      [
        "Scimitar",
        "Any simple melee weapon"
      ],
      [
        "Leather armor",
        "Explorer's pack",
        "Druidic focus"
      ]
    ],
    "features": [
      "Druidic (secret language)",
      "Spellcasting (Druid)"
    ]
  },
  "Fighter": {
    "hit_die": 10,
    "primary": [
      "Strength",
      "Dexterity"
    ],
    "saving_throws": [
      "Strength",
      "Constitution"
    ],
    "armor_prof": [
      "All",
      "Shields"
    ],
    "weapon_prof": [
      "Simple",
      "Martial"
    ],
    "skills": [
      "Acrobatics",
      "Animal Handling",
      "Athletics",
      "History",
      "Insight",
      "Intimidation",
      "Perception",
      "Survival"
    ],
    "num_skills": 2,
    "equipment_options": [
      [
        "Chain mail",
        "Leather + longbow + 20 arrows"
      ],
      [
        "Martial weapon + shield",
        "Two martial weapons"
      ],
      [
        "Light crossbow + 20 bolts",
        "Two handaxes"
      ],
      [
        "Dungeoneer's pack",
        "Explorer's pack"
      ]
    ],
    "features": [
      "Fighting Style (choose one)",
      "Second Wind (1d10 + level, 1/short rest)"
    ]
  },
  "Monk": {
    "hit_die": 8,
    "primary": [
      "Dexterity",
      "Wisdom"
    ],
    "saving_throws": [
      "Strength",
      "Dexterity"
    ],
    "armor_prof": [],
    "weapon_prof": [
      "Simple",
      "Shortswords"
    ],
    "skills": [
      "Acrobatics",
      "Athletics",
      "History",
      "Insight",
      "Religion",
      "Stealth"
    ],
    "num_skills": 2,
    "equipment_options": [
      [
        "Shortsword",
        "Any simple weapon"
      ],
      [
        "Dungeoneer's pack",
        "Explorer's pack"
      ],
      [
        "10 darts"
      ]
    ],
    "features": [
      "Unarmored Defense (10 + Dex + Wis)",
      "Martial Arts (1d4)"
    ]
  }
}
