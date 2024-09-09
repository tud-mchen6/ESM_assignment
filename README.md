# ESM_assignment

## Getting started

To set up a conda environment for the toy models, run

    conda env create -f environment.yaml

## Exercise questions

### Exercise 1. City-scale dispatch problem

Assume we are modelling for city A that has gas power plants with a fixed total capacity. To meet the electricity demand of the city, the gas power plant is in use, and we can choose to add some renewable energy sources.

**Step 1**. Run model 1 as it is.
1. How has the model decided for the capacity of renewables?
2. What is the price of electricity, and who sets it?

**Step 2**. Run model 1 and reduce the gas power plant capacity to 2 GW.
1. What happens to the electricity price now? Why is it?
2. What have you observed regarding the operation curve of wind and solar?

**Step 3**. Run model 1 without fixed gas power plant capacity.
1. What happens to the system capacity? Why?

**Step 4**. Run model 1 without fixed gas power plant capacity, and decrease the investment cost of onshore wind by 50%.
1. What has changed compared to step 3? Why?

### Exercise 2. Intercountry capacity expansion problem

Assume we are modelling three countries: Germany, Switzerland and Italy. Each country has certain amount of available land for renewables with different capacity factors.

**Step 1.** Run model 2 as it is and calculate the nodal electricity prices.
1. Why are they different?

**Step 2.** Change one parameter in the model or add one technology at one specific node to make the nodal prices equivalent to each other.
1. What did you do? Why would that work?
2. Can you think of at least 3 ways to make it happen?
3. Which one of them are the best in a real-world case, in your opinion, and why?
