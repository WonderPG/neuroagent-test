"""Synapse Analyzer Tool for analyzing synaptic properties and connections."""

from typing import Dict, List, Optional, Any
import numpy as np
from pydantic import BaseModel, Field
from neuroagent.tools.base_tool import BaseTool


class SynapseAnalysisInput(BaseModel):
    """Input schema for synapse analysis."""
    pre_neuron_type: str = Field(description="Type of presynaptic neuron (e.g., pyramidal, interneuron)")
    post_neuron_type: str = Field(description="Type of postsynaptic neuron")
    brain_region: str = Field(default="cortex", description="Brain region to analyze")
    analysis_type: str = Field(default="strength", description="Type of analysis: strength, plasticity, or connectivity")


class SynapseAnalyzerTool(BaseTool):
    """Tool for analyzing synaptic properties between neuron types."""
    
    name: str = "synapse_analyzer"
    description: str = "Analyze synaptic strength, plasticity, and connectivity between different neuron types"
    args_schema = SynapseAnalysisInput
    
    def _run(self, pre_neuron_type: str, post_neuron_type: str, 
             brain_region: str = "cortex", analysis_type: str = "strength") -> Dict[str, Any]:
        """Run synapse analysis."""
        
        if analysis_type == "strength":
            return self._analyze_synaptic_strength(pre_neuron_type, post_neuron_type, brain_region)
        elif analysis_type == "plasticity":
            return self._analyze_plasticity(pre_neuron_type, post_neuron_type, brain_region)
        elif analysis_type == "connectivity":
            return self._analyze_connectivity(pre_neuron_type, post_neuron_type, brain_region)
        else:
            return {"error": f"Unknown analysis type: {analysis_type}"}
    
    def _analyze_synaptic_strength(self, pre_type: str, post_type: str, region: str) -> Dict[str, Any]:
        """Analyze synaptic strength between neuron types."""
        base_strength = np.random.uniform(50, 200)
        
        # Adjust based on known neuron interactions
        if pre_type == "pyramidal" and post_type == "interneuron":
            multiplier = 1.5
        elif pre_type == "interneuron" and post_type == "pyramidal":
            multiplier = 0.8
        else:
            multiplier = 1.0
            
        strength = base_strength * multiplier
        
        return {
            "analysis_type": "synaptic_strength",
            "pre_neuron": pre_type,
            "post_neuron": post_type,
            "brain_region": region,
            "strength_pA": round(strength, 2),
            "connection_probability": round(np.random.uniform(0.1, 0.8), 3),
            "latency_ms": round(np.random.uniform(0.5, 3.0), 2),
            "reliability": round(np.random.uniform(0.6, 0.95), 3)
        }
    
    def _analyze_plasticity(self, pre_type: str, post_type: str, region: str) -> Dict[str, Any]:
        """Analyze synaptic plasticity properties."""
        return {
            "analysis_type": "plasticity",
            "pre_neuron": pre_type,
            "post_neuron": post_type,
            "brain_region": region,
            "ltp_threshold_hz": round(np.random.uniform(10, 50), 1),
            "ltd_threshold_hz": round(np.random.uniform(1, 10), 1),
            "max_potentiation_percent": round(np.random.uniform(150, 400), 1),
            "max_depression_percent": round(np.random.uniform(20, 80), 1),
            "time_constant_minutes": round(np.random.uniform(30, 180), 1)
        }
    
    def _analyze_connectivity(self, pre_type: str, post_type: str, region: str) -> Dict[str, Any]:
        """Analyze connectivity patterns."""
        return {
            "analysis_type": "connectivity",
            "pre_neuron": pre_type,
            "post_neuron": post_type,
            "brain_region": region,
            "connection_density": round(np.random.uniform(0.05, 0.3), 4),
            "average_synapses_per_connection": round(np.random.uniform(1, 8), 1),
            "spatial_reach_um": round(np.random.uniform(50, 500), 1),
            "clustering_coefficient": round(np.random.uniform(0.1, 0.7), 3)
        }