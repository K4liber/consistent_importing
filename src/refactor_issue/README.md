Try to move (use option `Refactor` on VSCode) `EntityA` from `/examples/refactor_issue/package_1_lvl_1/package_1_lvl_2/module_a.py` to `/examples/refactor_issue/package_2_lvl_1/package_1_lvl_2/module_b.py`.

It will mess up the imports in init files since VSCode does not know about your imports strategy.
