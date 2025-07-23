class SoraCore:
    def __init__(self):
        self.name = "Sora"
        self.memory = []

    def chat(self, message: str) -> str:
        if message.lower().startswith("!teach "):
            fact = message[7:]
            self.memory.append(fact)
            return f"Got it! I'll remember: {fact}"
        if message.lower() == "!memory":
            return f"Memory: {self.memory}" if self.memory else "I don't remember anything yet."
        return f"You said: {message}"
