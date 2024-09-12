# ESM_assignment

## Getting started

To set up a conda environment for the toy models, run

    conda env create -f environment.yaml

## Exercise questions

### Exercise 1. City-scale dispatch problem

Assume we are modelling for city A that has gas power plants with fixed total capacity. To meet the electricity demand of the city, the gas power plant and some renewable energy plants are in use.

**Step 1**. Run model 1 as it is.
1. What is the electricity shadow price, and how is that set?

**Step 2**. Run model 1 and reduce the gas power plant capacity to 2 GW.
1. What happens to the shadow price now? Why is it?
2. What have you observed regarding the operation curve of wind and solar?

### Exercise 2. Intercountry capacity expansion problem

Assume we are modelling three countries: Germany, Switzerland and Italy. Each country has certain amount of available land for renewables with different capacity factors.

**Step 1.** Run model 2 in a "plan then operate" mode and calculate the nodal shadow prices.
1. Are they different? Why / why not?

**Step 2.** Change one parameter in the model or add one technology at one specific node to make the nodal shadow prices equivalent to each other.
1. What did you do? Why would that work?
2. Can you think of at least 3 ways to make it happen?
3. Which one of them are the best in a real-world case, in your opinion, and why?
