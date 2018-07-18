Taken from [Stackoverflow](https://stackoverflow.com/questions/2233883/get-all-related-django-model-objects)
> ## Django <= 1.7
> 
> This gives you the property names for all related objects:
> 
>     links = [rel.get_accessor_name() for rel in a._meta.get_all_related_objects()]
> 
> You can then use something like this to get all related objects:
> 
>     for link in links:
>         objects = getattr(a, link).all()
>         for object in objects:
>             # do something with related object instance
> 
> I spent a while trying to figure this out so I could implement a kind
> of "Observer Pattern" on one of my models. Hope it's helpful.
> 
> ## Django 1.8+
> 
> Use `_meta.get_fields()`:
> https://docs.djangoproject.com/en/1.10/ref/models/meta/#django.db.models.options.Options.get_fields
> (see reverse in the `_get_fields()` source also)
