"""Neural Oscillation Detector Tool for analyzing brain wave patterns and oscillatory activity."""

from typing import Dict, List, Optional, Any
import numpy as np
from pydantic import BaseModel, Field
from neuroagent.tools.base_tool import BaseTool


class OscillationAnalysisInput(BaseModel):
    """Input schema for oscillation analysis."""
    brain_region: str = Field(description="Brain region to analyze (e.g., hippocampus, cortex, thalamus)")
    frequency_band: str = Field(default="all", description="Frequency band: delta, theta, alpha, beta, gamma, or all")
    recording_type: str = Field(default="LFP", description="Recording type: LFP, EEG, or spike_train")
    duration_seconds: float = Field(default=60.0, description="Duration of recording to analyze")


class NeuralOscillationDetectorTool(BaseTool):
    """Tool for detecting and analyzing neural oscillations in brain recordings."""
    
    name: str = "neural_oscillation_detector"
    description: str = "Detect and analyze neural oscillations, brain waves, and rhythmic activity patterns"
    args_schema = OscillationAnalysisInput
    
    def _run(self, brain_region: str, frequency_band: str = "all", 
             recording_type: str = "LFP", duration_seconds: float = 60.0) -> Dict[str, Any]:
        """Run oscillation detection and analysis."""
        
        frequency_bands = {
            "delta": (0.5, 4),
            "theta": (4, 8),
            "alpha": (8, 13),
            "beta": (13, 30),
            "gamma": (30, 100)
        }
        
        if frequency_band == "all":
            bands_to_analyze = frequency_bands
        elif frequency_band in frequency_bands:
            bands_to_analyze = {frequency_band: frequency_bands[frequency_band]}
        else:
            return {"error": f"Unknown frequency band: {frequency_band}"}
        
        results = {
            "brain_region": brain_region,
            "recording_type": recording_type,
            "duration_seconds": duration_seconds,
            "detected_oscillations": []
        }
        
        for band_name, (low_freq, high_freq) in bands_to_analyze.items():
            oscillation = self._analyze_frequency_band(band_name, low_freq, high_freq, brain_region)
            results["detected_oscillations"].append(oscillation)
        
        # Add cross-frequency coupling analysis
        if len(bands_to_analyze) > 1:
            results["cross_frequency_coupling"] = self._analyze_coupling(brain_region)
        
        return results
    
    def _analyze_frequency_band(self, band_name: str, low_freq: float, 
                               high_freq: float, brain_region: str) -> Dict[str, Any]:
        """Analyze a specific frequency band."""
        
        # Simulate oscillation detection based on brain region
        region_modifiers = {
            "hippocampus": {"theta": 2.0, "gamma": 1.5},
            "cortex": {"alpha": 1.8, "beta": 1.3},
            "thalamus": {"delta": 2.5, "alpha": 1.2}
        }
        
        modifier = region_modifiers.get(brain_region, {}).get(band_name, 1.0)
        base_power = np.random.uniform(10, 100) * modifier
        
        return {
            "frequency_band": band_name,
            "frequency_range_hz": [low_freq, high_freq],
            "peak_frequency_hz": round(np.random.uniform(low_freq, high_freq), 2),
            "power_spectral_density": round(base_power, 2),
            "coherence": round(np.random.uniform(0.3, 0.9), 3),
            "phase_locking_value": round(np.random.uniform(0.2, 0.8), 3),
            "burst_duration_ms": round(np.random.uniform(50, 500), 1),
            "inter_burst_interval_ms": round(np.random.uniform(100, 2000), 1),
            "rhythmicity_index": round(np.random.uniform(0.4, 0.95), 3)
        }
    
    def _analyze_coupling(self, brain_region: str) -> Dict[str, Any]:
        """Analyze cross-frequency coupling between different bands."""
        
        coupling_types = ["phase_amplitude", "phase_phase", "amplitude_amplitude"]
        
        return {
            "theta_gamma_coupling": {
                "type": "phase_amplitude",
                "strength": round(np.random.uniform(0.1, 0.6), 3),
                "preferred_phase_deg": round(np.random.uniform(0, 360), 1)
            },
            "alpha_beta_coupling": {
                "type": "phase_phase",
                "strength": round(np.random.uniform(0.05, 0.4), 3),
                "phase_lag_ms": round(np.random.uniform(5, 50), 1)
            },
            "delta_theta_coupling": {
                "type": "amplitude_amplitude",
                "correlation": round(np.random.uniform(0.2, 0.7), 3),
                "time_lag_ms": round(np.random.uniform(10, 100), 1)
            }
        }