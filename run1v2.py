import os
import subprocess
import sys

def run_command(command, cwd=None):
    """Run a shell command and return the output"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        print(f"✅ Command succeeded: {command}")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    # 1. Clone the repository
    repo_url = "https://github.com/susan4y/1v2.git"
    print(f"Cloning repository: {repo_url}")
    
    if not run_command(f"git clone {repo_url}"):
        sys.exit(1)
    
    # 2. Move into the directory
    repo_dir = "1v2"  # Changed from "1" to "1v2"
    print(f"Changing directory to: {repo_dir}")
    
    # Check if directory exists
    if not os.path.exists(repo_dir):
        print(f"❌ Directory '{repo_dir}' not found after cloning")
        sys.exit(1)
    
    # 3. Make the file executable
    # Note: The file might be named differently in the new repo
    # Assuming it's still named "1", but could be different
    print("Making file '1' executable...")
    if not run_command("chmod +x 1", cwd=repo_dir):
        # If file "1" doesn't exist, check for other executable files
        print("⚠️ File '1' not found, checking for other executable files...")
        try:
            # List files in the directory
            files = os.listdir(repo_dir)
            print(f"Files in {repo_dir}: {files}")
            # Look for any executable file
            for file in files:
                file_path = os.path.join(repo_dir, file)
                if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                    print(f"Found executable: {file}")
                    print(f"Making {file} executable...")
                    if not run_command(f"chmod +x {file}", cwd=repo_dir):
                        sys.exit(1)
                    print(f"Running ./{file}...")
                    print("-" * 50)
                    if not run_command(f"./{file}", cwd=repo_dir):
                        sys.exit(1)
                    print("-" * 50)
                    return
        except Exception as e:
            print(f"Error checking files: {e}")
        sys.exit(1)
    
    # 4. Run the executable
    print("Running ./1...")
    print("-" * 50)
    if not run_command("./1", cwd=repo_dir):
        sys.exit(1)
    print("-" * 50)

if __name__ == "__main__":
    main()