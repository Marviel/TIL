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
