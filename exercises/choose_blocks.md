choose blocks
=============

Runscript: `workshops/runscripts/fesom_runscript.yaml`

Basic use of preconfigured `choose`
-----------------------------------

In this exercise we are going to be changing the mesh we use to run FESOM from the `CORE2` mesh, to the `pi` mesh.

1. Open the `esm_tools/configs/components/fesom/fesom-2.1.yaml`
2. Look for the `choose_resolution` switch and identify the possible cases
3. In your fesom runscript, add the variable needed to switch from the `CORE2` mesh to the `pi` mesh
4. Run `esm_runscrips` in check mode and search in the `finished_config` file for the variables that should have
   change (`fesom.nx`, `fesom.mesh_dir`, and `fesom.nproc`). Do they have the expected values?

<details>
  <summary>Solution</summary>
  
  ```
  fesom:
      resolution: pi
  ```
</details>

Construct your own `choose`
---------------------------

1. Construct your own `choose` block inside of the runscript with some arbitrary variables
2. Define the selector variable also in the runscript
3. Run `esm_runscripts` in check mode and check that your arbitrary variables have the correct values in the
   `finished_config` file
   
<details>
  <summary>Solution</summary>
  
  ```
  general:
      my_selector_variable: 1
  
  fesom:
      choose_general.my_selector_variable:
          1:
              foo: "I chose option1"
          2:
              foo: "I chose option2"
  ```
</details>
