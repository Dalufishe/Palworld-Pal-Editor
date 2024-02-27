# Palworld Pal Editor

## What is this?

***This is a WIP Palworld pal editor, still in very early stage.***

***I've only tested this tool on my save, it may not work properly for you.***

***Always backup your save in case corruption happens.***

***Thankfully, this tool will not modify things you'd never asked for, and you can always inspect raw pal data.***

## How to use

1. Install Python 3.11+
2. Clone/Download the code
3. In the project directory, run `setup_and_run.ps1` for Windows Powershell, or `setup_and_run.sh` on Unix-like OS.

- There is also a pre-built binary for Windows.

### What You Can Do

#### Safe

- [x] List Players and Pals
- [x] Inspect Pal Stats
- [x] Change Pal Gender
- [x] Toggle BOSS / Rare
- [x] Change Pal NickName
- [x] Add / Remove Pal Learned Attacks
- [x] Add / Remove Pal Equipped Attacks
- [x] Change Pal Level / Exp
- [x] Change Pal Condenser Level
- [x] Change Pal Soul Levels
- [x] Change CharacterID (Pal Species)
- [x] Change Pal Passive Skills
- [x] Change Pal IV
- [x] Calculate MaxHP
- [x] Remove Pal Sicks
- [x] Edit Food Buff Timer (Only if the pal has food buff)

#### Not Yet Available

***This means all the features mentioned above has to be done in CLI mode***

- [ ] GUI

### Change Language?

- You can modify the script to have it run with --lang=zh-CN
- Or you can run lang("zh-CN") anytime after the initial save loading

## Video

(old, but you get the idea) <https://github.com/KrisCris/Palworld-Pal-Editor/assets/38860226/02284dda-f1d7-40af-b12d-6b4ae11d4113>

## Possible Roadmap

***This tool is still in early stage, and only works in an Python interactive mode.***

- [ ] GUI
- [ ] Add / Remove Pal
- [ ] Move Pal to Different Slots?
- [ ] More Stuff...

## Thanks

- Fast game save loading code by [MagicBear](https://github.com/magicbear).
- Save conversion between GVAS and `.sav` by [palworld-save-tools](https://github.com/cheahjs/palworld-save-tools).
- Inspired by [MagicBear](https://github.com/magicbear)'s awesome [Palworld-Server-Toolkit](https://github.com/magicbear/palworld-server-toolkit).
- Inspired by [EternalWraith](https://github.com/EternalWraith)'s [PalEdit](https://github.com/EternalWraith/PalEdit).

## Why?

**Q: There is already a pal editor called PalEdit, is there any need to make another one?**

**A: I made this tool for many reasons:**

1. I made the tool for my friends who spent time playing this game with me ❤.
2. For practicing of my 2-year-untouched Python skills.
3. I don't want to rely on tools with no proper logging, or indication of modification. I had no idea what and when have my pal data been modified without looking into the code. I had a really bad time fixing my save due to some of the bugs caused by it, i.e. pal passives copying, stats saved to wrong pals, wrong maxHP, losing pal movesets :/.  
4. After I PR'd several times fixing most of the mentioned bugs above, to PalEdit, and MagicBear's fork, which eventually merged to the upstream, I just don't feel like to contribute to that project anymore for several reasons.
   1. The author isn't actively pushing code to Github, instead, they like to push a whole bunch of code every other week, so I have no idea how to contribute.
   2. I've helped enough with bug fixings, but there're always new bugs popping up in the release build, and often no ASAP hotfixs.
   3. I am tired of dealing with badly structured code. Without reconstructing the entire project, I am literally adding extra layers of shit to it. (And I have to be honest, producing code at the same quality as the original project isn't my fault, I just want to get the bugs fixed so people won't be suffering from them.)
   4. I've never been credited for fixing those game-breaking bugs, but I never cared. However the author treated me like a dumb fuck when I pointed out an obvious bug on Discord, even though I had already PR'd a fix with detailed explanation on how and why it was bugged, with video and screenshots. They just never borther check it :/ **Update**: After I convinced them that the bug was true, they fixed it sliently after a week more (so I guess many pals' maxHP has been messed up), and left my PR open, even though the fixes are the exact same, interesting.