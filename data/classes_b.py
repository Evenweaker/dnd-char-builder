# Auto-split for upload
CLASSES_B = {
  "Paladin": {
    "hit_die": 10,
    "primary": ["Strength", "Charisma"],
    "saving_throws": ["Wisdom", "Charisma"],
    "armor_prof": ["All", "Shields"],
    "weapon_prof": ["Simple", "Martial"],
    "skills": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
    "num_skills": 2,
    "equipment_options": [
      ["Martial weapon + shield", "Two martial weapons"],
      ["Five javelins", "Any simple melee weapon"],
      ["Priest's pack", "Explorer's pack"],
      ["Chain mail", "Holy symbol"]
    ],
    "features": ["Divine Sense", "Lay on Hands (5 × level HP pool)"]
  },
  "Ranger": {
    "hit_die": 10,
    "primary": ["Dexterity", "Wisdom"],
    "saving_throws": ["Strength", "Dexterity"],
    "armor_prof": ["Light", "Medium", "Shields"],
    "weapon_prof": ["Simple", "Martial"],
    "skills": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
    "num_skills": 3,
    "equipment_options": [
      ["Scale mail", "Leather armor"],
      ["Two shortswords", "Two simple melee weapons"],
      ["Dungeoneer's pack", "Explorer's pack"],
      ["Longbow + 20 arrows"]
    ],
    "features": ["Favored Enemy", "Natural Explorer"]
  },
  "Rogue": {
    "hit_die": 8,
    "primary": ["Dexterity"],
    "saving_throws": ["Dexterity", "Intelligence"],
    "armor_prof": ["Light"],
    "weapon_prof": ["Simple", "Hand Crossbow", "Longsword", "Rapier", "Shortsword"],
    "skills": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
    "num_skills": 4,
    "equipment_options": [
      ["Rapier", "Shortsword"],
      ["Shortbow + 20 arrows", "Shortsword"],
      ["Burglar's pack", "Dungeoneer's pack", "Explorer's pack"],
      ["Leather armor", "Two daggers", "Thieves' tools"]
    ],
    "features": ["Expertise", "Sneak Attack (1d6)", "Thieves' Cant"]
  },
  "Sorcerer": {
    "hit_die": 6,
    "primary": ["Charisma"],
    "saving_throws": ["Constitution", "Charisma"],
    "armor_prof": [],
    "weapon_prof": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"],
    "skills": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
    "num_skills": 2,
    "equipment_options": [
      ["Light crossbow + 20 bolts", "Any simple weapon"],
      ["Component pouch", "Arcane focus"],
      ["Dungeoneer's pack", "Explorer's pack"],
      ["Two daggers"]
    ],
    "features": ["Spellcasting (Sorcerer)", "Sorcerous Origin (choose origin)"]
  },
  "Warlock": {
    "hit_die": 8,
    "primary": ["Charisma"],
    "saving_throws": ["Wisdom", "Charisma"],
    "armor_prof": ["Light"],
    "weapon_prof": ["Simple"],
    "skills": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
    "num_skills": 2,
    "equipment_options": [
      ["Light crossbow + 20 bolts", "Any simple weapon"],
      ["Component pouch", "Arcane focus"],
      ["Scholar's pack", "Dungeoneer's pack"],
      ["Leather armor", "Any simple weapon", "Two daggers"]
    ],
    "features": ["Otherworldly Patron (choose patron)", "Pact Magic"]
  },
  "Wizard": {
    "hit_die": 6,
    "primary": ["Intelligence"],
    "saving_throws": ["Intelligence", "Wisdom"],
    "armor_prof": [],
    "weapon_prof": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"],
    "skills": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
    "num_skills": 2,
    "equipment_options": [
      ["Quarterstaff", "Dagger"],
      ["Component pouch", "Arcane focus"],
      ["Scholar's pack", "Explorer's pack"],
      ["Spellbook"]
    ],
    "features": ["Spellcasting (Wizard)", "Arcane Recovery"]
  }
}
