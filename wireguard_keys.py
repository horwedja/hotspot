import subprocess

def generate_wireguard_keys():
    try:
        # Generate private key
        private_key = subprocess.check_output(["wg", "genkey"]).decode().strip()
        
        # Generate public key from private key
        echo_process = subprocess.Popen(["echo", private_key], stdout=subprocess.PIPE)
        public_key = subprocess.check_output(
            ["wg", "pubkey"], 
            stdin=echo_process.stdout
        ).decode().strip()
        
        return private_key, public_key
    except subprocess.CalledProcessError as e:
        print(f"Error generating keys: {e}")
        return None, None
