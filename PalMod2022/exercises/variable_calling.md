variable calling
================

Runscript: `workshops/runscripts/fesom_runscript.yaml`

Invoke a nested variable
------------------------

In your FESOM runscript:

1. Define the following under the `general` section:
   ``` yaml
   general:
       foo1:
           foo2:
               foo3: bar
           foo4: [1, 2, 3]
   ```
2. Retreive the `foo4` value under a `new_variable` nested under the `fesom` section.
3. Run `esm_runscripts` in check mode, and check that your `new_variable` contains the `[1, 2, 3]` list.

<details>
  <summary>Solution</summary>
  
  ``` yaml
  general:
      foo1:
          foo2:
              foo3: bar
          foo4: [1, 2, 3]
  fesom:
      new_variable: ${general.foo1.foo4}
  ```
</details>