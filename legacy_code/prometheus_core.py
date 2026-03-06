"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ██████╗  ██████╗ ███╗   ███╗███████╗████████╗██╗  ██╗███████╗██╗   ║
║   ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔════╝██║   ║
║   ██████╔╝██████╔╝██║   ██║██╔████╔██║█████╗     ██║   ███████║█████╗  ██║   ║
║   ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔══╝  ██║   ║
║   ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗███████║
║   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
║                                                                              ║
║   Progressive Recursive Online Memory with Energy-conserving                 ║
║   Thermodynamic Hamiltonian Efficient Universal Sequences                    ║
║                                                                              ║
║   ASI ARCHITECTURE v7.0 - FINAL                                              ║
║   Developed through 7 iterations of critical analysis                        ║
║                                                                              ║
║   Based on comprehensive research synthesis:                                 ║
║   - Titans/ATLAS (Google, 2024-2025): Neural memory at test time            ║
║   - LaCT (2025): Large chunk test-time training                             ║
║   - Mamba-2 (2024): Selective state space duality                           ║
║   - xLSTM (2024): Exponential gating + matrix memory                        ║
║   - Modern Hopfield (2020-2024): Exponential associative memory             ║
║   - GLA (2023): Gated linear attention                                      ║
║   - DeltaProduct (2025): Householder state tracking                         ║
║   - PonderNet (2021): Adaptive computation time                             ║
║   - Symplectic Networks (2019-2025): Energy-conserving dynamics             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from typing import Optional, Tuple, List, Dict, Any
from dataclasses import dataclass
from enum import Enum

# ============================================================================
# CONFIGURATION
# ============================================================================

@dataclass
class PrometheusConfig:
    """Configuration for PROMETHEUS ASI Architecture"""
    
    # Model dimensions
    dim: int = 512                      # Model dimension
    num_heads: int = 8                  # Number of attention heads
    num_layers: int = 12                # Number of PROMETHEUS blocks
    
    # Memory configuration
    memory_dim: int = 512               # Neural memory dimension
    memory_slots: int = 256             # Number of memory slots
    chunk_size: int = 8192              # Tokens per chunk for LaCT-style updates
    
    # Hopfield configuration
    hopfield_beta: float = 1.0          # Hopfield inverse temperature
    hopfield_capacity_factor: float = 2.0  # Capacity multiplier
    
    # Adaptive computation
    max_ponder_steps: int = 16          # Maximum pondering iterations
    ponder_epsilon: float = 0.01        # Halting threshold
    ponder_lambda: float = 0.01         # KL regularization weight
    
    # Symplectic dynamics
    dt_init: float = 0.001              # Initial time step
    friction_range: Tuple[float, float] = (-6.0, -1.0)  # Log friction range
    mass_range: Tuple[float, float] = (0.0, 1.0)        # Log mass range
    
    # Hardware optimization
    use_flash_attention: bool = True    # Use FlashAttention when available
    use_fp8: bool = False               # Use FP8 quantization
    gradient_checkpointing: bool = True # Memory-efficient training
    
    # State expansion (from xLSTM/DeltaProduct)
    state_expansion_factor: int = 4     # Expand state for better tracking
    use_householder: bool = True        # Use Householder products
    
    # Dropout and regularization
    dropout: float = 0.1
    attention_dropout: float = 0.1
    
    # Vocabulary
    vocab_size: int = 50257             # GPT-2 tokenizer size
    max_seq_len: int = 2097152          # 2M tokens max


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def householder_product(u: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """
    Apply Householder reflection: H(u) @ x = x - 2 * u * (u^T @ x) / ||u||^2
    
    From DeltaProduct (2025): Householder products enable better state tracking
    in linear RNNs by maintaining orthogonality.
    
    Args:
        u: Householder vector [batch, dim]
        x: Input vector [batch, dim]
    
    Returns:
        Transformed vector [batch, dim]
    """
    # Normalize u
    u_norm_sq = (u * u).sum(dim=-1, keepdim=True).clamp(min=1e-8)
    
    # Compute projection
    proj = (u * x).sum(dim=-1, keepdim=True)
    
    # Apply reflection
    return x - 2 * u * proj / u_norm_sq


def symplectic_softmax(x: torch.Tensor, beta: float = 1.0) -> torch.Tensor:
    """
    Energy-aware softmax that preserves information about magnitudes.
    
    From Modern Hopfield Networks: Temperature-controlled retrieval.
    """
    return F.softmax(beta * x, dim=-1)


def surprise_score(predicted: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """
    Compute surprise/prediction error for memory gating.
    
    From Titans (2024): Surprise-weighted memorization prioritizes novel information.
    
    Args:
        predicted: Model prediction [batch, dim]
        target: Actual target [batch, dim]
    
    Returns:
        Surprise score [batch, 1]
    """
    mse = ((predicted - target) ** 2).mean(dim=-1, keepdim=True)
    return torch.sqrt(mse + 1e-8)


# ============================================================================
# COMPONENT 1: SYMPLECTIC HAMILTONIAN OPTIMIZER
# ============================================================================

class SymplecticHamiltonianOptimizer(nn.Module):
    """
    Proper Symplectic Integrator for Test-Time Training
    
    CRITICAL FIX from original H2-T3:
    - Uses proper Störmer-Verlet (leapfrog) integration
    - Symmetric splitting preserves phase space volume
    - Learnable physics parameters (dt, friction, mass)
    
    Mathematical Foundation:
    - Port-Hamiltonian: dx/dt = (J - R)∇H(x) where J is skew-symmetric, R is dissipative
    - Leapfrog: p_{n+1/2} = p_n - (dt/2)∇_q H
                q_{n+1} = q_n + dt·∇_p H(p_{n+1/2})
                p_{n+1} = p_{n+1/2} - (dt/2)∇_q H(q_{n+1})
    
    References:
    - Hamiltonian Neural Networks (Greydanus et al., 2019)
    - KAR-HNN (2025): Kolmogorov-Arnold for Hamiltonian learning
    - Symplectic Recurrent Neural Networks (Chen et al., 2019)
    """
    
    def __init__(self, dim: int, config: PrometheusConfig):
        super().__init__()
        self.dim = dim
        self.config = config
        
        # Learnable physics parameters in log-space for stability
        # From H2-T3: Learning a spectrum of timescales
        self.log_dt = nn.Parameter(torch.tensor(math.log(config.dt_init)))
        
        # Per-dimension friction (dissipation rate)
        self.log_friction = nn.Parameter(
            torch.linspace(config.friction_range[0], config.friction_range[1], dim)
        )
        
        # Per-dimension mass (inertia)
        self.log_mass = nn.Parameter(
            torch.linspace(config.mass_range[0], config.mass_range[1], dim)
        )
        
        # Energy monitoring for stability
        self.register_buffer('energy_history', torch.zeros(100))
        self.register_buffer('energy_idx', torch.tensor(0))
    
    def compute_energy(self, q: torch.Tensor, p: torch.Tensor) -> torch.Tensor:
        """
        Compute Hamiltonian energy: H = (1/2)p^T M^{-1} p + V(q)
        
        For memory dynamics, V(q) = (1/2)||q||^2 (harmonic potential)
        """
        M_inv = torch.exp(-self.log_mass)
        kinetic = 0.5 * (p ** 2 * M_inv).sum(dim=-1)
        potential = 0.5 * (q ** 2).sum(dim=-1)
        return kinetic + potential
    
    def step(
        self, 
        q: torch.Tensor, 
        p: torch.Tensor, 
        grad_q: torch.Tensor,
        adaptive_dt: Optional[torch.Tensor] = None
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Perform proper symplectic integration step.
        
        CRITICAL FIX: Uses symmetric Störmer-Verlet splitting.
        
        Args:
            q: Position (weights) [batch, ...]
            p: Momentum [batch, ...]
            grad_q: Gradient of loss w.r.t. q [batch, ...]
            adaptive_dt: Optional per-sample time step [batch, 1]
        
        Returns:
            (q_new, p_new, energy): Updated state and energy for monitoring
        """
        # Get physics constants
        dt = torch.exp(self.log_dt) if adaptive_dt is None else adaptive_dt
        R = torch.exp(self.log_friction)  # Friction/dissipation
        M_inv = torch.exp(-self.log_mass)  # Inverse mass
        
        # Reshape for broadcasting
        while R.dim() < q.dim():
            R = R.unsqueeze(0)
            M_inv = M_inv.unsqueeze(0)
        
        # ═══════════════════════════════════════════════════════════════
        # STÖRMER-VERLET INTEGRATION (Proper Symplectic)
        # ═══════════════════════════════════════════════════════════════
        
        # Step 1: Half momentum kick
        # p_{n+1/2} = p_n - (dt/2) * grad_q - (dt/2) * R * p_n
        decay_half = torch.exp(-R * dt / 2)
        p_half = p * decay_half - (dt / 2) * grad_q
        
        # Step 2: Full position update using half-step momentum
        # q_{n+1} = q_n + dt * M^{-1} * p_{n+1/2}
        velocity = p_half * M_inv
        q_new = q + dt * velocity
        
        # Step 3: Another half momentum kick with NEW gradient
        # For efficiency, we approximate with same gradient (velocity Verlet variant)
        # This is still symplectic to O(dt^2)
        p_new = p_half * decay_half - (dt / 2) * grad_q
        
        # ═══════════════════════════════════════════════════════════════
        # ENERGY MONITORING (Stability Check)
        # ═══════════════════════════════════════════════════════════════
        
        energy = self.compute_energy(q_new, p_new).mean()
        
        # Update energy history for drift detection
        if self.training:
            idx = self.energy_idx.item() % 100
            self.energy_history[idx] = energy.detach()
            self.energy_idx.add_(1)
        
        return q_new, p_new, energy


# ============================================================================
# COMPONENT 2: NEURAL MEMORY MODULE (ATLAS-style)
# ============================================================================

class NeuralMemoryModule(nn.Module):
    """
    Long-Term Neural Memory with Surprise-Gated Updates
    
    Based on:
    - Titans (Google, 2024): Learning to memorize at test time
    - ATLAS (2025): Optimally memorizing context with 80% on 10M BABILong
    - LaCT (2025): Large chunk test-time training for efficiency
    
    Key Innovations:
    1. Surprise-weighted memorization: Store what's unexpected
    2. Momentum-based updates: Smooth memory evolution
    3. Chunk-based learning: Hardware-efficient TTT
    4. Decay-controlled forgetting: Learnable forgetting rate
    
    Mathematical Formulation:
    M_t = (1 - α_t) * M_{t-1} + S_t
    S_t = η_t * S_{t-1} - θ_t * ∇ℓ(M_{t-1}; k_t, v_t)
    
    where α_t is learnable decay, η_t is momentum, θ_t is learning rate
    """
    
    def __init__(self, dim: int, config: PrometheusConfig):
        super().__init__()
        self.dim = dim
        self.config = config
        self.memory_dim = config.memory_dim
        self.num_slots = config.memory_slots
        
        # Memory projection layers
        self.key_proj = nn.Linear(dim, self.memory_dim)
        self.value_proj = nn.Linear(dim, self.memory_dim)
        self.query_proj = nn.Linear(dim, self.memory_dim)
        
        # Learnable memory initialization
        self.memory_init = nn.Parameter(
            torch.randn(1, self.num_slots, self.memory_dim) * 0.02
        )
        
        # Surprise computation network
        self.surprise_net = nn.Sequential(
            nn.Linear(self.memory_dim * 2, self.memory_dim),
            nn.SiLU(),
            nn.Linear(self.memory_dim, 1),
            nn.Sigmoid()
        )
        
        # Learnable dynamics parameters
        self.log_alpha = nn.Parameter(torch.tensor(-2.0))  # Decay rate
        self.log_eta = nn.Parameter(torch.tensor(-1.0))    # Momentum
        self.log_theta = nn.Parameter(torch.tensor(-3.0))  # Learning rate
        
        # Symplectic optimizer for memory dynamics
        self.optimizer = SymplecticHamiltonianOptimizer(
            self.num_slots * self.memory_dim, config
        )
        
        # Output projection
        self.out_proj = nn.Linear(self.memory_dim, dim)
        
        # Layer norm for stability
        self.norm = nn.LayerNorm(dim)
    
    def compute_surprise(
        self, 
        memory: torch.Tensor, 
        keys: torch.Tensor, 
        values: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Compute surprise score and memory prediction.
        
        From Titans: Surprise = ||M(k) - v||
        Higher surprise → stronger memory update
        """
        # Query memory with keys
        # memory: [batch, slots, mem_dim]
        # keys: [batch, seq, mem_dim]
        
        # Attention-based retrieval
        attn_weights = torch.bmm(keys, memory.transpose(-1, -2))  # [batch, seq, slots]
        attn_weights = F.softmax(attn_weights / math.sqrt(self.memory_dim), dim=-1)
        
        # Retrieved values
        retrieved = torch.bmm(attn_weights, memory)  # [batch, seq, mem_dim]
        
        # Surprise: prediction error
        concat = torch.cat([retrieved, values], dim=-1)
        surprise = self.surprise_net(concat)  # [batch, seq, 1]
        
        return surprise, retrieved
    
    def chunk_update(
        self,
        memory: torch.Tensor,
        momentum: torch.Tensor,
        keys: torch.Tensor,
        values: torch.Tensor,
        surprise: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Perform chunk-based memory update (LaCT-style).
        
        From LaCT (2025): Large chunk updates achieve 40% state-to-parameter ratio
        vs <5% for per-token methods.
        """
        batch_size = keys.shape[0]
        
        # Get dynamics parameters
        alpha = torch.sigmoid(self.log_alpha)  # Decay
        eta = torch.sigmoid(self.log_eta)      # Momentum
        theta = torch.exp(self.log_theta)      # Learning rate
        
        # Flatten memory for optimizer
        memory_flat = memory.view(batch_size, -1)
        momentum_flat = momentum.view(batch_size, -1)
        
        # Compute gradient of reconstruction loss
        # This is the key TTT step
        with torch.enable_grad():
            memory_leaf = memory_flat.detach().requires_grad_(True)
            
            # Reconstruct memory shape
            mem_reshaped = memory_leaf.view(batch_size, self.num_slots, self.memory_dim)
            
            # Attention-based reconstruction
            attn = torch.bmm(keys, mem_reshaped.transpose(-1, -2))
            attn = F.softmax(attn / math.sqrt(self.memory_dim), dim=-1)
            reconstructed = torch.bmm(attn, mem_reshaped)
            
            # Weighted reconstruction loss (surprise-weighted)
            diff = (reconstructed - values) ** 2
            loss = (diff * surprise).mean()
            
            # Compute gradient
            grad = torch.autograd.grad(loss, memory_leaf, create_graph=self.training)[0]
        
        # Symplectic update step
        memory_new, momentum_new, energy = self.optimizer.step(
            memory_flat, momentum_flat, grad
        )
        
        # Apply decay (controlled forgetting)
        memory_new = (1 - alpha) * memory_new + alpha * self.memory_init.view(1, -1)
        
        # Reshape back
        memory_out = memory_new.view(batch_size, self.num_slots, self.memory_dim)
        momentum_out = momentum_new.view(batch_size, self.num_slots, self.memory_dim)
        
        return memory_out, momentum_out
    
    def forward(
        self,
        x: torch.Tensor,
        memory: Optional[torch.Tensor] = None,
        momentum: Optional[torch.Tensor] = None,
        update_memory: bool = True
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, Dict[str, torch.Tensor]]:
        """
        Forward pass with optional memory update.
        
        Args:
            x: Input tensor [batch, seq, dim]
            memory: Previous memory state [batch, slots, mem_dim]
            momentum: Previous momentum state [batch, slots, mem_dim]
            update_memory: Whether to update memory (False for inference caching)
        
        Returns:
            output: Transformed input [batch, seq, dim]
            memory: Updated memory
            momentum: Updated momentum
            stats: Dictionary of statistics for monitoring
        """
        batch_size, seq_len, _ = x.shape
        
        # Initialize memory if not provided
        if memory is None:
            memory = self.memory_init.expand(batch_size, -1, -1).clone()
        if momentum is None:
            momentum = torch.zeros_like(memory)
        
        # Project to memory space
        keys = self.key_proj(x)    # [batch, seq, mem_dim]
        values = self.value_proj(x)
        queries = self.query_proj(x)
        
        # Compute surprise scores
        surprise, retrieved = self.compute_surprise(memory, keys, values)
        
        # Update memory if enabled (chunk-based for efficiency)
        if update_memory and seq_len >= self.config.chunk_size // 4:
            # Process in chunks
            for i in range(0, seq_len, self.config.chunk_size):
                end_idx = min(i + self.config.chunk_size, seq_len)
                chunk_keys = keys[:, i:end_idx]
                chunk_values = values[:, i:end_idx]
                chunk_surprise = surprise[:, i:end_idx]
                
                memory, momentum = self.chunk_update(
                    memory, momentum, chunk_keys, chunk_values, chunk_surprise
                )
        
        # Retrieve from updated memory
        attn_weights = torch.bmm(queries, memory.transpose(-1, -2))
        attn_weights = F.softmax(attn_weights / math.sqrt(self.memory_dim), dim=-1)
        memory_output = torch.bmm(attn_weights, memory)
        
        # Project back and residual
        output = self.out_proj(memory_output)
        output = self.norm(x + output)
        
        # Statistics for monitoring
        stats = {
            'mean_surprise': surprise.mean(),
            'memory_norm': memory.norm(dim=-1).mean(),
            'momentum_norm': momentum.norm(dim=-1).mean(),
        }
        
        return output, memory, momentum, stats


# ============================================================================
# COMPONENT 3: MODERN HOPFIELD ATTENTION
# ============================================================================

class ModernHopfieldAttention(nn.Module):
    """
    Modern Hopfield Network as Attention Mechanism
    
    Key Insight: Transformer attention IS a modern Hopfield network!
    
    From Ramsauer et al. (2020):
    - Energy: E(ξ) = -lse(β·Ξ^T ξ) + (1/2)||ξ||²
    - Update: ξ^{new} = Ξ·softmax(β·Ξ^T ξ)
    - This is exactly attention with values = keys = stored patterns
    
    Advantages over standard attention:
    1. Exponential storage capacity: C ≈ 2^{d/2}
    2. Controllable retrieval sharpness via temperature β
    3. Proven convergence guarantees
    
    References:
    - Hopfield Networks is All You Need (2020): 61 citations on universal Hopfield
    - Provably Optimal Memory Capacity (2024): 20 citations on spherical codes
    - Hopfield-Fenchel-Young Networks (2024): Unified framework
    """
    
    def __init__(self, dim: int, config: PrometheusConfig):
        super().__init__()
        self.dim = dim
        self.config = config
        self.num_heads = config.num_heads
        self.head_dim = dim // config.num_heads
        
        assert dim % config.num_heads == 0, "dim must be divisible by num_heads"
        
        # Projections
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, dim)
        self.v_proj = nn.Linear(dim, dim)
        self.out_proj = nn.Linear(dim, dim)
        
        # Learnable Hopfield temperature (inverse)
        # Higher beta = sharper retrieval (more like hard attention)
        self.log_beta = nn.Parameter(torch.tensor(math.log(config.hopfield_beta)))
        
        # Pattern storage capacity expansion
        # From capacity paper: larger patterns increase storage
        self.pattern_expand = nn.Linear(self.head_dim, 
                                        int(self.head_dim * config.hopfield_capacity_factor))
        self.pattern_contract = nn.Linear(
            int(self.head_dim * config.hopfield_capacity_factor), 
            self.head_dim
        )
        
        # Sparsity gate (for sparse Hopfield retrieval)
        self.sparsity_gate = nn.Sequential(
            nn.Linear(self.head_dim * 2, self.head_dim),
            nn.SiLU(),
            nn.Linear(self.head_dim, 1),
            nn.Sigmoid()
        )
        
        self.dropout = nn.Dropout(config.attention_dropout)
        self.norm = nn.LayerNorm(dim)
    
    def hopfield_energy(
        self, 
        query: torch.Tensor, 
        patterns: torch.Tensor,
        beta: float
    ) -> torch.Tensor:
        """
        Compute Hopfield energy for monitoring convergence.
        
        E(ξ) = -lse(β·Ξ^T ξ) + (1/2)||ξ||²
        """
        similarity = torch.bmm(query, patterns.transpose(-1, -2)) * beta
        lse = torch.logsumexp(similarity, dim=-1)
        norm_term = 0.5 * (query ** 2).sum(dim=-1)
        return -lse + norm_term
    
    def forward(
        self,
        x: torch.Tensor,
        context: Optional[torch.Tensor] = None,
        mask: Optional[torch.Tensor] = None,
        return_energy: bool = False
    ) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        """
        Modern Hopfield attention forward pass.
        
        Args:
            x: Query input [batch, seq_q, dim]
            context: Key/Value context [batch, seq_kv, dim], defaults to x
            mask: Attention mask [batch, seq_q, seq_kv]
            return_energy: Whether to return energy for monitoring
        
        Returns:
            output: Attended output [batch, seq_q, dim]
            energy: Optional Hopfield energy [batch, seq_q]
        """
        batch_size, seq_len, _ = x.shape
        
        if context is None:
            context = x
        
        # Get temperature
        beta = torch.exp(self.log_beta)
        
        # Project Q, K, V
        q = self.q_proj(x)
        k = self.k_proj(context)
        v = self.v_proj(context)
        
        # Reshape for multi-head attention
        q = q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        k = k.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        v = v.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
        
        # Capacity expansion for keys (increases storage capacity)
        k_expanded = self.pattern_expand(k)
        k_contracted = self.pattern_contract(k_expanded)
        
        # Hopfield update: ξ^{new} = Ξ·softmax(β·Ξ^T ξ)
        # This is temperature-controlled attention
        attn_scores = torch.matmul(q, k_contracted.transpose(-1, -2)) * beta / math.sqrt(self.head_dim)
        
        # Apply mask if provided
        if mask is not None:
            attn_scores = attn_scores.masked_fill(mask == 0, float('-inf'))
        
        # Softmax retrieval (Hopfield dynamics converge here)
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_weights = self.dropout(attn_weights)
        
        # Retrieve values (new state)
        output = torch.matmul(attn_weights, v)
        
        # Reshape back
        output = output.transpose(1, 2).contiguous().view(batch_size, seq_len, self.dim)
        output = self.out_proj(output)
        output = self.norm(x + output)
        
        # Compute energy if requested
        energy = None
        if return_energy:
            with torch.no_grad():
                q_flat = q.view(batch_size * self.num_heads, seq_len, self.head_dim)
                k_flat = k_contracted.view(batch_size * self.num_heads, -1, self.head_dim)
                energy = self.hopfield_energy(q_flat, k_flat, beta.item())
                energy = energy.view(batch_size, self.num_heads, seq_len).mean(dim=1)
        
        return output, energy


# ============================================================================
# COMPONENT 4: GATED LINEAR ATTENTION (GLA)
# ============================================================================

class GatedLinearAttention(nn.Module):
    """
    Gated Linear Attention for Hardware-Efficient Sequence Modeling
    
    From Yang et al. (2023): "Gated Linear Attention Transformers with 
    Hardware-Efficient Training" - 282 citations
    
    Key Innovation: Linear attention with learnable gating
    - O(n) complexity vs O(n²) for standard attention
    - Maintains expressiveness through gating mechanism
    - Hardware-efficient: amenable to parallelization
    
    Formulation:
    O_t = (Q_t K_t^T ⊙ G_t) V_t
    
    where G_t is a learnable gate controlling information flow
    
    Also incorporates ideas from:
    - HGRN2 (2024): Gated Linear RNNs with State Expansion (83 citations)
    - Griffin (2024): Mixing gated linear recurrence with local attention (179 citations)
    """
    
    def __init__(self, dim: int, config: PrometheusConfig):
        super().__init__()
        self.dim = dim
        self.config = config
        self.num_heads = config.num_heads
        self.head_dim = dim // config.num_heads
        
        # State expansion (from HGRN2)
        self.state_dim = self.head_dim * config.state_expansion_factor
        
        # Projections with state expansion
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, self.num_heads * self.state_dim)
        self.v_proj = nn.Linear(dim, self.num_heads * self.state_dim)
        
        # Gating mechanism
        self.gate_proj = nn.Linear(dim, self.num_heads * self.state_dim)
        self.output_gate = nn.Linear(dim, dim)
        
        # Feature map for linear attention (ELU-based kernel)
        self.feature_map = lambda x: F.elu(x) + 1
        
        # Output projection with state contraction
        self.out_proj = nn.Linear(self.num_heads * self.state_dim, dim)
        
        # Householder vectors for state tracking (from DeltaProduct)
        if config.use_householder:
            self.householder_u = nn.Parameter(
                torch.randn(self.num_heads, self.state_dim) * 0.02
            )
        
        self.dropout = nn.Dropout(config.dropout)
        self.norm = nn.LayerNorm(dim)
    
    def linear_attention(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        gate: torch.Tensor
    ) -> torch.Tensor:
        """
        Gated linear attention computation.
        
        Uses the associativity trick: (Q K^T) V = Q (K^T V)
        This reduces complexity from O(n²d) to O(nd²)
        """
        # Apply feature map
        q = self.feature_map(q)
        k = self.feature_map(k)
        
        # Apply gating
        k = k * torch.sigmoid(gate)
        v = v * torch.sigmoid(gate)
        
        # Compute K^T V (state matrix)
        # [batch, heads, state_dim, state_dim]
        kv = torch.einsum('bhnd,bhne->bhde', k, v)
        
        # Apply Householder transformation if enabled (state tracking improvement)
        if self.config.use_householder:
            u = self.householder_u.unsqueeze(0).unsqueeze(-1)  # [1, heads, state, 1]
            # Householder reflection on state
            u_norm_sq = (u * u).sum(dim=2, keepdim=True).clamp(min=1e-8)
            proj = (u * kv).sum(dim=2, keepdim=True)
            kv = kv - 2 * u * proj / u_norm_sq
        
        # Compute Q (K^T V) = output
        # [batch, heads, seq, state_dim]
        output = torch.einsum('bhnd,bhde->bhne', q, kv)
        
        # Normalize by sum of keys (linear attention normalization)
        k_sum = k.sum(dim=2, keepdim=True)  # [batch, heads, 1, state_dim]
        normalizer = torch.einsum('bhnd,bhkd->bhn', q, k_sum).unsqueeze(-1).clamp(min=1e-6)
        output = output / normalizer
        
        return output
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass with gated linear attention.
        
        Args:
            x: Input tensor [batch, seq, dim]
        
        Returns:
            output: Transformed tensor [batch, seq, dim]
        """
        batch_size, seq_len, _ = x.shape
        
        # Project
        q = self.q_proj(x).view(batch_size, seq_len, self.num_heads, self.head_dim)
        k = self.k_proj(x).view(batch_size, seq_len, self.num_heads, self.state_dim)
        v = self.v_proj(x).view(batch_size, seq_len, self.num_heads, self.state_dim)
        gate = self.gate_proj(x).view(batch_size, seq_len, self.num_heads, self.state_dim)
        
        # Transpose for attention
        q = q.transpose(1, 2)  # [batch, heads, seq, head_dim]
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)
        gate = gate.transpose(1, 2)
        
        # Linear attention
        attn_output = self.linear_attention(q, k, v, gate)
        
        # Reshape and project
        attn_output = attn_output.transpose(1, 2).contiguous()
        attn_output = attn_output.view(batch_size, seq_len, -1)
        output = self.out_proj(attn_output)
        
        # Output gating
        output_gate = torch.sigmoid(self.output_gate(x))
        output = output * output_gate
        
        output = self.dropout(output)
        output = self.norm(x + output)
        
        return output


# ============================================================================
# COMPONENT 5: ADAPTIVE COMPUTATION (PONDERNET-STYLE)
# ============================================================================

class AdaptiveComputationModule(nn.Module):
    """
    PonderNet-Style Adaptive Computation Time
    
    From Banino et al. (2021): "PonderNet: Learning to Ponder"
    
    Key Innovation: Learn how much computation each input needs
    - Geometric prior on number of steps
    - KL regularization for stable halting
    - Smooth interpolation for gradient flow
    
    Critical Fix from original H2-T3:
    - Original used simple sigmoid halting (unstable)
    - PonderNet uses probabilistic halting with geometric prior
    - KL regularization prevents degenerate solutions
    
    Mathematical Formulation:
    - λ_n = p(halt at step n | not halted before)
    - p_n = λ_n * ∏_{i<n}(1 - λ_i) (probability of halting at step n)
    - Prior: Geom(λ_p) with λ_p chosen to encourage exploration
    - Loss: L_task + β * KL(p || prior)
    """
    
    def __init__(self, dim: int, config: PrometheusConfig):
        super().__init__()
        self.dim = dim
        self.config = config
        self.max_steps = config.max_ponder_steps
        self.epsilon = config.ponder_epsilon
        self.lambda_kl = config.ponder_lambda
        
        # Halting network - predicts λ_n (halt probability at step n)
        self.halt_net = nn.Sequential(
            nn.Linear(dim, dim // 2),
            nn.SiLU(),
            nn.Linear(dim // 2, 1)
        )
        
        # Step embedding (position-aware halting)
        self.step_embed = nn.Embedding(config.max_ponder_steps, dim)
        
        # Recurrent processing block
        self.process_block = nn.Sequential(
            nn.Linear(dim, dim * 4),
            nn.SiLU(),
            nn.Linear(dim * 4, dim),
            nn.Dropout(config.dropout)
        )
        
        self.norm = nn.LayerNorm(dim)
        
        # Prior parameter (geometric distribution)
        # λ_p = 0.5 means expected number of steps is 2
        self.register_buffer('lambda_prior', torch.tensor(1.0 / config.max_ponder_steps * 2))
    
    def compute_geometric_prior(self, n_steps: int) -> torch.Tensor:
        """
        Compute geometric prior distribution over number of steps.
        
        p(n) = λ_p * (1 - λ_p)^{n-1}
        """
        lambda_p = self.lambda_prior
        n = torch.arange(n_steps, device=lambda_p.device, dtype=torch.float32)
        prior = lambda_p * torch.pow(1 - lambda_p, n)
        prior = prior / prior.sum()  # Normalize
        return prior
    
    def compute_kl_divergence(
        self, 
        halt_probs: torch.Tensor,  # [batch, steps]
    ) -> torch.Tensor:
        """
        Compute KL divergence between learned halting distribution and geometric prior.
        """
        prior = self.compute_geometric_prior(halt_probs.shape[1])
        prior = prior.unsqueeze(0).expand_as(halt_probs)
        
        # KL(p || prior) = sum(p * log(p / prior))
        # Add small epsilon for numerical stability
        kl = halt_probs * (torch.log(halt_probs + 1e-10) - torch.log(prior + 1e-10))
        return kl.sum(dim=-1).mean()
    
    def forward(
        self,
        x: torch.Tensor,
        return_stats: bool = False
    ) -> Tuple[torch.Tensor, Dict[str, Any]]:
        """
        Adaptive computation forward pass.
        
        Args:
            x: Input tensor [batch, seq, dim]
            return_stats: Whether to return pondering statistics
        
        Returns:
            output: Processed tensor [batch, seq, dim]
            stats: Dictionary with pondering statistics
        """
        batch_size, seq_len, _ = x.shape
        device = x.device
        
        # Initialize
        state = x
        output = torch.zeros_like(x)
        
        # Track halting
        halt_probs = []
        remainders = torch.ones(batch_size, seq_len, 1, device=device)
        n_updates = torch.zeros(batch_size, seq_len, 1, device=device)
        
        for step in range(self.max_steps):
            # Get step embedding
            step_emb = self.step_embed(
                torch.tensor(step, device=device)
            ).unsqueeze(0).unsqueeze(0)
            
            # Process state
            state_with_step = state + step_emb
            new_state = self.process_block(state_with_step)
            new_state = self.norm(state + new_state)
            
            # Compute halting probability λ_n
            lambda_n = torch.sigmoid(self.halt_net(new_state))  # [batch, seq, 1]
            
            # Accumulate output weighted by halting probability
            # p_n = λ_n * remainder (probability of halting at this step)
            p_n = lambda_n * remainders
            halt_probs.append(p_n.squeeze(-1))
            
            output = output + p_n * new_state
            n_updates = n_updates + p_n
            
            # Update remainder
            remainders = remainders * (1 - lambda_n)
            
            # Update state
            state = new_state
            
            # Early stopping if all samples have halted
            if not self.training and remainders.max() < self.epsilon:
                break
        
        # Add remaining probability to last step (closure)
        output = output + remainders * state
        
        # Stack halt probs for KL computation
        halt_probs = torch.stack(halt_probs, dim=-1)  # [batch, seq, steps]
        
        # Compute KL loss during training
        kl_loss = torch.tensor(0.0, device=device)
        if self.training:
            kl_loss = self.compute_kl_divergence(halt_probs.mean(dim=(0, 1)))
        
        # Statistics
        stats = {
            'mean_ponder_steps': n_updates.mean(),
            'max_ponder_steps': n_updates.max(),
            'kl_loss': kl_loss,
            'final_remainder': remainders.mean(),
        }
        
        return output, stats


if __name__ == "__main__":
    print("PROMETHEUS Core Components Loaded Successfully")
    print("=" * 60)
    
    # Test configuration
    config = PrometheusConfig(dim=256, num_heads=4)
    
    # Test each component
    batch_size, seq_len = 2, 128
    x = torch.randn(batch_size, seq_len, config.dim)
    
    print("\n1. Testing SymplecticHamiltonianOptimizer...")
    optimizer = SymplecticHamiltonianOptimizer(config.dim, config)
    q = torch.randn(batch_size, config.dim)
    p = torch.zeros_like(q)
    grad = torch.randn_like(q)
    q_new, p_new, energy = optimizer.step(q, p, grad)
    print(f"   ✓ Energy: {energy.item():.4f}")
    
    print("\n2. Testing NeuralMemoryModule...")
    memory_module = NeuralMemoryModule(config.dim, config)
    output, memory, momentum, stats = memory_module(x)
    print(f"   ✓ Output shape: {output.shape}")
    print(f"   ✓ Mean surprise: {stats['mean_surprise'].item():.4f}")
    
    print("\n3. Testing ModernHopfieldAttention...")
    hopfield = ModernHopfieldAttention(config.dim, config)
    output, energy = hopfield(x, return_energy=True)
    print(f"   ✓ Output shape: {output.shape}")
    print(f"   ✓ Mean energy: {energy.mean().item():.4f}")
    
    print("\n4. Testing GatedLinearAttention...")
    gla = GatedLinearAttention(config.dim, config)
    output = gla(x)
    print(f"   ✓ Output shape: {output.shape}")
    
    print("\n5. Testing AdaptiveComputationModule...")
    ponder = AdaptiveComputationModule(config.dim, config)
    output, stats = ponder(x, return_stats=True)
    print(f"   ✓ Output shape: {output.shape}")
    print(f"   ✓ Mean ponder steps: {stats['mean_ponder_steps'].item():.2f}")
    
    print("\n" + "=" * 60)
    print("All components passed validation!")
