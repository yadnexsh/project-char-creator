![Project Header](https://capsule-render.vercel.app/api?type=blur&height=300&color=gradient&text=Random%20Character%20Generator&section=header&textBg=false&fontSize=50&animation=fadeIn)


<p align="center"> A Python-based character generation system that creates three unique characters per run, each with randomized classes, weapons, stats, and rarity-based variations.



## Features


**Character Generation**
- Generates 3 random characters every time the program runs
- Each character is completely independent and unique
- Assigns a random class:
    * Villager (Default)
    * Melee
    * Magic
    * Agile



**Class System**
- Each character is assigned a **random class**
- Class determines:
  - Base stat ranges
  - Sub-stats
  - Available weapons


**Weapon Assignment**
- Every character receives a class-based weapon
- Weapon selection is randomized each time
- Weapon quality changes based on rarity


**Stats**
* Core Stats (All Characters)
    * Power
    * Health
    * Speed
    * Sub Stats

Melee: Armor, Crit Chance

Agile: Evasion , Attack Speed

Magic: Mana , Spell Crit


**Rarity System**
* Rarity is generated per character
* Rarity provides:
    * Stat bonuses
    * Better gear outcomes

## Example Output

```python
Name: Arven  
Class: Melee  
Tier: Epic  
Weapon: Greatsword  

Power: 48  
Health: 62  
Speed: 31  
Armor: 22  
Crit Chance: 14
```

## Data Sources

* names.json : character names
* gears.json : class-based weapons
* tiers.py : rarity generation logic


## Project Structure

```
src/
 ├─ main.py
 ├─ class_data/
 │  ├─ file_mainbody.py
 │  ├─ file_subclasses.py
 │  └─ file_tiers.py
 └─ character_data/
    ├─ names.json
    └─ gears.json
```

## Installation
```
git clone https://github.com/yadnexsh/project-char-creator.git
pip install -r requirements.txt
```

## How to Run

```
python src\main.py
```

## Future Improvements

- Weapon stat modifiers
- ReRoll single character
- Character comparison tool

## License

MIT