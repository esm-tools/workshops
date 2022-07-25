File dictionaries
=================
Runscripts:
- AWI-CM3: `workshops/runscripts/awicm3-v3.1-ollie-TCO95L91-CORE2.yaml`
- AWI-ESM-2.1: `workshops/runscripts/awiesm-2.1-pi.yaml`

Excercise 1: Change the source of a forcing file
================================================
In this exercise we want to change the source from where an input file is copied into the experiment folder.

AWI-CM3
-------
Change the source of the OpenIFS `input` file `ICMSH_INIT` to a new path `/work/ollie/mandresm/workshop/forcings/awicm3/ICMSHaackINIT`,
and run `esm_runscripts` in check mode (`-c`).

Tips:
- You can open the `esm_tools/configs/components/oifs/oifs.yaml` file and search for `input_sources` for inspiration.
- Make sure that your changes have an effect by looking into the `*finished_config.yaml` of the experiment.

<details>
  <summary>Solution</summary>
  
  ``` yaml
  oifs:
      add_input_sources:
          ICMSH_INIT: "/work/ollie/mandresm/workshop/input/awicm3/ICMSHaackINIT"
  ```
</details>

AWI-ESM-2.1
===========
Change the source of the ECHAM `input` file `/work/ollie/mandresm/workshop/input/awiesm2/T63L47_jan_spec.nc`, and run
`esm_runscripts` in check mode (`-c`).

**Tips**:
- You can open the `esm_tools/configs/components/echam/echam.datasets.yaml` file and search for `input_sources` for inspiration.
- Make sure that your changes have an effect by looking into the `*finished_config.yaml` of the experiment.

<details>
  <summary>Solution</summary>
  
  ``` yaml
  echam:
      add_input_sources:
          janspec: "/work/ollie/mandresm/workshop/input/awiesm2/T63L47_jan_spec.nc"
  ```
</details>

Exercise 2: Add a new input file and rename it
==============================================
Add the file `cats_input.rst` located in `/work/ollie/mandresm/workshop/input/` as an `input` file into any of the models.
Make it so that when it's copied to the `work` folder the file is renamed to `lunas_input.rst`.

**Tips**:
- Check that the file is copied and renamed correctly in the `run_<DATE>/work` folder of your experiment.

<details>
  <summary>Solution</summary>
  
  ``` yaml
  echam/oifs:
    add_input_files:
        cats: cats
    add_input_sources:
        cats: "/work/ollie/mandresm/workshop/input/cats_input.rst"
    add_input_in_work:
        cats: "lunas_input.rst"
  ```
</details>
