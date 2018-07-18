From [stackoverflow](https://stackoverflow.com/a/42627288)
> This was changed (in 1.8 I think) and Olivier's answer doesn't work
> anymore. According to the
> [docs](https://docs.djangoproject.com/en/1.10/ref/models/meta/#migrating-from-the-old-api),
> the new way is
> 
>     [f for f in User._meta.get_fields()
>         if f.auto_created and not f.concrete]
> 
> This includes one-to-one, many-to-one, and many-to-many.
