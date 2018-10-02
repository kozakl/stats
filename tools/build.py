import os

def main() :
	
    command = "java -jar compiler.jar --language_in=ECMASCRIPT5 --compilation_level SIMPLE_OPTIMIZATIONS"
    command += " --js ../Build/Stats.js"
    command += " --js_output_file ../Build/Stats.min.js"
    os.system(command)
    
if __name__ == "__main__":
    main()
