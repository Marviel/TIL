# Pass in A Tuple, Produce An Object Keyed on Its Type

```typescript
function getObjectWithTheseKeys<T extends readonly (string)[]>(arr: T): {[K in T[number]]: boolean} {
    const m = arr.map((k) => {
        // TODO do stuff to get the value
        const theValue = true;
        
        return [k, true] as const
    });

    // We disable here because we know that we only got our keys from the original, 
    // so we're keeping the promise we made.
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    //@ts-ignore
    return Object.fromEntries(m);
}

// This should show "hi" and "wow" as the keys on the object
const x = getObjectWithTheseKeys(["hi", "wow"] as const);
```
