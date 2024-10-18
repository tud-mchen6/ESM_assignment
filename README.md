# ESM_assignment

## Getting started

To set up a conda environment for the toy models, run the following command in the terminal.

    conda env create -f environment.yaml

Next, you can call calliope to solve the model, here for model 1.

    calliope run model_1/input/model.yaml --save_netcdf model_1/results/results.nc

To plot the results, run the following command. After a few moments, it will direct you to a web application where you can select different types of plots for your model results.

    calligraph ymodel_1/results/results.nc

## Exercise questions

### Exercise 1. City-scale dispatch problem

Assume we are modelling for city A that has gas power plants and a nuclear power plan with fixed total capacity. To meet the electricity demand of the city, the above-mentioned power plants and some renewable energy plants are in use.

**Step 1**. Run model 1 without any renewables capacity, then use calligraph to plot the results. Navigate to "Timeseries plots", and choose 'flow*' in the drop-down list of Variable. Then, at the bottom of the page, choose 'Original resolution'.
1. What do you observe when you look at the dispatch pattern of gas and nuclear power plants? How do their way of operation differ from each other?
2. Now, look at the electricity shadow price by selecting the variable 'shadow_price_system_boundary'. What do you observe? Can you explain why it behaves like this? You may want to have a look at the input data of the power plants in `techs.yaml`, which can help explain the values that the shadow price attains.

Now, take a moment to get acquainted with the model's input data in `model_1/input`. If you don't understand everything at first glance, that is ok. To play around and learn about the model, you will now start to change the model's input assumptions and learn how that alters the results, so it's good to know where you find what.

You will find the following directories and files: `model.yaml` is the central file, containing information on which calliope version to use, what temporal scope to select and where files containing specific data are located, among others. `techs.yaml` defines the properties of technologies that are used in the model. In our case, these are electricity demand, wind, pv, gas power plants, nuclear power plants and transmission lines. In `nodes.yaml`, we define the different locations of a model, which are nodes in a graph, and which technologies can exist in which node. In model_1, we only have 1 node - the city. Last, we have a directory `timeseries/` which contains timeseries data for electricity demand and capacity factors for wind and pv.

**Step 2**. Add 3 GW of onshore wind and 3 GW of solar in `model_1/input/nodes.yaml` by setting `flow_cap_min` and `flow_cap_max` both to 3. Run the model and plot the results again.
1. Look at the timeseries of the shadow price again. What do you observe? How can you explain it?
2. What can you observe regarding the operation of wind and solar?

### Exercise 2. Intercountry capacity expansion problem

Assume we are modelling three countries: Germany, Switzerland and Italy. Each country has certain amount of available land for renewables with different capacity factors.

**Step 1.** Run model 2 as it sits now and plot the nodal shadow prices.
1. Are they different? Why / why not?

**Step 2.** Change one parameter in the model or add one technology at one specific node to make the nodal shadow prices equivalent to each other.
1. What did you do? Why would that work?
2. Can you think of at least 3 ways to make it happen?
3. Which one of them are the best in a real-world case, in your opinion, and why?
