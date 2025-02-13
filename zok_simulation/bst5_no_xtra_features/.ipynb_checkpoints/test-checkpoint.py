import subprocess
import time
import os
import json

# Path to the directory containing ZoKrates programs
# program_directory = "./program"
program_directory = "./programs"
top_directory = "."

# Function to get the size of a file
def get_file_size(file_path):
    return os.path.getsize(file_path)

# Function to measure compilation time
def compile_program(program_path):
    start_time = time.time()
    compile_output = subprocess.run(["zokrates", "compile", "-i", program_path])
    end_time = time.time()
    output_file_path = os.path.join(top_directory, 'out')
    circuit_size = get_file_size(output_file_path)
    return end_time - start_time, circuit_size

# Function to execute the program and measure execution time
def execute_program(program_path):
    # input_path = "./input/bst1_instr.txt"
    start_time = time.time()
    subprocess.run(["zokrates", "compute-witness", "-a", "1", "360000000000", "1", "17904759277", "1", "3538782045", "1", "12015863319", "1", "26528449019", "1", "16945937538", "1", "9634043612", "1", "6394043787", "1", "589797008", "0", "999990000000000", "1", "644571333962", "1", "360000000000", "1", "6918175829", "1", "1418539498", "1", "4620052733", "1", "10353721365", "1", "6501064149", "1", "9153195873", "1", "4689987108", "1", "236423250", "0", "999990000000000", "1", "249054329850", "1", "0", "1", "490000000000", "1", "54678236122", "1", "74011882458", "1", "0", "1", "359806000000", "1", "30677200000", "1", "21763384366", "1", "57810268622", "1", "10573126065", "0", "999990000000000", "1", "2679233570000", "1", "50000000000", "1", "0", "1", "440000000000", "1", "256477272727", "1", "142574254605", "0", "35000000000", "1", "475000000000", "1", "272500000000", "0", "6346310419", "0", "3704631137", "1", "21493877604", "0", "999990000000000", "1", "11285000000000", "1", "360000000000", "0", "92623288862", "1", "18127037545", "0", "132460984911", "0", "60448929450", "0", "91192279514", "0", "2845884242", "0", "6548771326", "1", "3021172924", "0", "999990000000000", "0", "3334438399019", "1", "490000000000", "1", "247551020408", "1", "142463893265", "0", "60000000000", "1", "475000000000", "1", "250000000000", "0", "6099512120", "0", "2899719196", "1", "20351984752", "0", "999990000000000", "1", "12130000000000", "1", "10000000000", "1", "480000000000", "1", "300104166667", "1", "116698782940", "0", "70000000000", "1", "490000000000", "1", "317500000000", "0", "7510367051", "1", "14443085095", "1", "16844018436", "0", "999990000000000", "1", "14405000000000", "1", "160000000000", "1", "330000000000", "1", "102342129394", "1", "192526501837", "0", "329684000000", "1", "677689000000", "1", "45608600000", "1", "9881252514", "1", "24641335044", "1", "33514562149", "0", "999990000000000", "1", "3377290270000", "1", "0", "1", "0", "1", "490000000000", "1", "4846938776", "1", "12304149699", "0", "40000000000", "1", "36875000000", "1", "3125000000", "0", "3305014804", "1", "33092881158", "1", "1757735671", "0", "999990000000000", "1", "237500000000", "1", "0", "1", "180000000000", "1", "0", "1", "310000000000", "1", "139677419355", "1", "108558244611", "0", "255000000000", "1", "240000000000", "1", "160000000000", "0", "31488771247", "1", "99622837122", "1", "19497636311", "0", "999990000000000", "1", "4330000000000", "1", "410000000000", "1", "256707317073", "1", "146183146071", "0", "80000000000", "1", "490000000000", "1", "280000000000", "0", "6954836163", "0", "1113667812", "1", "22829971847", "0", "999990000000000", "1", "10525000000000", "1", "490000000000", "1", "305918367347", "1", "173276253030", "1", "10000000000", "1", "590000000000", "1", "300000000000", "1", "4862811", "0", "11977069957", "1", "24753750433", "0", "999990000000000", "1", "14990000000000", "1", "0", "1", "0", "1", "490000000000", "1", "9488776939", "1", "1461550223", "1", "2083330000", "1", "10350000000", "1", "9916670000", "0", "38679929838", "1", "157251657158", "1", "208792889", "0", "999990000000000", "1", "464950070000", "1", "160000000000", "1", "330000000000", "1", "78715069091", "1", "88073229229", "1", "2377830000", "1", "359806000000", "1", "42023800000", "1", "16887374731", "1", "25474914074", "1", "15331581297", "0", "999990000000000", "1", "2597597280000", "1", "460000000000", "1", "9238404348", "1", "2485120320", "1", "0", "1", "10000000000", "1", "9997825000", "0", "35573607045", "1", "113464572754", "1", "366411001", "0", "999990000000000", "1", "424966600000", "1", "0", "1", "140000000000", "1", "20000000000", "1", "0", "1", "0", "1", "0", "1", "70000000000", "1", "0", "1", "30000000000", "1", "150000000000", "1", "0", "1", "0", "1", "80000000000"])
    return time.time() - start_time

# Function to generate proof and extract proof size and number of constraints
def generate_proof(program_path):
    subprocess.run(["zokrates", "setup"])
    subprocess.run(["zokrates", "export-verifier"])
    start_time = time.time()
    proof_output = subprocess.run(["zokrates", "generate-proof"])
    end_time = time.time()
    # Example of extracting proof size and constraints from the output
    # This depends on the format of the output from ZoKrates
    output_file_path = os.path.join(top_directory, 'proof.json')
    proof_size = get_file_size(output_file_path)
    
    return proof_size

def verify_proof(program_path):
    start_time = time.time()
    subprocess.run(["zokrates", "verify"])
    end_time = time.time()
    
    return end_time - start_time


# Main function to batch test ZoKrates programs
def batch_test_zokrates_programs():
    results = []

    for program in os.listdir(program_directory):
        # Skip hidden files and directories
        if program.startswith('.') or os.path.isdir(os.path.join(program_directory, program)):
            continue

        program_path = os.path.join(program_directory, program)
        compile_time, circuit_size = compile_program(program_path)
        execution_time = execute_program(program_path)
        proof_size = generate_proof(program_path)
        verification_time = verify_proof(program_path)

        results.append({
            "program": program,
            "compile_time": compile_time,
            "circuit_size": circuit_size,
            "execution_time": execution_time,
            "proof_size": proof_size,
            "verification_time": verification_time
        })

    # Write results to a JSON file
    with open('zokrates_test_results.json', 'w') as file:
        json.dump(results, file, indent=4)

batch_test_zokrates_programs()