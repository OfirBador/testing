import subprocess

workflow_name = "your-workflow-name"

subprocess.run(["gh", "workflow", "run", test1.yml], check=True)
