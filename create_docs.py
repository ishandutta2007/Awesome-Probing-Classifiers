import os

docs_dir = "C:/Users/ishan/Documents/Projects/Awesome-Probing-Classifiers/docs"
os.makedirs(docs_dir, exist_ok=True)

files = [
    {
        "filename": "static_structural_layer_probing_era.md",
        "title": "The Static Structural Layer Probing Era (~2016–2019)",
        "content": "This era marks the beginning of modern interpretability, where simple linear classifiers were used to probe what deep language and vision encoders were learning."
    },
    {
        "filename": "information_theoretic_control_probe_era.md",
        "title": "The Information-Theoretic & Control Probe Era (~2020–2022)",
        "content": "Resolved the selectivity crisis by introducing strict baseline controls and MDL probes."
    },
    {
        "filename": "causal_interchange_intervention_era.md",
        "title": "The Causal Interchange Intervention Era (~2021–2024)",
        "content": "Shifted from passive diagnostic observation to active structural validation using frameworks like Causal Mediation Analysis (CMA) and Interchange Intervention Training (IIT)."
    },
    {
        "filename": "monosemantic_feature_probe_and_dictionary_era.md",
        "title": "The Monosemantic Feature Probe and Dictionary Era (Present)",
        "content": "Focuses on monosemanticity through dictionary learning over sparse autoencoders (SAEs), allowing isolation of individual features."
    },
    {
        "filename": "linear_probing.md",
        "title": "A. Linear Probing (The Expressiveness Ceiling)",
        "content": "Restricts the probing classifier strictly to a single, non-parameterized linear transformation layer to enforce a strict capacity cap."
    },
    {
        "filename": "structural_probing.md",
        "title": "B. Structural Probing (Geometric Spacing)",
        "content": "Instead of predicting a discrete categorical label, the probe learns a linear distance metric matrix that projects hidden vectors for syntactic tree evaluation."
    },
    {
        "filename": "control_probes_and_amortized_mdl_probes.md",
        "title": "C. Control Probes & Amortized MDL Probes",
        "content": "Evaluates information transmission density through the lens of data compression, fully neutralizing probe-memorization bias."
    },
    {
        "filename": "edge_probing.md",
        "title": "D. Edge Probing (Span-Relational Diagnostics)",
        "content": "Targets sub-sequence relationships rather than isolated individual tokens by checking spans of words in a sentence."
    },
    {
        "filename": "activation_registration_hooks.md",
        "title": "Activation Registration Hooks",
        "content": "Intercepts model states cleanly using small software hooks at the terminal exits of target layer blocks."
    },
    {
        "filename": "selectivity_normalization_layer.md",
        "title": "The Selectivity-Normalization Layer",
        "content": "Acts as an online evaluation buffer that constantly measures the cross-entropy loss delta between the structural task and a randomized control matrix."
    },
    {
        "filename": "activation_cache_volume_explosion_wall.md",
        "title": "The Activation Cache Volume Explosion Wall",
        "content": "Addresses the colossal, multi-terabyte data footprint of storing high-dimensional continuous activation tensors using sparsification or checkpointing."
    },
    {
        "filename": "superposition_and_opaque_polysemantic_confounding.md",
        "title": "The Superposition and Opaque Polysemantic Confounding",
        "content": "Deep transformers compress millions of disparate real-world facts into a limited number of neural channels. Mitigation involves Sparse Autoencoders (SAEs)."
    },
    {
        "filename": "mechanistic_model_auditing_safety_red_teaming.md",
        "title": "Mechanistic Model Auditing & Safety Red-Teaming",
        "content": "Secures foundational enterprise deployments against systemic exploits using continuous internal tracking."
    },
    {
        "filename": "automated_corporate_hallucination_fact_checking_filters.md",
        "title": "Automated Corporate Hallucination & Fact-Checking Filters",
        "content": "Regulates large-scale retrieval-augmented generation (RAG) loops by monitoring internal activation spaces for truthfulness."
    },
    {
        "filename": "anatomical_feature_extraction_mapping_medical_cv_backbones.md",
        "title": "Anatomical Feature-Extraction Mapping in Medical CV Backbones",
        "content": "Decodes the feature representations of deep convolutional and vision-transformer diagnostic models using structural linear probes."
    }
]

for item in files:
    filepath = os.path.join(docs_dir, item['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {item['title']}\n\n")
        f.write(f"[⬅️ Back to README](../README.md)\n\n")
        f.write(f"## Detailed Information\n\n")
        f.write(f"{item['content']}\n\n")
        f.write(f"## Diagram\n\n")
        f.write(f"```mermaid\n")
        f.write(f"graph TD\n")
        f.write(f"    A[{item['title']}] --> B[More Details]\n")
        f.write(f"```\n\n")
        f.write(f"*(This page was auto-generated to provide detailed insights into {item['title']}.)*\n")

print(f"Created {len(files)} files in {docs_dir}")
