"""Configuration utilities for the WebUI."""

def default_config():
    """Return default configuration settings."""
    return {
        "agent_type": "custom",
        "max_steps": 100,
        "max_actions_per_step": 10,
        "use_vision": True,
        "tool_calling_method": "auto",
        "llm_provider": "openai",
        "llm_model_name": "gpt-4",
        "llm_num_ctx": 32000,
        "llm_temperature": 1.0,
        "llm_base_url": "",
        "llm_api_key": "",
        "use_own_browser": False,
        "keep_browser_open": False,
        "headless": False,
        "disable_security": True,
        "enable_recording": True,
        "window_w": 1280,
        "window_h": 1100,
        "save_recording_path": "./tmp/record_videos",
        "save_trace_path": "./tmp/traces",
        "save_agent_history_path": "./tmp/agent_history",
        "task": "go to google.com and type 'OpenAI' click search and give me the first url",
    }