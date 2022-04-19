General Instructions for the Workshop Exercises
===============================================

- The runscript to be used in each exercise is stated at the top of each exercise, right below the title. Those
  runscripts are all available in the `PalMod/runscripts/` folder.
- Some times the exercise will tell you to add some variables to the runscript in this way:
  ``` yaml
  general:
      foo1: bar1
  fesom:
      foo2: bar2
  ```
  What we mean by that is that you need to add `foo1: bar1` and `foo2: bar` to the `general` and `fesom` sections of the
  existing runscript, and remember: you can place your variable wherever you want inside the correct section,
  just make sure it is well indented.
- Some times we use the dot-notation `.` to indicate nesting, i.e.: `fesom.climate_data_dir`. This can be written in the
  yaml file as:
  ``` yaml
  fesom:
      climate_data_dir: /my/path/
  ```
- Don't use tabs, the `pyyaml` package we use to parse the yaml files hates tabs...
- Most of the exercises have no effects to the models, and involve a lot of `foo`, `bar` and `cats`, however,
  after these exercises you'll have master all the ESM-Tools functionalities needed to implement or modify your
  new model/machine/coupled-system, and debug the ESM-Tools part.
