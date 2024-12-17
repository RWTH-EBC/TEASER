from setuptools import setup


# read the contents of your README file
from pathlib import Path

readme_path = Path(__file__).parent.joinpath("README.md")
with open(readme_path, "r", encoding="utf-8") as file:
    long_description = file.read()

with open(Path(__file__).parent.joinpath("teaser", "__init__.py"), "r") as file:
    for line in file.readlines():
        if line.startswith("__version__"):
            VERSION = line.replace("__version__", "").split("=")[1].strip().replace("'", "").replace('"', '')

setup(
    name="teaser",
    version=VERSION,
    description="Tool for Energy Analysis and Simulation for " "Efficient Retrofit ",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/RWTH-EBC/TEASER",
    download_url=f'https://github.com/RWTH-EBC/TEASER/archive/refs/tags/{VERSION}.tar.gz',
    author="RWTH Aachen University, E.ON Energy Research Center, "
           "Institute of Energy Efficient Buildings and Indoor Climate",
    author_email="ebc-teaser@eonerc.rwth-aachen.de",
    license="MIT",
    packages=[
        "teaser",
        "teaser.logic",
        "teaser.logic.archetypebuildings",
        "teaser.logic.archetypebuildings.tabula",
        "teaser.logic.archetypebuildings.tabula.de",
        "teaser.logic.archetypebuildings.tabula.dk",
        "teaser.logic.archetypebuildings.bmvbs",
        "teaser.logic.archetypebuildings.bmvbs.custom",
        "teaser.logic.archetypebuildings.urbanrenet",
        "teaser.logic.buildingobjects",
        "teaser.logic.buildingobjects.buildingphysics",
        "teaser.logic.buildingobjects.buildingsystems",
        "teaser.logic.buildingobjects.calculation",
        "teaser.logic.simulation",
        "teaser.data",
        "teaser.data.input",
        "teaser.data.input.inputdata",
        "teaser.data.input.inputdata.weatherdata",
        "teaser.data.output",
        "teaser.data.output.modelicatemplate",
        "teaser.data.output.reports",
        "teaser.data.output.modelicatemplate.AixLib",
        "teaser.data.output.modelicatemplate.BESMod",
        "teaser.data.output.modelicatemplate.IBPSA",
        "teaser.examples",
        "teaser.examples.verification",
        "teaser.examples.examplefiles",
    ],
    package_data={
        "teaser.data.input.inputdata": ["*.json"],
        "teaser.data.input.inputdata.weatherdata": [
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos",
            "ASHRAE140.mos",
        ],
        "teaser.data.output.modelicatemplate": [
            "package",
            "package_order",
            "conversion",
            "modelica_language",
            "modelica_test_script",
        ],
        "teaser.data.output.modelicatemplate.AixLib": [
            "AixLib_Multizone",
            "AixLib_ThermalZoneRecord_OneElement",
            "AixLib_ThermalZoneRecord_TwoElement",
            "AixLib_ThermalZoneRecord_ThreeElement",
            "AixLib_ThermalZoneRecord_FourElement",
        ],
        "teaser.data.output.modelicatemplate.BESMod": [
            "Building",
            "Example_GasBoilerBuildingOnly",
            "Example_HeatPumpMonoenergetic",
            "Example_TEASERHeatLoadCalculation",
            "Script_GasBoilerBuildingOnly",
            "Script_HeatPumpMonoenergetic",
            "Script_TEASERHeatLoadCalculation",
        ],
        "teaser.data.output.modelicatemplate.IBPSA": [
            "IBPSA_OneElement",
            "IBPSA_TwoElements",
            "IBPSA_ThreeElements",
            "IBPSA_FourElements",
        ],
        "teaser.data.output.texttemplate": [
            "ReadableBuilding_OneElement",
            "ReadableBuilding_TwoElement",
            "ReadableBuilding_ThreeElement",
            "ReadableBuilding_FourElement",
        ],
        "teaser.examples.examplefiles": ["*.json"],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    install_requires=["mako", "pytest", "pandas", "numpy"],
    extras_require={"report": ["plotly"]}
)
