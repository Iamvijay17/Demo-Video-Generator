from TTS.api import TTS

print("🔍 Checking for Tamil language support in TTS models...")

try:
    # Create TTS instance
    tts = TTS()

    # Get available models using the manager
    manager = tts.manager
    tts_models = manager.list_tts_models()
    vc_models = manager.list_vc_models()
    all_models = tts_models + vc_models

    print(f"📋 Total TTS models available: {len(tts_models)}")
    print(f"🎭 Total VC models available: {len(vc_models)}")

    # Look for Tamil or Indic language models
    tamil_models = []
    indic_models = []

    for model in all_models:
        model_str = str(model).lower()
        if 'ta' in model_str or 'tamil' in model_str:
            tamil_models.append(model)
        elif any(lang in model_str for lang in ['indic', 'hi', 'bn', 'te', 'ml', 'kn']):
            indic_models.append(model)

    print(f"\n🇮🇳 Tamil-specific models found: {len(tamil_models)}")
    for model in tamil_models:
        print(f"  ✅ {model}")

    print(f"\n🌏 Other Indic language models: {len(indic_models)}")
    for model in indic_models[:5]:  # Show first 5
        print(f"  📝 {model}")

    if len(indic_models) > 5:
        print(f"  ... and {len(indic_models) - 5} more")

    # Check if any models support Tamil
    if not tamil_models:
        print("\n❌ No dedicated Tamil TTS models found in Coqui TTS library.")
        print("💡 Suggestions for Tamil TTS:")
        print("  1. Use Google Translate TTS API")
        print("  2. Use Azure Cognitive Services Text-to-Speech")
        print("  3. Use AWS Polly (supports Tamil)")
        print("  4. Use specialized Tamil TTS models from research")
        print("  5. Try Indic TTS models that might work with Tamil script")

        # Try to find any model that might work with Tamil
        print("\n🔍 Trying to find alternative approaches...")
        alternative_found = False

        # Check for any multilingual models that might support Indic scripts
        for model in all_models:
            model_str = str(model).lower()
            if 'multi' in model_str and ('indic' in model_str or 'script' in model_str):
                print(f"  💡 Alternative: {model}")
                alternative_found = True

        if not alternative_found:
            print("  📝 No direct alternatives found in current library")

except Exception as e:
    print(f"❌ Error checking models: {e}")
    print("💡 Alternative: Try using external TTS services for Tamil support")
