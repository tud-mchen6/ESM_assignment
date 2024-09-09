# ESM_assignment

## Getting started

To set up a conda environment for the toy models, run

    conda env create -f environment.yaml

## Exercise questions

### Exercise 1. City-scale dispatch problem

Assume we are modelling for city A that has gas power plants with a fixed total capacity. To meet the electricity demand of the city, the gas power plant is in use, and we can choose to add some renewable energy sources.

Step 1. Run model 1 as it is.
(1) How has the model decided for the capacity of renewables?
(2) What is the price of electricity, and who sets it?

Step 2. Run model 1 and reduce the gas power plant capacity to 2 GW.
(1) What happens to the electricity price now? Why is it?
(2) What have you observed regarding the operation curve of wind and solar?

Step 3. Run model 1 without changing the gas power plant capacity, but reduce wind and solar investment cost by 50%.
(1) What happens to the system capacity? Why?

### Exercise 2. Intercountry capacity expansion problem
