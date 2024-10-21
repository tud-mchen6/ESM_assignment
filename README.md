# `calliope-tutorial`

## Getting started

Follow these [installation instructions](https://github.com/sjpfenninger/optimisation-course/blob/main/README.md) to set up a Python environment with everything necessary installed.

Inside a Jupyter Notebook, you can run a model with these two lines of code - the `!` means execution of a tool outside of Python, and you could also run these two commands (without the `!` in a terminal or shell window if you prefer that):

```bash
!calliope run economic_dispatch/model.yaml --save_netcdf results_economic_dispatch.nc
!calligraph results_economic_dispatch.nc
```

## Exercise questions

### Exercise 1. City-scale dispatch problem

Assume we are modelling for city A that has gas power plants and a nuclear power plan with fixed total capacity. To meet the electricity demand of the city, the above-mentioned power plants and some renewable energy plants are in use.

**Step 1**. Run model 1 without any renewables capacity, then use calligraph to plot the results. Navigate to Timeseries plots, and choose 'flow*' in the drop-down list of Variable. Then, at the bottom of the page, choose 'Original resolution'.
1. What do you observe as the dispatch pattern between gas and nuclear power plants?
2. What is the electricity shadow price, and can you explain why it is at this value?

**Step 2**. Run model 1 and add 3 GW of onshore wind and 3 GW of solar in `model_1/input/nodes.yaml`. Plot the results again.
1. What happens to the shadow price now? Why is it?
2. What have you observed regarding the operation curves of wind and solar?

### Exercise 2. Intercountry capacity expansion problem

Assume we are modelling three countries: Germany, Switzerland and Italy. Each country has certain amount of available land for renewables with different capacity factors.

**Step 1.** Run model 2 as it sits now and plot the nodal shadow prices.
1. Are they different? Why / why not?

**Step 2.** Change one parameter in the model or add one technology at one specific node to make the nodal shadow prices equivalent to each other.
1. What did you do? Why would that work?
2. Can you think of at least 3 ways to make it happen?
3. Which one of them are the best in a real-world case, in your opinion, and why?
