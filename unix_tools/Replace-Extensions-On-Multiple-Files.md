# Replace Words
`find Large -name "*.old_extension" -exec sh -c 'mv "$1" "${1%.old_extension}.new_extension"' _ {} \;`
