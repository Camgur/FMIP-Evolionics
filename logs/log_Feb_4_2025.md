
---
# Feb 4th, 2025
---


# Atomic Simulation and Material Design

## ASE (Atomic simulation environment) Module
- Provides atomic simulation capabilities with DFT relaxation and other prediction features
- Implements a plug and play model architecture featuring 4 different models, including ORB

## Materials Development
- Utilizes genetic algorithms for new materials development
- Implements benchmarking across 8 different materials
- Leverages the Materials Project database which contains:
  - Crystal structures with coordinate information (DFT-based)
  - Charge density data (DFT-based)
  - Energy predictions (DFT-based)
  - Specialized focus on solid state batteries

## Doping Process
- Involves introducing ions of different species into the material
- Commonly uses germanium and aluminum as dopants
- Concentration levels are critical for effectiveness
- Primary materials include ceramics and sulphides
- Uses .cif files (crystallography information files) for structure data

## Diffusivity Analysis
- Measures the speed of lithium movement through structures
- Process flow:
  1. Initial structure input (may include doping specifications)
  2. Temperature application
  3. Heatbath maintenance
  4. Conductivity measurement
- Produces trajectory files with linear regression output for diffusion coefficient calculation

## Genetic Algorithm Implementation
- Proposed goal: Optimize doping prediction through genetic algorithm
- Process would involve:
  1. Lithium input
  2. Test execution
  3. Iteration for local optimum finding

## NMR and DFT Analysis
- Uses chemical shift prediction for material environment assignment
- DFT (Density Functional Theory) implementation includes:
  - Pseudo-potential modeling of core electrons
  - Valence electron phenomenon analysis
  - Exchange correlation function for electron-electron interaction
  - Ground state energy configuration determination

## MACE Implementation
*(Note: Further details not provided in original notes)*

## Availability for Uriel Garcilazo Cruz (GCU)
- Location: McMaster
- Days: Tuesday, Wednesday, Friday
- Hours: 
  - Morning: 9 AM - 12 PM
  - Afternoon: After 3 PM

## Action Items
- Complete Notice of Intent


# Original transcript
```
Concurrent model


Using ACE - a module that creates an atomic simulation environment
	features	DFT relaxation and other predictions
	Plug and play model
		4 different models
			ORB

Use genetic algorithms to develop new materials


8 materials for benchmarking 
The materials project offers many materials
	solid state bateries
		crystal structures in the database
			Coordinate information			DFT
			charge density					DFT
			Energy prediction				DFT


Doping is introducing an ion of a different species

Give some structure to determine the amount of doping needed to increase conductivity

ceramics
sulphides

.cif files
crystallography information 


germanium and aluminium are commonly used for doping but the concentration matters

Diffusivity is how fast lithium moves through a structure 

Inputs
	Initial structure (sometimes comes with the amount of doping) -> 


Goal could be if in the doping prediction we can use the genetic algorithm to input lithium to then run a test, and iterate to find a local optimum

A trajectory file is 
Takes the initial structure
	appplies temperature
	keeps it in a heatbath
	measure the conductivity of lithium

The output is a linear regresion that gives the 
Diffusion coefficient (how fast the lithium is moving through)



The technique used in NMR is predicting the chemical shift of the material (an intrinsic property of the material that allows to assign environments to the material).
This is ofren done with DFT (density functional theory). When trying to assess the energy of the system we use DFT, which breaks the prediction into parameters:

	Pseudo-potential: Non-real image of what the core electron looks like
	Valence electron phenomenon
	Exchange correlation function, which governs electron-electron interaction
			||
			v
		Find energy via ground state (lowest energy configuration)

MACE 


##########################################################################################

Availability:
	Uriel is in McMaster on Tuesdays, Wednesdays and Fridays. Available in the mornings from 9 am to 12 pm and in the afternoons after 3 pm.


TODOS:
	Notice of Intent

```