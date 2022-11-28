### Show where data directory is:
Enter psql console, then:

    show data_directory;

### Show run_time parameters:
Enter psql console, then:

    show all;

## Datatypes
### `typed_uuid`
UUIDs are very useful because they can be generated quickly, and are very unlikely to collide with eachother.

One issue with UUIDs is that they do not quickly tell you what type of object they are associated with. In many contexts, it can be helpful to see what type of object an id refers to.

Enter: The typed uuid. It looks like a usual UUID, but it has a prefix added to its beginning.
- `example_4aee3613-4f08-4994-a3ac-fadb9a1f9a4d`

The following code will add typed_uuid functionality to your postgres database:
```sql
CREATE DOMAIN typed_uuid AS 
   VARCHAR CHECK ((VALUE IS NULL) OR (split_part(value,'|', 2)::uuid IS NOT NULL));

CREATE OR REPLACE FUNCTION public.generate_typed_uuid(type_name text)
 RETURNS text
 LANGUAGE plpgsql
 STABLE
AS $function$	
	BEGIN
        IF type_name IS NULL THEN
            RAISE EXCEPTION 'generate_typed_uuid must have a type_name passed to it.';
        ELSE
            RETURN type_name || '|' || uuid_generate_v4();
        END IF;     
	END;                  
$function$
;
```

And you can use it like:

```sql
CREATE TABLE example (
    # You can now create new entries in the example table, and they'll automatically have `example_UUID` ids attached to them :)
    id typed_uuid PRIMARY KEY DEFAULT (generate_typed_uuid('example'))
);
```
