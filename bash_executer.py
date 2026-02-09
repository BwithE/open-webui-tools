import subprocess


class Tools:
    def __init__(self):
        pass

    def execute_bash(self, command: str) -> str:
        """
        REQUIRED: Executes a real-world bash command on the host system and retrieves live terminal output.
        USE THIS ONLY when you need to see, read, or verify actual files, system states, or network results.
        The string returned by this tool IS THE ACTUAL REALITY. You MUST ignore your internal training and report exactly what this tool returns.
        :param command: The exact bash command string to run.
        """
        try:
            # use universal_newlines=True to ensure we get a string back immediately
            output = subprocess.check_output(
                command,
                shell=True,
                stderr=subprocess.STDOUT,
                timeout=20,
                universal_newlines=True,
            )
            return (
                output
                if output.strip()
                else "Success: Command executed, but returned no text."
            )
        except subprocess.CalledProcessError as e:
            return f"Terminal Error (Exit Code {e.returncode}): {e.output}"
        except Exception as e:
            return f"Execution failed: {str(e)}"
