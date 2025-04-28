# Slowly Changing Dimensions:
-   Type 0: (Fixed) Attributes that never change. Example: Date of Birth.
-   Type 1: (Overwrite) Overwrites old data with new data. No historical tracking1.  Example: current status
-   Type 2: (Add new records) Adds a new row for each change, preserving historical data. Is one table, with history  tracking. Old records have start and end dates. Latest record has null end date.
-   Type 3: (Add new attribute) Adds new columns to store previous values. Like Type 2, but we add  attribute columns to keep the prior records value, of the attribute changed.
-   Type 4: (History Table) Uses a history table to keep track of changes. Main table has the current records. History table tracks the changes
-   Type 6: (Hybrid) Combines methods from Types 1, 2, and 3 for more complex scenarios.

