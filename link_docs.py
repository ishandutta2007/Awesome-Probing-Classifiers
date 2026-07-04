import os

readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Probing-Classifiers/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "**The Static Structural Layer Probing Era (~2016–2019)**": "[**The Static Structural Layer Probing Era (~2016–2019)**](docs/static_structural_layer_probing_era.md)",
    "**The Information-Theoretic & Control Probe Era (~2020–2022)**": "[**The Information-Theoretic & Control Probe Era (~2020–2022)**](docs/information_theoretic_control_probe_era.md)",
    "**The Causal Interchange Intervention Era (~2021–2024)**": "[**The Causal Interchange Intervention Era (~2021–2024)**](docs/causal_interchange_intervention_era.md)",
    "**The Monosemantic Feature Probe and Dictionary Era (Present)**": "[**The Monosemantic Feature Probe and Dictionary Era (Present)**](docs/monosemantic_feature_probe_and_dictionary_era.md)",
    "**A. Linear Probing (The Expressiveness Ceiling)**": "[**A. Linear Probing (The Expressiveness Ceiling)**](docs/linear_probing.md)",
    "**B. Structural Probing (Geometric Spacing)**": "[**B. Structural Probing (Geometric Spacing)**](docs/structural_probing.md)",
    "**C. Control Probes & Amortized MDL Probes**": "[**C. Control Probes & Amortized MDL Probes**](docs/control_probes_and_amortized_mdl_probes.md)",
    "**D. Edge Probing (Span-Relational Diagnostics)**": "[**D. Edge Probing (Span-Relational Diagnostics)**](docs/edge_probing.md)",
    "**Activation Registration Hooks**": "[**Activation Registration Hooks**](docs/activation_registration_hooks.md)",
    "**The Selectivity-Normalization Layer**": "[**The Selectivity-Normalization Layer**](docs/selectivity_normalization_layer.md)",
    "**The Activation Cache Volume Explosion Wall**": "[**The Activation Cache Volume Explosion Wall**](docs/activation_cache_volume_explosion_wall.md)",
    "**The Superposition and Opaque Polysemantic Confounding**": "[**The Superposition and Opaque Polysemantic Confounding**](docs/superposition_and_opaque_polysemantic_confounding.md)",
    "**Mechanistic Model Auditing & Safety Red-Teaming (Jailbreak Detection)**": "[**Mechanistic Model Auditing & Safety Red-Teaming (Jailbreak Detection)**](docs/mechanistic_model_auditing_safety_red_teaming.md)",
    "**Automated Corporate Hallucination & Fact-Checking Filters**": "[**Automated Corporate Hallucination & Fact-Checking Filters**](docs/automated_corporate_hallucination_fact_checking_filters.md)",
    "**Anatomical Feature-Extraction Mapping in Medical CV Backbones**": "[**Anatomical Feature-Extraction Mapping in Medical CV Backbones**](docs/anatomical_feature_extraction_mapping_medical_cv_backbones.md)"
}

for old, new in replacements.items():
    content = content.replace(f"| {old} |", f"| {new} |")
    # also replacing in case it has spaces around
    content = content.replace(f"| {old}", f"| {new}")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated README.md with links")
