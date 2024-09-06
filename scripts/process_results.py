from pathlib import Path
import calliope
import matplotlib.pyplot as plt


def plot_stacked_bar(df, x, y, stack, color, destination):
    fig, ax = plt.subplots()
    df = df.pivot(index=x, columns=stack, values=y)
    df.plot.bar(stacked=True, ax=ax, color=color)
    ax.set_ylabel(y)
    plt.savefig(destination, bbox_inches="tight")


name_model = "model_1"
path_results = Path(__file__).parent.parent / name_model / "results" / "results.nc"
path_plots = Path(__file__).parent.parent / name_model / "plots"
model = calliope.read_netcdf(path_results)


def rename_transmission_techs(df, transmission_techs):
    return (
        df.replace({t: "transmission" for t in transmission_techs})
        .groupby(["nodes", "techs"])
        .sum()
        .reset_index()
    )


def separe_demand_electricity(df, demand_name="demand_electricity"):
    demand = df.loc[df["techs"] == demand_name]
    other = df.loc[df["techs"] != demand_name]
    return demand, other


flow_cap = (
    model.results.flow_cap.to_dataframe()
    .dropna()
    .reset_index()
    .drop(columns=["carriers"])
)
flow_out = (
    model.results.flow_out.to_dataframe()
    .dropna()
    .reset_index()
    .drop(columns=["carriers", "timesteps"])
    .groupby(["nodes", "techs"])
    .sum()
    .reset_index()
)

transmission_techs = list(
    model.inputs.techs.loc[model.inputs.base_tech == "transmission"].values
)
flow_cap = rename_transmission_techs(flow_cap, transmission_techs)
flow_out = rename_transmission_techs(flow_out, transmission_techs)

_, flow_cap_generation = separe_demand_electricity(flow_cap)
flow_out_demand, flow_out_generation = separe_demand_electricity(flow_out)

color = {
    "wind": "blue",
    "pv": "yellow",
    "gas_pp": "brown",
    "demand_electricity": "red",
    "transmission": "orange",
}

print("Saving plots to: ", path_plots)
plot_stacked_bar(
    flow_out_generation,
    x="nodes",
    y="flow_out",
    stack="techs",
    color=color,
    destination=path_plots / f"{name_model}_flow_out.png",
)
plot_stacked_bar(
    flow_cap_generation,
    x="nodes",
    y="flow_cap",
    stack="techs",
    color=color,
    destination=path_plots / f"{name_model}_flow_cap.png",
)
