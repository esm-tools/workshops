environment_changes
===================

Runscript: `workshops/runscripts/fesom_runscript.yaml`

Change the runtime environment
------------------------------

In your FESOM runscript, use the `runtime_environment_changes` dictionary to select the `openmpi` configuration
and export the variable `PalModWS="test"`.

1. Open the default `esm_tools/configs/machines/mistral.yaml` and search for the variable that controls the MPI
   `choose_` block. You'll need to use that variable in your runscript to switch to the `openmpi` configuration.
2. Carry out the necessary modifications in your runscript.
3. Run `esm_runscripts` in check mode, and check that the `*.run` script
   (`<base_dir>/<exp_id>/run_DDMMYYY-DDMMYYYY/scripts/*.run`) contains the `openmpi` variables selected in the
   `choose_` block in the `mistral.yaml` and also the exported var `PalModWS="test"`

<details>
  <summary>Solution</summary>
  
  ``` yaml
  fesom:
      runtime_environment_changes:
          useMPI: openmpi
          add_export_vars:
              PalModWS: '"test"'
  ```
</details>