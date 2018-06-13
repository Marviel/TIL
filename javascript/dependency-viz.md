# Javascript Dependency Visualization

## Motivation
Sometimes, you find yourself wanting to visualize the dependencies of a given javascript file.

This can be tremendously useful when:
- You first start working on a library with which you are unfamiliar
- You return to a file that you wrote a long time ago
- You're trying to debug a problem in a complex codebase

## Method
It's actually pretty straightforward to get a graph of javascript dependencies.
1. install both [Madge](https://github.com/pahen/madge) and graphviz (as described in the madge install steps)
2. run `madge --image graph.svg path/to/your/file`
3. open graph.svg with your favorite svg viewer!
