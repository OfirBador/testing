import subprocess

workflow_name = "test1.yml"

subprocess.run(["gh", "workflow", "run", workflow_name], check=True)
