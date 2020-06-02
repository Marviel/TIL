export function switchReturn<S, T>(value: S, mapping: Array<[(val: S) => boolean, T]>,  defaultCase: T): T {
    // Go through all our cases, and determine if any of them fit.
    for (const item of mapping) {
        if (item[0](value)) {
            return item[1];
        }
    }

    // If we don't find anything, the last case is our default.
    return defaultCase;
}

// Gets an object which contains the elements of the given array, keyed on a property given by a selector function.
export function objectKeyedOnArrayProperty<T>(arr: T[] , propertyGetter: (inputObj: T) => number): {[key: number]: T} {
    return arr.reduce((acc: any, item) => {
        acc[propertyGetter(item)] = item;
        return acc;
    }, {});
}
