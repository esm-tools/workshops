add_ functionality
==================

Runscript: `workshops/runscripts/fesom_runscript.yaml`

add_ into a list
----------------

In your FESOM runscript, use the `add_` syntax to change add two arbitraty strings to as elements of the list
`wiso_fields`.

1. Open the `esm_tools/config/components/fesom/fesom-2.1.yaml` configuration file and look for the `wiso_fields`.
2. In your runscript, add two new strings to that list.
3. Run `esm_runscripts` in check mode, and check that the new elements made it into the `wiso_fields`, in the
   `finished_config.yaml` (`<base_dir>/<exp_id>/run_DDMMYYY-DDMMYYYY/config/*_finished_config.yaml`

<details>
  <summary>Solution</summary>
  
  ``` yaml
  fesom:
      add_wiso_fields:
          - str-1
          - str-2
  ```
</details>

add_ into a dictionary
----------------------

In your FESOM runscript, use the `add_` syntax to change the `steps_per_ib_step` inside the FESOM `namelist_config`, `iceberg section`.

1. In your runscript, set `icb_code` to `True` in the `fesom` section, to emmulate a run with FESOM-Icebergs.
2. Use the `add_` feature and the `namelist_changes` to change the `steps_per_ib_step` to `3` (you can look at the
   `fesom-2.1.yaml` to get information about the expected structure for this section of the namelist).
3. Run `esm_runscripts` in check mode, and check that the namelist changes made it into the namelist in the work
   directory: `<base_dir>/<exp_id>/run_DDMMYYY-DDMMYYYY/work/namelist.config`
4. Remove the `add_` from `add_namelist_changes` and run another check run. You'll notice that your changes didn't
   make it into the `<base_dir>/<exp_id>/run_DDMMYYY-DDMMYYYY/work/namelist.config`, because the `add_` was missing
   and the information in the `fesom-2.1.yaml` contained in the `choose_icb_code` won over that in the runscript.

<details>
  <summary>Solution</summary>
  
  ``` yaml
  fesom:
      icb_code:
      add_namelist_changes:
          namelist.config:
              icebergs:
                  steps_per_ib_step: 8
  ```
</details>
