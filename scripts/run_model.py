from pathlib import Path
import calliope

name_model = "model_2"
path_inputs = Path(__file__).parent.parent / name_model / "input" / "model.yaml"
path_results = Path(__file__).parent.parent / name_model / "results" / "results.nc"

print("Reading model from path: ", path_inputs)
model = calliope.Model(path_inputs)

print("Running model")
model.run()

print("Results:")
print(model.results)

print("Writing results to path: ", path_results)
model.to_netcdf(path_results)
