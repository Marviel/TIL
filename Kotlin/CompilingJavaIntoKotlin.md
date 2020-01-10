# Compiling Java Into Kotlin

1. Gather all Java files you care about:

```bash
find "[SRC_DIR]" -name "*.java" > JAVA_SOURCES.txt
```
2. Compile the Java files: 

```bash
javac -d "[JAVA_CLASS_DESTINATION_DIR]" @JAVA_SOURCES.txt
```

3. Compile Kotlin: 
```bash
kotlinc -cp [JAVA_CLASS_DESTINATION_DIR] [KOTLIN_FILE]
```
