namelist_changes
================

Runscript: `workshops/runscripts/fesom_runscript.yaml`

Use namelist_changes syntax
---------------------------

In your FESOM runscript, use the `namelist_changes` syntax to change the `ClimateDataPath` of the FESOM namelist
`namelist.config`

1. Open the default `esm_tools/namelists/fesom2/2.1/namelist.config` and check the name of the section where
   `ClimateDataPath` is.
2. Open your runscript and add the `namelist_changes` syntax necessary to change `ClimateDataPath` to an arbitrary
   path.
3. Run `esm_runscripts` in check mode, and check that the namelist changes made it to the namelist in the work
   directory: `<base_dir>/<exp_id>/run_DDMMYYY-DDMMYYYY/work/namelist.config`

<details>
  <summary>Solution</summary>
  
  ```
  fesom:
      namelist_changes:
          namelist.config:
              paths:
                  ClimateDataPath: "/my/arbitrary/path/"
  ```
</details>

Used default namelist_changes configurations
--------------------------------------------

1. Open the `fesom-2.1.yaml` configuration file and look for the `namelist_changes` (ignore for now
   `add_namelist_changes`).
2. By looking at that default `namelist_changes`, can you come up with an idea on how to change the
   `ClimateDataPath` for the experiment, just by editing your runscript, without using `namelist_changes` there?
   
<details>
  <summary>Solution</summary>
  
  ```
  fesom:
      climate_data_dir: "/my/arbitrary/path/"
  ```
</details>
