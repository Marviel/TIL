If you have an object with simple properties (int, str, dict, etc) the below function (once you give it some TLC and fix the typing issues) should allow you to load things dynamically from localstorage.

Once you write the syncSettingsToLocalStorage, in a similar fashion, you should be able to use these in conjunction.

```javascript
    loadSettingsFromLocalStorage() {
        // Go through everything in our settings model, and see if it is cached in our
        // local storage.
        const currentSettings: any = this.settingsModel;
        Object.keys(currentSettings).forEach((key) => {
            const storageName = `${LOCALSTORAGE_PREFIX}:${key}`;

            if (localStorage) {
                const lsValue = localStorage.getItem(storageName);
                if (lsValue) {
                    currentSettings[key] = lsValue;
                    return JSON.parse(lsValue) === true;
                }
            }
        });
    }

    syncSettingsToLocalStorage() {
        // TODO
    }
```

The better appproach to all of this would probably be a `mobx` style variable decorator (in TS), which would allow you to add a getter/setter method which checked the localstorage for the same value, if it exists, and get that if it does.
