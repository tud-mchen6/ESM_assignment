from pathlib import Path
import calliope

name_model = "model_1"
path_inputs = Path(__file__).parent.parent / name_model / "input" / "model.yaml"
path_results = Path(__file__).parent.parent / name_model / "results" / "results.nc"

print("Reading model from path: ", path_inputs)
model = calliope.Model(path_inputs)

print("Building model")
model.build()

print("Solving model")
model.solve()

print("Solving model again in operate mode")
model.build(force=True, mode="operate", operate_use_cap_results=True)

print("Writing results to path: ", path_results)
model.to_netcdf(path_results)
