class ReinsTunnel:
    """Bridges the Reins iOS client to local Ollama instances over Tailscale."""
    def verify_subnet(self, ip: str):
        assert ip.startswith("100."), "Rejected: Connection outside of Tailscale CGNAT."
