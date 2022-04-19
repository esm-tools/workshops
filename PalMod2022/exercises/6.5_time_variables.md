Feature time variables
======================

Runscript: `workshops/runscripts/fesom_runscript.yaml`

Change the total experiment length and restart frequency
--------------------------------------------------------

1. In your FESOM runscript, change the total experiment length to 15 days (from `2001-01-01` until `2001-01-16`),
   and the frecuency of the restarts to daily, instead of monthly.

2. Remember that you'll also need to indicate to FESOM a daily `restart_unit` (`d`), as the different models
   control their calendars in different ways. In this case, FESOM namelist is modified through the `fesom-2.1.yaml`
   by using the `restart_unit` variable (note that ESM-Tools knows nothing about this variable, not a feature
   variable, but instead has an effect through the configuration file).

3. Use `esm_runscripts` to run a simulation and check that the experiment folder contains the correct `run_` 
   subfolders, `restart` files, and `outdata`.

<details>
  <summary>Solution</summary>
  
  ``` yaml
  general:
      initial_date: '2001-01-01'
      final_date: '2001-01-16'
      nmonth: 0
      nday: 1
  fesom:
      restart_unit: 'd'
  ```
</details>