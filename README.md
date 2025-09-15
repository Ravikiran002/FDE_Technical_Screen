# FDE_Technical_Screen
Python solution for classifying packages into STANDARD, SPECIAL, or REJECTED stacks based on volume and mass, as part of the FDE technical screen challenge.


This project classifies packages into STANDARD, SPECIAL, or REJECTED stacks based on their dimensions and mass.

* Problem Rules
  - Bulky: volume ≥ 1,000,000 cm3(cubic centimeters) OR any dimension ≥ 150 cm  
  - Heavy: mass ≥ 20 kg  
* Stacks:
  - STANDARD: not bulky and not heavy  
  - SPECIAL: either bulky or heavy  
  - REJECTED: both bulky and heavy 
